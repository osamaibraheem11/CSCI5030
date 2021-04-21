/* Change Log															*/
/* Alpha - 3/9/2021 - Garrett Reed - Initial Creation - Create English and French Corpus Tables	*/

/*
Hi Garrett et al  Even though I don't care about this being developed "at scale", I would like it to be "scalable"! 

Your proposed data model would work for a small corpus it doesn't really work when you get to, say, a few million words. 
Focus on the fast lookup you need. Given a word+POS, you want to retrieve all sentences containing that word. 
If I were doing this in Python, that might look like a dictionary that has the words/part-of-speech tags as keys, and something like a list of sentence IDs as values:

{ "sink/NOUN": [4, 8, 23, 141], "good/ADJ": [1,2,7,14,16,143], ...}

In short you'd like to be able to reproduce this fast lookup of sentence IDs with your database.
*/
use wordsense;

/* This is a good step to include in the case the existing table is corrupted in some way */
DROP TABLE IF EXISTS English_Corpus;

/* Set up structure of English corpus table */
create table English_Corpus (
	Line_ID INT NOT NULL AUTO_INCREMENT,
    Lang_ID INT NOT NULL,
    Doc_ID INT NOT NULL,
    Doc_Name varchar(25),
	Line_Text blob not null,
	Last_Update datetime not null,
	primary key (Line_ID),
    FOREIGN KEY (Lang_ID) REFERENCES Lang_Ref(Lang_ID));


/* This is a good step to include in the case the existing table is corrupted in some way */
DROP TABLE IF EXISTS French_Corpus;

/* Set up structure of French corpus table */
create table French_Corpus (
	Line_ID INT NOT NULL AUTO_INCREMENT,
    Lang_ID INT NOT NULL,
    Doc_ID INT NOT NULL,
    Doc_Name varchar(25),
	Line_Text blob not null,
	Last_Update datetime not null,
	primary key (Line_ID),
    FOREIGN KEY (Lang_ID) REFERENCES Lang_Ref(Lang_ID));
    

DROP TABLE IF EXISTS English_Index;
    
/* Set up structure of English index table */
create table English_Index (
    Word_Speech varchar(50),
    Lang_ID INT NOT NULL,
	Line_ID INT NOT NULL,
	Last_Update datetime not null,
	primary key (Word_Speech, Lang_ID),
    FOREIGN KEY (Lang_ID) REFERENCES Lang_Ref(Lang_ID),
    FOREIGN KEY (Line_ID) REFERENCES English_Corpus(Lang_ID));
    
    
    DROP TABLE IF EXISTS French_Index;
    
/* Set up structure of French index table */
create table French_Index (
    Word_Speech varchar(50),
    Lang_ID INT NOT NULL,
	Line_ID INT NOT NULL,
	Last_Update datetime not null,
	primary key (Word_Speech, Lang_ID),
    FOREIGN KEY (Lang_ID) REFERENCES Lang_Ref(Lang_ID),
    FOREIGN KEY (Line_ID) REFERENCES English_Corpus(Lang_ID));