from flask import Flask, render_template, request, redirect, jsonify
from flaskext.mysql import MySQL
from datetime import datetime
import logic
import json
from collections import defaultdict
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

def GetIndexing():
    f = open("indexing.txt", "r")
    dictionary = json.loads(f.read())
    return dictionary

@app.route('/', methods =["GET", "POST"])
def homepage():
    # Get the indexing in memory so that we have it until the application is closed
    dictionary = GetIndexing()

    if request.method == "GET":
        sentence_List = ""
        error = ""
    if request.method == "POST":
        language_selected = request.form.get('language')
        Lang_ID = logic.SQLQuery(f"SELECT Lang_ID FROM Lang_Ref WHERE Lang_Desc = '{language_selected}';")
        part_of_speech_selected = request.form.get('partOfSpeech')
        word_selected = (request.form.get('word') + '/' + request.form.get('partOfSpeech')).lower()

        line_ids = dictionary[word_selected]
        # ignore first and last characters i.e. '[' and ']' to get the list of line ids as a string like "1,3,6,7,...""
        line_ids_str = str(line_ids)[1:][:-1]
        sentence_List = logic.SQLQuery(f"select Line_Text from {language_selected}_corpus where Line_id in ({line_ids_str})")
        error = ""
        if len(sentence_List) == 0:
            error = "Error: Word not in corpus"

    language_list = logic.SQLQuery("SELECT Lang_Desc FROM Lang_Ref;")
    part_of_speech_list = logic.SQLQuery("SELECT Part_Desc FROM Speech_Parts WHERE Lang_ID = 1;")
    return render_template('index.html', language_list = language_list, part_of_speech_list=part_of_speech_list, sentence_List=sentence_List, error=error)

@app.route('/Query', methods =["GET", "POST"])
def Query():
    language_list = logic.SQLQuery("SELECT Lang_Desc FROM Lang_Ref;")
    language_selected = request.form.get('language')
    Lang_ID = logic.SQLQuery(f"SELECT Lang_ID FROM Lang_Ref WHERE Lang_Desc = '{language_selected}';")
    part_of_speech_list = logic.SQLQuery(f"SELECT Part_Desc FROM Speech_Parts WHERE Lang_ID = '{Lang_ID[0]}';")
    return render_template('partofspeech.html', part_of_speech_list=part_of_speech_list )

if __name__ == '__main__':
    app.run(debug = True)