/* Change Log															*/
/* Beta - 4/4/2021 - Garrett Reed - Initial Creation - Load German Corpus	*/
/* Tags can be found here: https://universaldependencies.org/u/pos/	*/
/* Instructions	*/
/* You will need the corpus on your local machine as well.	*/
/* Set the filepath to whatever it should be for your local machine.	*/
/* You may need to add these two lines to your Advanced DB connection settings	*/
/* AllowLoadLocalInfile=true	*/
/* OPT_LOCAL_INFILE=1	*/


SET GLOBAL local_infile = true; 
LOAD DATA LOCAL INFILE "C:\\Users\\Garth\\Documents\\GitHub\\CSCI5030\\Corpora\\deu-de_web-wrt_2019_100K-sentences_tagged.txt" INTO table german_corpus
CHARACTER SET utf8
FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n'
(@col1,@col2) set Line_ID=@col1,lang_id=(select lang_id from lang_ref where lang_desc = "Deutsche"),Doc_ID="1",Doc_Name="deu-de_web-wrt_2019_100K-sentences_tagged",Line_Text=@col2,Last_Update=Now();
