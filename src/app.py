from cgitb import html
from flask import Flask, render_template
from config import config
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Rapsoda25'
app.config['MYSQL_DB'] = 'hotel_gevora'


conexion = MySQL()

@app.route('/')
def index():
    return render_template('auth/index.html')

@app.route('/sobrenosotros')
def sobrenosotros():
    return render_template('auth/sobrenosotros.html')

@app.route('/contacto')
def contacto():
    return render_template('auth/contact.html')

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run(port=5000)