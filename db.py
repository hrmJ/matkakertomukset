from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///matkakertomukset.db', echo=False)

class TextMeta(Base):
    """Metatiedot teksteistä"""
    # DB table
    __tablename__ = "textmeta"
    id = Column(Integer, primary_key=True)
    title = Column(String,default='unspecified')
    maa = Column(String,default='unspecified')
    korkeakoulu = Column(String,default='unspecified')
    vaihtoaika = Column(String,default='unspecified')
    vaihto_ohjelma = Column(String,default='unspecified')
    lahettava_laitos = Column(String,default='unspecified')
    analyzedby = Column(String,default='unspecified')
    analyzed = Column(String,default='unspecified')
    ispractice = Column(String,default='unspecified')

    def __init__(self,title='unspecified',maa='unspecified',korkeakoulu='unspecified',vaihtoaika='unspecified',vaihto_ohjelma='unspecified',lahettava_laitos='unspecified'):
        self.title = title
        self.maa = maa
        self.korkeakoulu = korkeakoulu
        self.vaihtoaika = vaihtoaika
        self.vaihto_ohjelma = vaihto_ohjelma
        self.lahettava_laitos = lahettava_laitos
        self.lahettava_laitos = lahettava_laitos

class Chapter(Base):
    """Tekstin seuraava taso, alaluvut (mahdollisesti vain yksi)"""
    __tablename__ = "chapters"
    header = Column(String,default='unspecified')
    id = Column(Integer, primary_key=True)
    text_id = Column(Integer, ForeignKey('textmeta.id'))
    text = relationship("TextMeta", backref=backref("chapters", order_by=id))

    def __init__(self,header="unspecified"):
        """ """
        self.header = header


class Paragraph(Base):
    """Tekstin pienin taso, kappaleet"""
    __tablename__ = "paragraphs"
    id = Column(Integer, primary_key=True)
    content = Column(String,default='')
    theme = Column(String,default='')
    parsed = Column(String,default='')
    #text_id = Column(Integer, ForeignKey('textmeta.id'))
    chapter_id = Column(Integer, ForeignKey('chapters.id'))
    ##Itext = relationship("TextMeta", backref=backref("textmeta", order_by=id))
    chapter = relationship("Chapter", backref=backref("paragraphs", order_by=id))

    def __init__(self,content="",theme="", parsed=""):
        """ """
        self.content = content
        self.theme = theme
        self.parsed = parsed


class SqlaCon:
    """Autoconn:ct to sqlite via sqlalchemy"""

    def __init__(self):
        self.Base = Base
        self.engine = engine

    def LoadSession(self):
        """"""
        metadata = self.Base.metadata
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        
    def insert(self, dbobj):
        """Insert via sqla"""
        self.LoadSession()
        self.session.add(dbobj)
        self.session.commit()

Base.metadata.create_all(engine)
