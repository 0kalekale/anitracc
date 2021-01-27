#methods for route /manga/id and /anime/id

import anilistpy
from flask import render_template

def animeP(id):
    anime = anilistpy.Anime(id)
    title=anime.title("english")
    description=anime.description()
    img=anime.coverImage("large")
    eps=anime.episodes()
    id = anime.id
    #html = "Title: " + anime.title("english") + "<br><br>Description: " + anime.description() + "<br><img src=" + anime.coverImage("large") + ">"
    
    return render_template("page.html", img=img, title=title, description=description, eps=eps, id=id, media='ANIME', md="Episodes")
    #return "Title: " + anime.title("english") + "<br><br>Description: " + anime.description() + "<br><img src=" + anime.coverImage("large") + ">"

def mangaP(id):
    anime = anilistpy.Manga(id)
    title=anime.title("english")
    description=anime.description()
    img=anime.coverImage("large")
    eps=anime.chapters()
    id = anime.id
    #html = "Title: " + anime.title("english") + "<br><br>Description: " + anime.description() + "<br><img src=" + anime.coverImage("large") + ">"
    
    return render_template("page.html", img=img, title=title, description=description, eps=eps, id=id, media='MANGA', md="Chapters")
