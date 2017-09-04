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
    errors = ""
    def __init__(self, html, address=""):
        self.address = address
        soup = BeautifulSoup(html,'lxml')
        self.text = soup.find(["div"],{'class':'teksti'})
        self.chapters = list()
        self.getType()
        self.CleanChapters()
        self.GetMeta()
        self.hasfailed = False
        self.title = ""
        #header = self.text.find("h3")
        #self.header = header.text

    def getType(self):
        self.p = self.text.findAll("p")
        self.prettified = self.text.prettify()
        if(len(self.p)<4):
            if "<br/>\n   <br/>\n" in self.prettified:
                self.title = self.text.find("h3").text
                try:
                    self.IterateBr()
                except IndexError:
                    Text.errors += self.address + "\n"
                    self.hasfailed = True
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
        print("Scraping " + self.address)
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
        print("Scraping " + self.address)
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
        if self.hasfailed:
            return False
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


con = db.SqlaCon()

with open("linksource.html","r") as f:
    soup = BeautifulSoup(f.read(),'lxml')

links = soup.find_all(["a"],{'href':re.compile(r'.*matkakertomukset/kertomus.*')})
for idx, link in enumerate(links):
    href = link.get("href")
    try:
        thistext = Text(urlopen(href).read(), href)
        #thistext.InsertToDb(con)
        print (thistext.prettified);
    except:
        if href not in Text.errors:
            Text.errors += href + "\n"
            print(href + "FAILED!")
    print("{}/{}".format(idx,len(links)),end="\r")
    if idx % 100 == 0:
        break

print("\n\nDone. Errors with the following hrefs:\n {}.".format(Text.errors))

