/* Change Log															*/
/* Alpha - 2/26/2021 - Garrett Reed - Initial Creation - Create and populate Speech_Parts Table with English and French	*/

use wordsense;

/* This is a good step to include in the case the existing table is corrupted in some way */
DROP TABLE IF EXISTS Speech_Parts;

/* Set up structure of table */
create table Speech_Parts (
	Part_ID INT NOT NULL AUTO_INCREMENT,
    Lang_ID INT NOT NULL,
	Part_Desc varchar(50) not null,
	Last_Update datetime not null,
	primary key (Part_ID),
    FOREIGN KEY (Lang_ID) REFERENCES Lang_Ref(Lang_ID));

/* Populate table with data */    
insert into Speech_Parts (Lang_ID, Part_Desc, Last_Update)
values (1,"Noun",Now()),
	(1,"Pronoun",Now()),
	(1,"Adjective",Now()),
	(1,"Adverb",Now()),
	(1,"Preposition",Now()),
    (1,"Conjunction",Now()),
    (1,"Article",Now()),
    (1,"Interjection",Now()),
    (2,"Adjectif",Now()),
	(2,"Adverbe",Now()),
	(2,"Article",Now()),
	(2,"Conjonction",Now()),
	(2,"Nom",Now()),
    (2,"Préposition",Now()),
    (2,"Pronom",Now()),
    (2,"Verbe",Now()),
    (3,"Adjektiv",Now()),
	(3,"Adverb",Now()),
	(3,"Präposition",Now()),
	(3,"Artikel",Now()),
	(3,"Conjunction",Now()),
    (3,"Pronomen",Now()),
    (3,"Zwischenruf",Now()),
    (3,"Conjunction",Now()),
    (3,"Substantiv",Now()),
    (3,"Eigenname",Now()),
    (3,"Verb",Now());
