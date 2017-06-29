import db
import language
from language import re
import json
from utils import BuildString


class Analysis():

    paragraphs = list()
    textids = list()

    def __init__(self):
        if not Analysis.paragraphs:
            self.LoadParagraphs()
        self.data = list()
        self.Analyze()
        self.WriteResults()

    def LoadParagraphs(self):
        print("Loading paragraphs...")
        engine = db.create_engine('sqlite:///matkakertomukset.db', echo=False)
        Session = db.sessionmaker(bind=engine)
        session = Session()
        textids = session.query(db.TextMeta.id).filter(db.TextMeta.analyzed=="yes").all()
        Analysis.textids = textids
        pamounts={0:0, 1:0,2:0,3:0,"n":0}
        for tnumber, tid in enumerate(textids):
            chapterids = [thisid[0] for thisid in session.query(db.Chapter.id).filter(db.Chapter.text_id==tid[0]).all()]
            ps = session.query(db.Paragraph).filter(db.Paragraph.chapter_id.in_(chapterids)).filter(db.Paragraph.theme=="Asuminen").all()

            if len(ps)>3:
                pamounts["n"]+=1
            else:
                pamounts[len(ps)]+=1

            for pidx, p in enumerate(ps):
                p.textid = tid[0]
                p.pnumber = pidx + 1
                p.ptotal = len(ps)
                Analysis.paragraphs.append(p)
            if tnumber % 100 == 0:
                print("{}/{}".format(tnumber,len(textids)))

        with open("data/genstats.json","w") as f:
            json.dump({"tekstit":len(textids),"asumiskappaleet":len(Analysis.paragraphs), "kpl_0":pamounts[0],"kpl_1":pamounts[1],"kpl_2":pamounts[2],"kpl_3":pamounts[3],"kpl_n":pamounts["n"]}, f, indent=4,ensure_ascii = False)

    def Analyze(self):
        print("Performing analysis: " + self.name)
        for p in Analysis.paragraphs:
            self.ProcessParagraph(p)

    def WriteResults(self):
        with open("data/" + self.name + ".json","w") as f:
            json.dump(self.data, f, indent=4,ensure_ascii = False)
        print("Results saved.")


class HeadverbStats(Analysis):
    """Laske tilastoja virkkeiden pääverbeistä."""
    def __init__(self):
        self.name = "headverbs"
        super().__init__()

    def ProcessParagraph(self, p):
        sentences = p.parsed.strip().split("\n\n")
        for idx, sentencestring in enumerate(sentences):
            s = language.Sentence(sentencestring)
            h = s.GetVerbalHead()
            if h:
                try:
                    pers = re.findall(r"Person=(\d)",h.feat)[0]
                except IndexError:
                    pers = 0
                self.data.append({"lemma":h.lemma,"pers":pers,
                                  "sentence_number":idx+1, "number_of_sentences":len(sentences),
                                  "paragraph_number":p.pnumber, "number_of_paragraphs":p.ptotal,
                                  "sentence": BuildString(s.tokens), "textid":p.textid})
            else:
                print("no head verb for this sentence: {}".format(BuildString(s.tokens)))

class FirstSentenceStats(Analysis):
    """Laske tilastoja virkkeiden pääverbeistä."""
    def __init__(self):
        self.name = "firstsentence"
        super().__init__()

    def ProcessParagraph(self, p):
        if p.pnumber == 1:
            sentences = p.parsed.strip().split("\n\n")
            s = language.Sentence(sentences[0])
            s.CheckIfAsuminen()
            self.data.append({"asuminen_expressed": s.asuminen_expressed_in,
                              "indicatorword": s.asuminen_expressed_by,
                              "number_of_paragraphs":p.ptotal,
                              "paragraph":p.content,
                              "head_of_indicator":s.iwhead,
                              "sentence": BuildString(s.tokens), "textid":p.textid})


#hv = HeadverbStats()
fs = FirstSentenceStats()

