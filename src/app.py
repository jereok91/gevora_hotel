from cgitb import html
from flask import Flask, render_template, g
from config import config
import sqlite3

DATABASE = './database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


app=Flask(__name__)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def inicio():
    cur = get_db().cursor()
    print(cur)    
    return render_template('auth/inicio.html')

@app.route('/sobrenosotros.html')
def sobrenosotros():
    return render_template('auth/sobrenosotros.html')

@app.route('/contact.html')
def contact():
    return render_template('auth/contact.html')

@app.route('/login.html')
def login():
    return render_template('auth/login.html')

@app.route('/index.html')
def index():
    return render_template('auth/index.html')

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run(port=5000)