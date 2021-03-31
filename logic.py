# This file will hold useful functions
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from datetime import datetime
import logic
import itertools

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