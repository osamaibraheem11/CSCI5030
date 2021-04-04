/* Change Log															*/
/* Beta - 4/4/2021 - Garrett Reed - Initial Creation - Create German Reference Tables and Data	*/

use wordsense;

/* Create table structures */
DROP TABLE IF EXISTS German_Index;
DROP TABLE IF EXISTS German_Corpus;

create table German_Corpus (
	Line_ID INT NOT NULL AUTO_INCREMENT,
    Lang_ID INT NOT NULL,
    Doc_ID INT NOT NULL,
    Doc_Name varchar(25),
	Line_Text longtext not null,
	Last_Update datetime not null,
	primary key (Line_ID),
    FOREIGN KEY (Lang_ID) REFERENCES Lang_Ref(Lang_ID));
    
create table German_Index (
    Word_Speech varchar(50),
    Lang_ID INT NOT NULL,
	Line_ID INT NOT NULL,
	Last_Update datetime not null,
	primary key (Word_Speech, Lang_ID),
    FOREIGN KEY (Lang_ID) REFERENCES Lang_Ref(Lang_ID),
    FOREIGN KEY (Line_ID) REFERENCES German_Corpus(Lang_ID));

 
 /* Start populating data */
 
delete from lang_ref where lang_id > 0 and Lang_Desc = "Deutsche";
insert into Lang_ref (Lang_Desc, Last_update)
values ("Deutsche", Now());

insert into Speech_Parts (Lang_ID, Part_Desc, Last_Update)
values ((
	select distinct lang_id 
    from Lang_ref 
    where Lang_Desc = "Deutsche"),"Adjektiv",Now()),
	((
	select distinct lang_id 
    from Lang_ref 
    where Lang_Desc = "Deutsche"),"Adverb",Now()),
	((
	select distinct lang_id 
    from Lang_ref 
    where Lang_Desc = "Deutsche"),"Zwischenruf",Now()),
	((
	select distinct lang_id 
    from Lang_ref 
    where Lang_Desc = "Deutsche"),"Substantiv",Now()),
    ((
	select distinct lang_id 
    from Lang_ref 
    where Lang_Desc = "Deutsche"),"Pronomen",Now()),
    ((
	select distinct lang_id 
    from Lang_ref 
    where Lang_Desc = "Deutsche"),"Eigenname",Now()),
    ((
	select distinct lang_id 
    from Lang_ref 
    where Lang_Desc = "Deutsche"),"Verb",Now());