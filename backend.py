from flask import Flask, render_template, request, redirect
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

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/log')
def log():
    cursor.execute("SELECT Lang_Desc FROM Lang_Ref;")
    conn.commit()
    language_list = logic.tuple2list(cursor.fetchall()) # Uses function from logic file to convert tuple to list 
    return render_template('index.html', language_list = language_list)

if __name__ == '__main__':
    app.run(debug = True)