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

class Text():
    def __init__(self, html):
        soup = BeautifulSoup(html,'lxml')
        text = soup.find(["div"],{'class':'teksti'})
        header = text.find("h3")
        self.header = header.text
        ps = text.findAll("p")
        self.body = ps[1]
        self.name = ps[2]
        self.Iterate()

    def Iterate(self):
        chapters = list()
        wasbr = False
        elwasbr = False
        for el in self.body.children:
            if el.name=="strong":
                #otsikko suoraan ilman span-elementtiä
                chapters.append(Chapter(el.text))
            else:
                header = el.find("strong")
                if header and header != -1:
                    #otsikko span-elementin alla
                    chapters.append(Chapter(header.text))

            #Etsi kappaleenkatkaisua emoelementistä
            if el.name=="br" and not elwasbr:
                elwasbr = True
            elif elwasbr and el == " ":
                pass
            elif elwasbr and el.name == "br":
                chapters[-1].paragraphs.append("")
                elwasbr = False
            else:
                elwasbr = False

            try:
                for subel in el.contents:
                    #Etsi kappaleenkatkaisua lapsielementistä
                    if subel.name=="br" and wasbr:
                        wasbr=False
                        chapters[-1].paragraphs.append("")
                    elif subel.name=="br":
                        wasbr=True
                    else:
                        if isinstance(subel, str):
                            ptext = subel
                        else:
                            ptext = subel.text
                        if(len(ptext)>0):
                            #normaali tekstinoodi
                            chapters[-1].AddText(ptext)
                        wasbr=False
            except AttributeError:
                pass

        #Siisti:
        for chapter in chapters:
            for idx, par in enumerate(chapter.paragraphs):
                if not par:
                    del chapter.paragraphs[idx]
                else:
                    chapter.paragraphs[idx] = chapter.paragraphs[idx].strip()


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

        #tuhoa tyhjät kappaleet
        if self.paragraphs[0] != self.paragraphs[-1] and not self.paragraphs[0]:
            del self.paragraphs[0]


#with open("linksource.html","r") as f:
#    html = f.read()

with open("test.xhtml","r") as f:
    html = f.read()

thistext =Text(html)

#spans = body.findAll("span")





#paragraphs = [x for x in body.contents if getattr(x, 'name', None) != 'br']

#links = soup.find_all(["a"],{'href':re.compile(r'.*matkakertomukset/kertomus.*')})
#for link in links:
#    href = link.get("href")


#'http://www.uta.fi/opiskelu/opiskelu_ulkomailla/matkakertomukset/kertomus.html?id=23181'

#paragraphs = justext.justext(body, justext.get_stoplist("Finnish"))
