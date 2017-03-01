from bs4 import BeautifulSoup
#from urllib2 import urlopen
from urllib.request import urlopen
import urllib
import re
import csv
import os
import sys
import logging
#import justext
import datetime
import db


class Text():
    def __init__(self, html):
        soup = BeautifulSoup(html,'lxml')
        self.text = soup.find(["div"],{'class':'teksti'})
        self.chapters = list()
        self.getType()
        self.CleanChapters()
        self.GetMeta()
        #header = self.text.find("h3")
        #self.header = header.text

    def getType(self):
        self.p = self.text.findAll("p")
        self.prettified = self.text.prettify()
        if(len(self.p)<4):
            if "<br/>\n   <br/>\n" in self.prettified:
                self.title = self.text.find("h3").text
                self.IterateBr()
        else:
            if "Takaisin" in self.p[0].text:
                self.title = self.text.find("h1").text
                self.IterateP()

    def GetMeta(self):
        """Hae metatiedot alun taulukosta"""
        trs = self.text.findAll("tr")
        for tr in trs:
            tds = tr.findAll("td")
            setattr(self,tds[0].text.replace(":","").strip().lower().replace(" ","_").replace("ä","a").replace("-","_"),tds[1].text)

    def IterateP(self):
        for p in self.p[1:]:
            potentialheader = p.find("strong")
            if potentialheader:
                self.chapters.append(Chapter(potentialheader.text))
            else:
                if not self.chapters:
                    #If a chapter without headera encountered
                    self.chapters.append(Chapter())
                self.chapters[-1].paragraphs.append(p.text)

    def IterateBr(self):
        ps = self.text.findAll("p")
        body = ps[1]
        name = ps[2]
        wasbr = False
        elwasbr = False
        for el in body.children:
            if el.name=="strong":
                #otsikko suoraan ilman span-elementtiä
                self.chapters.append(Chapter(el.text))
            else:
                header = el.find("strong")
                if header and header != -1:
                    #otsikko span-elementin alla
                    self.chapters.append(Chapter(header.text))

            #Etsi kappaleenkatkaisua emoelementistä
            if el.name=="br" and not elwasbr:
                elwasbr = True
            elif elwasbr and el == " ":
                pass
            elif elwasbr and el.name == "br":
                self.chapters[-1].paragraphs.append("")
                elwasbr = False
            else:
                elwasbr = False

            try:
                for subel in el.contents:
                    #Etsi kappaleenkatkaisua lapsielementistä
                    if subel.name=="br" and wasbr:
                        wasbr=False
                        self.chapters[-1].paragraphs.append("")
                    elif subel.name=="br":
                        wasbr=True
                    else:
                        if isinstance(subel, str):
                            ptext = subel
                        else:
                            ptext = subel.text
                        if(len(ptext)>0):
                            #normaali tekstinoodi
                            self.chapters[-1].AddText(ptext)
                        wasbr=False
            except AttributeError:
                pass

    def CleanChapters(self):
        #Siisti:
        for chapter in self.chapters:
            for idx, par in enumerate(chapter.paragraphs):
                if not par:
                    del chapter.paragraphs[idx]
                else:
                    chapter.paragraphs[idx] = chapter.paragraphs[idx].strip()

    def InsertToDb(self, con):
        """Tulosta teksti ja metadata tiedostoihin"""
        dbtext = db.TextMeta(self.title,self.maa,self.korkeakoulu,self.vaihtoaika,self.vaihto_ohjelma,self.lahettava_laitos)
        dbchapters = list()
        for chapter in self.chapters:

            dbchapter = db.Chapter(chapter.name)
            dbparagraphs = list()

            for paragraph in chapter.paragraphs:
                dbparagraphs.append(db.Paragraph(paragraph))

            dbchapter.paragraphs = dbparagraphs
            dbchapters.append(dbchapter)

        dbtext.chapters = dbchapters
        con.insert(dbtext)



class Chapter():
    """Mahdollisesti otsikoitu kokonaisuus"""
    def __init__(self, name="unnamed"):
        self.name = name
        self.paragraphs = list()
    def AddText(self, ptext):
        if not self.paragraphs:
            self.paragraphs.append("")
        if ptext and ptext.strip() != self.name.strip():
            self.paragraphs[-1] += " " + ptext


#with open("linksource.html","r") as f:
#    html = f.read()

with open("test.xhtml","r") as f:
    html = f.read()

#with open("test3.html","r") as f:
#    html = f.read()

thistext = Text(html)
con = db.SqlaCon()
thistext.InsertToDb(con)

#spans = body.findAll("span")





#paragraphs = [x for x in body.contents if getattr(x, 'name', None) != 'br']

#links = soup.find_all(["a"],{'href':re.compile(r'.*matkakertomukset/kertomus.*')})
#for link in links:
#    href = link.get("href")


#'http://www.uta.fi/opiskelu/opiskelu_ulkomailla/matkakertomukset/kertomus.html?id=23181'

#paragraphs = justext.justext(body, justext.get_stoplist("Finnish"))
