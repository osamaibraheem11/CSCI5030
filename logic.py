# This file will hold useful functions
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from datetime import datetime
import logic
import itertools
import os.path
import json

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'Osamas-MacBook-Pro.local'
# app.config['MYSQL_USER'] = 'Osama'
# app.config['MYSQL_PASSWORD'] = 'CSCI5030SLU2021'
# app.config['MYSQL_DATABASE_DB'] = 'wordsense'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'pnkls'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'wordsense'

mysql = MySQL(app)
conn = mysql.connect()
cursor = conn.cursor()

english_pos_mapping = {
    "NN":"Noun", 
    "NN$":"Noun",
    "NNS":"Noun",
    "NNS$":"Noun",
    "NP":"Noun",
    "NP$":"Noun",
    "NPS":"Noun",
    "NPS$":"Noun",
    "NR":"Noun",
    "NRS":"Noun",
    "VB":"Verb",
    "VBD":"Verb",
    "VBG":"Verb",
    "VBN":"Verb",
    "VBP":"Verb",
    "VBZ":"Verb",
    "PN":"Pronoun",
    "PN$":"Pronoun",
    "PP$":"Pronoun",
    "PP$$":"Pronoun",
    "PPL":"Pronoun",
    "PPLS":"Pronoun",
    "PPO":"Pronoun",
    "PPS":"Pronoun",
    "PPSS":"Pronoun",
    "WP$":"Pronoun",
    "WPO":"Pronoun",
    "WPS":"Pronoun",
    "JJ":"Adjective",
    "JJR":"Adjective",
    "JJS":"Adjective",
    "JJT":"Adjective",
    "RB":"Adverb",
    "RBR":"Adverb",
    "RBT":"Adverb",
    "RN":"Adverb",
    "RP":"Adverb",
    "WRB":"Adverb",
    "CC":"Conjunction",
    "CS":"Conjunction",
    "AT":"Article",
    "UH":"Interjection"
}

def tuple2list(ExTuple):
    ExList = list(itertools.chain(*ExTuple))
    return ExList 

def SQLQuery(statment):
    cursor.execute(statment)
    conn.commit()
    data = logic.tuple2list(cursor.fetchall()) 
    return data

def SQLInsertQuery(statment):
    cursor.execute(statment)
    conn.commit()

def GetLanguageId(language):
    language_id_list = logic.SQLQuery("select Lang_ID from lang_ref where Lang_Desc = '" + language + "'")
    if len(language_id_list) == 0:
        return -1
    else:
        return language_id_list[0]

def CreateIndexing(sentence, line_id, dictionary):
    word_list = sentence.split()
    # number of parts formed for each tagged word in the corpus(word/pos)
    tagged_word_parts = 2   
    for word in word_list:
        # skip untagged words
        if(len(word.split('/')) != tagged_word_parts):
            continue
        subtag = (word.split('/')[1]).upper()
        # ignore -TL suffix in subtags since they are just to indicate that the word occurs in title
        subtag = subtag.split('-TL')[0]
        if(subtag in logic.english_pos_mapping):
            generalized_pos = logic.english_pos_mapping[subtag]
        else:
            generalized_pos = subtag        
        word = (word.split('/')[0] + "/" + generalized_pos).lower()
        dictionary[word].append(line_id)        
    return dictionary

def StoreIndexing(dictionary):
    file = open("indexing.txt", "w")
    file.write(dictionary)
    file.close()

def GetIndexing():
    dictionary = {}
    if(os.path.exists("indexing.txt")):
        file = open("indexing.txt", "r")
        dictionary = json.loads(file.read())
    return dictionary
    
def isCorpusLoaded(corpus):
    query = f"select count(*) from {corpus}"
    count_list = SQLQuery(query)
    if(count_list[0] == 0):
        return False
    else:
        return True