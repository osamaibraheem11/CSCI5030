# Author: Pankil Shah
# Created on: 03/13/2021
# Description: Parse a corpus and dump the sentences into the database 

from nltk.corpus import brown
import nltk.data
import logic
import datetime
from os import listdir
from os.path import isfile, join

#print(brown.tagged_sents()[0:2])

#dirPath = 'E:\\SLU\\Sem1\\Principles of SD\\Project Material\\brown'
path = input("Enter path of the corpus directory: ")
language = input("Enter language: ")
#language = "english"

# list of all file names in the corpus directory
fileNameList = [f for f in listdir(path) if isfile(join(path, f))]
languageId = str(logic.SQLQuery("select Lang_ID from lang_ref where Lang_Desc = '" + language + "'")[0])

for fileName in fileNameList:

    # ignore the files CONTENTS and README
    if (fileName != "CONTENTS") and (fileName != "README"):
        filePath = path + '\\' + fileName
        with open(filePath, 'r') as file:
            text = file.read().replace('\n', '')

        sent_detector = nltk.data.load('tokenizers/punkt/' + language.lower() + '.pickle')
        sentenceList = sent_detector.tokenize(text.strip())

        values = ""
        # form the values string required in insert query
        for sentence in sentenceList:
            values += "(" + languageId + ", 1, " + "'" + fileName + "', " + "\"" + sentence + "\", " + "'" + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "'),"

        # remove last comma from values string    
        values = values[:-1]

        corpusTable = language.lower() + "_corpus"
        query = "insert into " + corpusTable + " (Lang_ID, Doc_ID, Doc_Name, Line_Text, Last_Update) values " + values
        logic.SQLInsertQuery(query)

