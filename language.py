
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
                            return dep
                else:
                    return w


class Word():
    def __init__(self, raw):
        props = raw.split("\t")
        self.tokenid = int(props[0])
        self.token = props[1]
        self.lemma = props[2]
        self.head = int(props[6])
        self.pos = props[3]
        self.feat = props[5]

    def GetDependents(self, words):
        """Listaa kaikki sanan dependentit"""
        self.dependents = list()
        for w in words:
            if w.head == self.tokenid:
                self.dependents.append(w)
        return self.dependents
