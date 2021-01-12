# IMPORTS
import anilistpy
from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/<medium>/<id>', methods=['GET', 'POST'])
def page(medium, id):
    if medium == "anime":
        return "Title: " + anilistpy.Anime(id).title("english") + "<br><br>Description: " + anilistpy.Anime(id).description() + "<br><img src=" + anilistpy.Anime(id).coverImage("large") + ">"
    elif medium == "manga": 
        return "Title: " + anilistpy.Manga(id).title("english") + "<br><br>Description: " + anilistpy.Manga(id).description() + "<br><img src=" + anilistpy.Manga(id).coverImage("large") + ">"

@app.route('/search/<medium>/<sQ>')
def search(medium, sQ):
    if medium == "anime":
        rt = animeS(sQ)
    elif medium == "manga":
        rt = mangaS(sQ)
    return rt
def animeS(sQ):
    Sobj = anilistpy.animeSearch(sQ)
    return "<a href=\"/anime/" + str(Sobj.id(0))+ "\">" + Sobj.title(0)+ "</a>"
def mangaS(sQ):
    Mobj = anilistpy.mangaSearch(sQ)
    return "<a href=\"/manga/" + str(Mobj.id(0))+ "\">" + Mobj.title(0)+ "</a>"
if __name__ == "__main__":
    app.run()