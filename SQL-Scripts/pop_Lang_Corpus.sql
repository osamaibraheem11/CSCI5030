/* Change Log															*/
/* Alpha - 3/9/2021 - Garrett Reed - Initial Creation - Populate English and French Corpus and Index Tables with a test record */

use wordsense;

/* Populate corpus tables with data */    
insert into English_Corpus (Lang_ID, Doc_ID, Doc_Name, Line_Text, Last_Update)
values (1,
	1,
    "ca01-test-en",
    "The/at Fulton/np-tl County/nn-tl Grand/jj-tl Jury/nn-tl said/vbd Friday/nr an/at investigation/nn of/in Atlanta's/np$ recent/jj primary/nn election/nn produced/vbd ``/`` no/at evidence/nn ''/'' that/cs any/dti irregularities/nns took/vbd place/nn ./.",
    Now());
    
   
insert into French_Corpus (Lang_ID, Doc_ID, Doc_Name, Line_Text, Last_Update)
values (2,
	1,
    "ca01-test-fr",
    "The/at Fulton/np-tl County/nn-tl Grand/jj-tl Jury/nn-tl said/vbd Friday/nr an/at investigation/nn of/in Atlanta's/np$ recent/jj primary/nn election/nn produced/vbd ``/`` no/at evidence/nn ''/'' that/cs any/dti irregularities/nns took/vbd place/nn ./.",
    Now());
    
    

    
    
/* Populate indexed tables with data */ 
insert into English_Index (Word_Speech, Lang_ID, Line_ID, Last_Update )
values ("primary/nn",
	1,
    1,
    Now());
    
insert into French_Index (Word_Speech, Lang_ID, Line_ID, Last_Update )
values ("primary/nn",
	2,
    1,
    Now());