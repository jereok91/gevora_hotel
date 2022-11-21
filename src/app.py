from cgitb import html
from distutils.util import execute
from flask import Flask, render_template, g, request, redirect

import sqlite3

app=Flask(__name__,)

DATABASE = './src/database/HOTEL_GEVORA.s3db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def inicio(): 
    return render_template('auth/inicio.html')

@app.route('/sobrenosotros.html')
def sobrenosotros():
    return render_template('auth/sobrenosotros.html')

@app.route('/contact.html')
def contact():
    return render_template('auth/contact.html')

@app.route('/contact/guardar', methods=['POST'])
def contact_guardar():
    print("prueba")
    _nombre = request.form['nombre_form']
    _correo = request.form['correo_form']
    _mensaje = request.form['mensaje_form']
    #conet DB SQL lite
    strsql = "INSERT INTO contact(nombre, correo, mensaje) VALUES(?, ?, ?)"
    datos=(_nombre, _correo, _mensaje)
    con = get_db()
    cursorObj = con
    cursorObj.execute(strsql, datos)
    cursorObj.commit()
    cursorObj.close()
    return redirect('/contact.html')

@app.route('/login.html')
def login():
    return render_template('auth/login.html')

@app.route('/login/guardar', methods=['GET', 'POST'])
def login_guardar():
    if request.method == 'POST':
    #conet DB SQL lite
        strsql = "SELECT correo,password FROM registro where correo='"+name+"' and password = '"+password+"'" 
        con = get_db()
        cursorObj = con
        cursorObj.execute(strsql)
        cursorObj.commit()
        cursorObj.close()
        results = cursorObj.fetchall()
        name = request.form['name']
        password = request.form['password']
        if len(results) == 0:
            print("validar datos erroneos por favor")
        else:
            return render_template(login.html)

@app.route('/index.html')
def index():
    return render_template('auth/index.html')

@app.route('/registro.html')
def registro():
    return render_template('auth/registro.html')

@app.route('/registro/guardar', methods=['POST'])
def registro_guardar():
    print("prueba")
    _nombre = request.form['nombre_form']
    _correo = request.form['correo_form']
    _password = request.form['password_form']
    #conet DB SQL lite
    strsql = "INSERT INTO registro(nombre, correo, password) VALUES(?, ?, ?)"
    datos=(_nombre, _correo, _password)
    con = get_db()
    cursorObj = con
    cursorObj.execute(strsql, datos)
    cursorObj.commit()
    cursorObj.close()
    return redirect('/registro.html')

if __name__=='__main__':
    app.run(port=5000)