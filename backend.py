from flask import Flask, render_template, request, redirect, jsonify
from flaskext.mysql import MySQL
from datetime import datetime
import logic
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'Osamas-MacBook-Pro.local'
app.config['MYSQL_USER'] = 'Osama'
app.config['MYSQL_PASSWORD'] = 'CSCI5030SLU2021'
app.config['MYSQL_DATABASE_DB'] = 'wordsense'

mysql = MySQL(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route('/', methods =["GET", "POST"])
def hello():
    if request.method == "GET":
        sentence_List = ""
        error = ""
    if request.method == "POST":
        language_selected = request.form.get('language')
        Lang_ID = logic.SQLQuery(f"SELECT Lang_ID FROM Lang_Ref WHERE Lang_Desc = '{language_selected}';")
        part_of_speech_selected = request.form.get('partOfSpeech')
        part_of_speech_ID = logic.SQLQuery(f"SELECT Part_ID FROM Speech_Parts WHERE Lang_ID = '{Lang_ID[0]}' AND Part_Desc = '{part_of_speech_selected}';")
        word_selected = logic.wordcreator(request.form.get('word'),request.form.get('partOfSpeech'))
        sentence_List = logic.SQLQuery(f"select Line_Text from {language_selected}_corpus where Line_Text like  '% {word_selected} %';")
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