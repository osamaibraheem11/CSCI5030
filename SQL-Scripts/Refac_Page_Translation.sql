/* Change Log															*/
/* Final - 5/7/2021 - Mounika Rajitha - Final update - Update database and table, then populate Lang_Ref Table with all languages	*/

use wordsense;


/* Adding Lang_ID column to Page translation */
alter table page_translation add column Lang_ID INT DEFAULT -1; 

/* Updating Lang_desc in Lang_ref to match Page_translation Lang_desc */
insert into Lang_ref (Lang_ID, Lang_Desc, Last_update)
values (4, "Spanish", Now()),
(5, "Irish", Now()),
(6, "Arabic", Now()),
(7, "Hindi", Now()),
(8, "Chinese", Now()),
(9, "Urdu", Now());

/* Updating Page translation languages to match Lang_ref */
update wordsense.page_translation set Lang_ID = '2' where Language_Page = 'French'; 
update wordsense.page_translation set Lang_ID = '3' where Language_Page = 'German';
update wordsense.page_translation set Lang_ID = '4' where Language_Page = 'Spanish';
update wordsense.page_translation set Lang_ID = '5' where Language_Page = 'Irish'; 
update wordsense.page_translation set Lang_ID = '6' where Language_Page = 'Arabic';
update wordsense.page_translation set Lang_ID = '7' where Language_Page = 'Hindi';
update wordsense.page_translation set Lang_ID = '8' where Language_Page = 'Chinese';
update wordsense.page_translation set Lang_ID = '9' where Language_Page = 'Urdu';

/* Set Lang_ID as Foreign key */
alter table page_translation ADD FOREIGN KEY(Lang_ID) REFERENCES lang_ref(Lang_ID);