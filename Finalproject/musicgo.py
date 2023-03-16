from flask import Flask 
from flask import Flask, flash, redirect, render_template, request, url_for, session, abort
import os

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index1():
        return render_template('main2.html')


@app.route('/home', methods = ['GET', 'POST'])
def main():
        return render_template('main2.html')


@app.route('/library' , methods = ['GET','POST'])
def create():
    return render_template("library.html") 

@app.route('/about', methods = ['GET', 'POST'])
def about():
    return render_template("about.html")
    
@app.route('/loginform')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def log_admin():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'login':
            session['logged_in'] = True
    else:
        print('wrong password!')
    return home()

@app.route("/signout", methods = ['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session['logged_in'] = False
    return index1()

        
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='localhost', port=3568)