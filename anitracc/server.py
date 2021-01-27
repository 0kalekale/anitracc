#GLOBAL IMPORTS
import anilistpy
from flask import Flask, session, redirect, url_for, request, render_template

#LOCAL IMPORTS
from search import animeS,mangaS
from page import animeP,mangaP
from user import display_userpage
from mutation import update_progress, update_status_
from config import writetoken, readtoken
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/<medium>/<id>', methods=['GET', 'POST'])
def page(medium, id):
    if medium == "anime":
        return animeP(id)
    elif medium == "manga": 
        return mangaP(id)

@app.route('/search/<medium>/<sQ>')
def search(medium, sQ):
    if medium == "anime":
        rt = animeS(sQ)
    elif medium == "manga":
        rt = mangaS(sQ)
    return rt

@app.route('/search', methods=['GET', 'POST'])
def searchPAGE():
    return render_template("search.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
    _opt = request.form.get("mat")
    _sq = request.form.get("sq")
    rd = r'/search/' + _opt + r'/' + _sq
    return redirect(rd)

@app.route('/user/<username>/')
def userpage(username):
    # rt = 'user: ' + username
    return display_userpage(username)

@app.route('/mutation/progress', methods=['GET', 'POST'])
def mutation():
    media = request.args.get('media', default = '', type = str)
    id = request.args.get('id', default = '', type = int)
    progress = request.form.get("progress")
    token = readtoken()
    return update_progress(id, token, progress, media)

@app.route('/mutation/status', methods=['GET', 'POST'])
def mutationstatus():
    media = request.args.get('media', default = '', type = str)
    id = request.args.get('id', default = '', type = int)
    status = request.form.get("status")
    token = readtoken()
    return update_status_(id, token, status, media)

@app.route('/login')
def login():
    
    return render_template("login.html")

@app.route('/login/write', methods=['GET', 'POST'])
def write():
    print("write")
    token = request.form.get("password")
    return writetoken(token)

    
if __name__ == "__main__":
    app.run()

