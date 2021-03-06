
ALTER TABLE paragraphs ADD COLUMN analyzedby VARCHAR;
ALTER TABLE paragraphs ADD COLUMN locked INTEGER;
UPDATE paragraphs SET locked = 0;

ALTER TABLE textmeta ADD COLUMN analyzed VARCHAR;
UPDATE textmeta set analyzed = 'no';
ALTER TABLE textmeta ADD COLUMN ispractice VARCHAR;
UPDATE textmeta set ispractice = 'ei';

ALTER TABLE paragraphs ADD COLUMN ispractice VARCHAR;
UPDATE paragraphs set ispractice = 'ei';


CREATE TABLE themes(id INTEGER, theme VARCHAR, PRIMARY KEY(id ASC));

INSERT INTO themes (theme) VALUES ('etukäteisjärjestelyt');
INSERT INTO themes (theme) VALUES ('kielikurssi');
INSERT INTO themes (theme) VALUES ('kohdemaahan saapuminen');
INSERT INTO themes (theme) VALUES ('asuminen');
INSERT INTO themes (theme) VALUES ('opiskelu');
INSERT INTO themes (theme) VALUES ('muuta mainitsemisen arvoista');
INSERT INTO themes (theme) VALUES ('paluu tampereelle');
INSERT INTO themes (theme) VALUES ('merkityksellisyys');
INSERT INTO themes (theme) VALUES ('kritiikkiä tai kiitoksia');
INSERT INTO themes (theme) VALUES ('muu');
