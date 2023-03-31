import os
import users
from flask import Flask, render_template, request, redirect, url_for, make_response
import cookie
import datetime
import hashlib

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get_user(username)
        #array[username,password]
        if user and user[2] == password:
            ip_address = request.remote_addr
            session_id = hashlib.md5(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}-{user[0]}'.encode()).hexdigest()
            cookie.update(ip_address, session_id, user)
          # Rediriger vers la page d'accueil avec un cookie contenant l'identifiant de session
            return redirect(url_for('home', username=username, session_id=session_id))
        else:
            error = 'Nom d\'utilisateur ou mot de passe incorrect'
            return render_template('signin.html', error=error)
    else:
        return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = users.insert_user(username, password)
        return render_template('signin.html', error=error)
    else:
        return render_template('signup.html')

@app.route('/home/<session_id>')
def home(session_id):
    username = request.args.get('username')
    return f'Bienvenue {username}!'

if __name__ == '__main__':
    app.run(debug=True)
