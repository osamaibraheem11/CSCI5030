from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'Osamas-MacBook-Pro.local'
app.config['MYSQL_USER'] = 'Osama'
app.config['MYSQL_PASSWORD'] = 'CSCI5030SLU2021'
app.config['MYSQL_DATABASE_DB'] = 'TestDB'

mysql = MySQL(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/log')
def log():
    cursor.execute("SELECT * FROM TestTable WHERE id = 1;")
    conn.commit()
    data = cursor.fetchall()
    (key, word, sentance) = data[0]
    file1 = open("log.txt","w+")
    file1.write(sentance)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)