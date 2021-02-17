from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)

# setting up SQL user access point 
app.config['MYSQL_DATABASE_USER'] = 'epiz_27941659'
app.config['MYSQL_DATABASE_PASSWORD'] = 'WDVb5wfcjg45m'
app.config['MYSQL_DATABASE_DB'] = 'epiz_27941659_Test'
app.config['MYSQL_DATABASE_HOST'] = 'sql106.epizy.com'

# creating an access point
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/button', methods=["GET", "POST"])
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)