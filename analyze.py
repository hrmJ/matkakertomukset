import db
import language
import re
import json
from utils import BuildString



def GetHeadVerbs(sentencestring, sidx, totals, pidx, totalp, textid):
    s = language.Sentence(sentencestring)
    h = s.GetVerbalHead()
    if h:
        try:
            pers = re.findall(r"Person=(\d)",h.feat)[0]
        except IndexError:
            pers = 0
        return {"lemma":h.lemma,"pers":pers,
                "sentence_number":sidx+1, "number_of_sentences":totals,
                "paragraph_number":pidx+1, "number_of_paragraphs":totalp,
                "sentence": BuildString(s.tokens), "textid":textid}
    else:
        print("no head verb for this sentence: {}".format(BuildString(s.tokens)))
        return False



def CountHeadVerbsFromAsuminen(textids, session):
    """Laske 
    """
    verbs = list()
    for tnumber, tid in enumerate(textids):
        chapterids = [thisid[0] for thisid in session.query(db.Chapter.id).filter(db.Chapter.text_id==tid[0]).all()]
        ps = session.query(db.Paragraph).filter(db.Paragraph.chapter_id.in_(chapterids)).filter(db.Paragraph.theme=="Asuminen").all()
        for pidx, p in enumerate(ps):
            sentences = p.parsed.strip().split("\n\n")
            for idx, sentencestring in enumerate(sentences):
                thisverb = GetHeadVerbs(sentencestring, idx, len(sentences), pidx, len(ps), tid[0])
                if thisverb:
                    verbs.append(thisverb)

    with open("data/headverbs.json","w") as f:
        json.dump(verbs, f, indent=4,ensure_ascii = False)

def GeneralStatitics(session, textids):
    """Laske 
    """
    allparagraphs = list()
    ps_with_theme_asuminen = 0
    pamounts={0:0, 1:0,2:0,3:0,"n":0}
    for tnumber, tid in enumerate(textids):
        chapterids = [thisid[0] for thisid in session.query(db.Chapter.id).filter(db.Chapter.text_id==tid[0]).all()]
        ps = session.query(db.Paragraph).filter(db.Paragraph.chapter_id.in_(chapterids)).filter(db.Paragraph.theme=="Asuminen").all()
        if len(ps)>3:
            pamounts["n"]+=1
        else:
            pamounts[len(ps)]+=1
        for pidx, p in enumerate(ps):
            ps_with_theme_asuminen += 1

    output = {"tekstit":len(textids),"asumiskappaleet":ps_with_theme_asuminen, "kpl_0":pamounts[0],"kpl_1":pamounts[1],"kpl_2":pamounts[2],"kpl_3":pamounts[3],"kpl_n":pamounts["n"]}
    with open("data/genstats.json","w") as f:
        json.dump(output, f, indent=4,ensure_ascii = False)

engine = db.create_engine('sqlite:///matkakertomukset.db', echo=False)
Session = db.sessionmaker(bind=engine)
session = Session()
textids = session.query(db.TextMeta.id).filter(db.TextMeta.analyzed=="yes").all()

CountHeadVerbsFromAsuminen(textids, session)
#GeneralStatitics(session, textids)
