import constants
import re

class Sentence():
    def __init__(self, raw):
        self.words = list()
        self.tokens = list()
        for line in raw.splitlines():
            self.words.append(Word(line))
            self.tokens.append(self.words[-1].token)

    def GetVerbalHead(self):
        """
        Hae virkkeestä sen juuri. Jos juuri ei ole verbi (esim. ), hae juuren dependenteistä 
        ensimmäinen verbi
        """
        for w in self.words:
            if w.head == 0:
                if w.pos != "VERB":
                    for dep in w.GetDependents(self.words):
                        if dep.pos == "VERB":
                            self.headverb = w
                            return dep
                else:
                    self.headverb = w
                    return w

    def CheckIfAsuminen(self):
        self.asuminen_expressed_in=self.asuminen_expressed_by_feat=self.indfeat=self.asuminen_expressed_by_token=self.asuminen_expressed_by=self.iwhead=self.iwheadloc=self.indicatorloc= ""
        feats = 0
        self.iw = Word("0\t"*8)
        for w in self.words: 
            w.GetHeadWord(self.words)
            iwords = 0
            if w.deprel.lower() not in ["punc","punct"]:
                feats += w.feat.count("|") +1  # plus 1 koska nolla ei oikeasti mahd.
            if re.search("(" + "|".join(constants.asuminen) + ")", w.lemma) and re.search(constants.asuminen_strict, w.lemma):
                #Jos sana on asua-verbin johdos
                iwords += 1
                if self.asuminen_expressed_in:
                    #jos ei virkkeen eka asua-johdos
                    self.asuminen_expressed_in += ";" + w.deprel
                    self.asuminen_expressed_by += ";" + w.lemma
                    self.asuminen_expressed_by_token += ";" + w.token
                    self.indicatorloc += ";" + str(w.GetRealLocation(self.words))
                    if w.headword:
                        self.iwhead += ";" + w.headword.lemma
                        self.iwheadloc += ";" + str(w.headword.GetRealLocation(self.words))
                else:
                    self.iw = w
                    self.asuminen_expressed_in = w.deprel
                    self.asuminen_expressed_by = w.lemma
                    self.indicatorloc = str(w.GetRealLocation(self.words))
                    if w.headword:
                        self.iwhead = w.headword.lemma
                        self.iwheadloc = str(w.headword.GetRealLocation(self.words))
        if not self.asuminen_expressed_in:
            self.asuminen_expressed_in = "None"
            self.asuminen_expressed_by = "None"
            self.asuminen_expressed_by_token = "None"
            self.asuminen_expressed_by_feat = "None"
        self.numberoffeats = feats

    def CountAsuminenWords(self, p):
        """@param Paragraph p kappale, jossa lause esiintyy"""
        for w in self.words:
            if w.deprel.lower() not in ["punc","punct"]:
                p.wordnumber += 1
                if w.lemma in constants.asuminen and re.search(constants.asuminen_strict, w.lemma):
                    p.aswordsnumber += 1


class Word():
    def __init__(self, raw):
        props = raw.split("\t")
        self.tokenid = int(props[0])
        self.token = props[1]
        self.lemma = props[2]
        self.head = int(props[6])
        self.pos = props[3]
        self.feat = props[5]
        self.deprel = props[7]
        self.headword = ""

    def GetDependents(self, words):
        """Listaa kaikki sanan dependentit"""
        self.dependents = list()
        for w in words:
            if w.head == self.tokenid:
                self.dependents.append(w)
        return self.dependents

    def GetHeadWord(self, words):
        """Etsi sanan pääsana ja palauta word-olio"""
        for w in words:
            if w.tokenid == self.head:
                self.headword = w
                return self.headword

    def GetRealLocation(self, words):
        """Määritä sanan sijainti niin, ettei välimerkkejä oteta huomioon"""
        self.loc = 0
        for w in words:
            if w.deprel.lower() not in ["punc","punct"]:
                self.loc += 1
            if w == self:
                break
        return self.loc
