# This file will hold useful functions
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from datetime import datetime
import logic
import itertools

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


        "There/ex can/md be/be no/at doubt/nn ,/, the/at Boston/np of/in that/dt era/nn could/md be/be exquisitely/ql cruel/jj in/in enforcing/vbg its/pp$ canons/nns of/in behavior/nn ./.The/at gentle/jj Channing/np ,/, revered/vbn by/in all/abn Bostonians/nps ,/, orthodox/jj or/cc Unitarian/jj ,/, wrote/vbd to/in a/at friend/nn in/in Louisville/np that/cs among/in its/pp$ many/ap virtues/nns Boston/np did/dod not/* abound/vb in/in a/at tolerant/jj spirit/nn ,/, that/cs the/at yoke/nn of/in opinion/nn crushed/vbd individuality/nn of/in judgment/nn and/cc action/nn :/: ``/`` No/at city/nn in/in the/at world/nn is/bez governed/vbn so/ql little/rb by/in a/at police/nn ,/, and/cc so/ql much/rb by/in mutual/jj inspections/nns and/cc what/wdt is/bez called/vbn public/jj sentiment/nn ./.We/ppss stand/vb more/rbr in/in awe/nn of/in one/cd another/dt than/cs most/ap people/nns ./.Opinion/nn is/bez less/ql individual/jj or/cc runs/vbz more/rbr into/in masses/nns ,/, and/cc often/rb rules/vbz with/in a/at rod/nn of/in iron/nn ''/'' ./.Even/ql more/ql poignantly/rb ,/, and/cc with/in the/at insight/nn of/in a/at genius/nn ,/, Channing/np added/vbd --/-- remember/vb ,/, this/dt is/bez Channing/np ,/, not/* Parker/np !/."