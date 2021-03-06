import db
import language
from language import re
import json
from utils import BuildString
import sys

def PrintText(t_id):
    """
    t_id: id of the text to be printed
    """
    engine = db.create_engine('sqlite:///matkakertomukset.db', echo=False)
    Session = db.sessionmaker(bind=engine)
    session = Session()
    chapterids = [cid[0] for cid in session.query(db.Chapter.id).filter(db.Chapter.text_id == t_id).all()]
    ps = session.query(db.Paragraph).filter(db.Paragraph.chapter_id.in_(chapterids)).all()
    for p in ps:
        print("{}\n\n".format(p.content))

def TextStats(fname):
    """
    fname: the file containing the ids of the texts
    """
    engine = db.create_engine('sqlite:///matkakertomukset.db', echo=False)
    Session = db.sessionmaker(bind=engine)
    with open(fname,"r") as f:
        text_ids = json.loads(f.read())
    session = Session()
    alltext = list()
    for idx, tid in enumerate(text_ids):
        if idx % 10 == 0:
            print("{}/{}".format(idx, len(text_ids)))
        chapterids = [cid[0] for cid in session.query(db.Chapter.id).filter(db.Chapter.text_id == tid).all()]
        ps = session.query(db.Paragraph).filter(db.Paragraph.chapter_id.in_(chapterids)).all()
        words_text = 0
        sentences_text = 0
        for p in ps:
            if p.parsed:
                for sentence_number, sentence_string in enumerate(p.parsed.strip().split("\n\n")):
                    s = language.Sentence(sentence_string)
                    words_text += len([w for w in s.words if w.deprel.lower() not in ["punct","punc"]])
                    sentences_text += 1
        alltext.append({"text_id":tid,"paragraphs":len(ps),"sentences":sentences_text,"words":words_text})
    outputfile = "data/text_stats.json"
    with open(outputfile,"w") as f:
        json.dump(alltext,f,indent=4,ensure_ascii = False)
    print("Done! Data saved in " + outputfile)

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

            allps = session.query(db.Paragraph).filter(db.Paragraph.chapter_id.in_(chapterids)).all()
            allps_dict = dict()
            for thisp in allps:
                allps_dict[thisp.id] = thisp.content

            if len(ps)>3:
                pamounts["n"]+=1
            else:
                pamounts[len(ps)]+=1

            for pidx, p in enumerate(ps):
                try:
                    p.previous_paragraph = allps_dict[p.id-1]
                except KeyError:
                    p.previous_paragraph = ""
                p.chaptertitle = session.query(db.Chapter.header).filter(db.Chapter.id==p.chapter_id).first()[0]
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
            p.wordnumber=p.aswordsnumber = 0
            indicator_has_been_found = False
            p.numberoffeats=0
            for sentence_number, sentence_string in enumerate(p.parsed.strip().split("\n\n")):
                s = language.Sentence(sentence_string)
                s.CheckIfAsuminen()
                s.GetVerbalHead()
                s.CountAsuminenWords(p)
                p.numberoffeats+=s.numberoffeats
                if s.asuminen_expressed_in != "None" and not indicator_has_been_found:
                    indicator_has_been_found = True
                    hvlemma=hvperson=hvfeat=""
                    if hasattr(s, "headverb"):
                        hvlemma= s.headverb.lemma
                        hvfeat= s.headverb.feat
                        try:
                            pers = re.search(r"Number=(\w+).*Person=(\d+)",s.headverb.feat,re.I)
                            hvperson = "{}.{}".format(pers.group(1),pers.group(2))
                        except AttributeError:
                            hvperson = "--"
                    try:
                        feats = p.numberoffeats/p.wordnumber
                    except ZeroDivisionError:
                        feats = 0
                    self.data.append({"asuminen_expressed": s.asuminen_expressed_in,
                                      "headverb_lemma":hvlemma,
                                      "sentence_number":sentence_number+1,
                                      "headverb_person":hvperson,
                                      "headverb_feat":hvfeat,
                                      "previous_paragraph": p.previous_paragraph,
                                      "chaptertitle": p.chaptertitle,
                                      "featmean":feats,
                                      "first_word_of_sentence_token": s.words[0].token if "pun" not in s.words[0].pos.lower() else s.words[1].token,
                                      "first_word_of_sentence_lemma": s.words[0].lemma if "pun" not in s.words[0].pos.lower() else s.words[1].lemma,
                                      "indicatorword": s.asuminen_expressed_by,
                                      "indicatorword_token": s.asuminen_expressed_by_token,
                                      "indicatorword_feat": s.iw.feat,
                                      "number_of_paragraphs":p.ptotal,
                                      "paragraph":p.content,
                                      "head_of_indicator":s.iwhead,
                                      "head_of_indicator_loc":s.iwheadloc.strip(";"),
                                      "indicatorloc":s.indicatorloc.strip(";"),
                                      "sentence": BuildString(s.tokens), "textid":p.textid})

                self.data[-1].update({"words_total":p.wordnumber, "indicatorwords":p.aswordsnumber})


#hv = HeadverbStats()
fs = FirstSentenceStats()

