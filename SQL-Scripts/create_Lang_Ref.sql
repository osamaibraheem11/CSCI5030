/* Change Log															*/
/* Alpha - 2/26/2021 - Garrett Reed - Initial Creation - Create database and table, then populate Lang_Ref Table with English and French	*/

/* Create Database */
Create database if not exists wordsense;
use wordsense;
 
/* This is a good step to include in the case the existing table is corrupted in some way */
drop table if exists Lang_Ref;

/* Set up structure of table */
create table Lang_Ref (
Lang_ID INT NOT NULL AUTO_INCREMENT, 
Lang_Desc varchar(50) not null,
Last_update datetime not null,
primary key (Lang_ID));

/* Populate table with data */
insert into Lang_ref (Lang_Desc, Last_update)
values ("English", Now()),
("français", Now());