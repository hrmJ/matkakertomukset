import db
import subprocess


engine = db.create_engine('sqlite:///matkakertomukset.db', echo=False)
Session = db.sessionmaker(bind=engine)
session = Session()
chapterdata = session.query(db.Paragraph.id, db.Paragraph.content, db.Paragraph.parsed).all()
for idx, row in enumerate(chapterdata):
    if not row.parsed:
        ps = subprocess.Popen(('echo', row[1]), stdout=subprocess.PIPE, cwd=r"/home/juho/Projects/corpora/Finnish-dep-parser/")
        try:
            output = subprocess.check_output(('./parser_wrapper.sh', 'process_name'), cwd=r"/home/juho/Projects/corpora/Finnish-dep-parser/", stdin=ps.stdout)
            rowparsed = output.decode("utf-8")
            newparsed = session.query(db.Paragraph).filter_by(id=row.id).update(dict(parsed=rowparsed))
        except:
            print("Error parsing...")
    print("{}/{}".format(idx,len(chapterdata)),end="\r")
session.commit()
print("\n\nDone.")

