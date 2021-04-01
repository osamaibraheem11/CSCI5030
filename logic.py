# This file will hold useful functions
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from datetime import datetime
import logic
import itertools
import csv

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'Osamas-MacBook-Pro.local'
app.config['MYSQL_USER'] = 'Osama'
app.config['MYSQL_PASSWORD'] = 'CSCI5030SLU2021'
app.config['MYSQL_DATABASE_DB'] = 'wordsense'

mysql = MySQL(app)
conn = mysql.connect()
cursor = conn.cursor()

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

def wordcreator(word,partofspeech): # this function takes word selected and part of speech collected and returns string needed for sql statment
    thisdict = {
    "Noun":"NN",
    "Pronoun":"PN",
    "Adjective":"JJ",
    "Adverb":"RB",
    "Preposition":"IN",
    "Conjunction":"CC",
    "Article":"AT",
    "Interjection":"UH",
                }
    if partofspeech in thisdict.keys():
        word = f"{word}/{thisdict[partofspeech]}"
        return word
    else:
        print("Not Found")

def SQL_log(statment,status,purpose):
    now = datetime.now()
    row = [statment, now.strftime("%d/%m/%Y, %H:%M:%S"),status,purpose]
    with open('SQL-Scripts/sql_log.csv', 'a') as csvfile:  
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows([row])
        