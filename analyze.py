import db
import language
import re
import json
from utils import BuildString



def GetHeadVerbs(parsedstring, pidx, totalp, textid):
    sentences = parsedstring.strip().split("\n\n")
    for idx, sentencestring in enumerate(sentences):
        s = language.Sentence(sentencestring)
        h = s.GetVerbalHead()
        if h:
            try:
                pers = re.findall(r"Person=(\d)",h.feat)[0]
            except IndexError:
                pers = 0
            return {"lemma":h.lemma,"pers":pers,
                    "sentence_number":idx+1, "number_of_sentences":len(sentences),
                    "paragraph_number":pidx+1, "number_of_paragraphs":totalp,
                    "sentence": BuildString(s.tokens), "textid":textid}
        else:
            print("no head verb for this sentence: {}".format(BuildString(s.tokens)))



def CountHeadVerbsFromAsuminen(session):
    """Laske 
    """
    textids = session.query(db.TextMeta.id).filter(db.TextMeta.analyzed=="yes").all()
    verbs = list()
    print("Processing..")
    for tnumber, tid in enumerate(textids):
        chapterids = [thisid[0] for thisid in session.query(db.Chapter.id).filter(db.Chapter.text_id==tid[0]).all()]
        ps = session.query(db.Paragraph).filter(db.Paragraph.chapter_id.in_(chapterids)).filter(db.Paragraph.theme=="Asuminen").all()
        for pidx, p in enumerate(ps):
            verbs.append(GetHeadVerbs(p.parsed, pidx, len(ps), tid[0]))

    with open("data/headverbs.json","w") as f:
        json.dump(verbs, f, indent=4,ensure_ascii = False)

engine = db.create_engine('sqlite:///matkakertomukset.db', echo=False)
Session = db.sessionmaker(bind=engine)
session = Session()
CountHeadVerbsFromAsuminen(session)
