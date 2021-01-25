# methods for route /search/manga/id and /search/anime/id
import anilistpy
from flask import render_template

def animeS(sQ):
    Sobj = anilistpy.animeSearch(sQ)
    url, title, desc, img = [], [], [], []
    try: 
        for i in range(0, 5):
            _anime = anilistpy.Anime(Sobj.id(i))
            id = r"/anime/"+str(Sobj.id(i))
            url.append(id)
            title.append(_anime.title("romaji"))
            desc.append(_anime.description())
            img.append(_anime.coverImage('medium')) 
    except IndexError:
        pass
    
    return render_template("result.html", title=title, desc=desc, sq=sQ, url= url, img=img)

def mangaS(sQ):
    Mobj = anilistpy.mangaSearch(sQ)

    url, title, desc, img = [], [], [], []
    try: 
        for i in range(0, 5):
            _anime = anilistpy.Manga(Mobj.id(i))
            id = r"/manga/"+str(Mobj.id(i))
            url.append(id)
            title.append(_anime.title("romaji"))
            desc.append(_anime.description())
            img.append(_anime.coverImage('medium')) 
    except IndexError:
        pass
    
    return render_template("result.html", title=title, desc=desc, sq=sQ, url= url, img=img)
