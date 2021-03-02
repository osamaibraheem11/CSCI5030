from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from datetime import datetime
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
    data = cursor.fetchall() # This is a list of two tuples, the two tuples are the languages from the database 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)