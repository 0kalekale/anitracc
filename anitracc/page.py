#methods for route /manga/id and /anime/id

import anilistpy

def animeP(id):
    return "Title: " + anilistpy.Anime(id).title("english") + "<br><br>Description: " + anilistpy.Anime(id).description() + "<br><img src=" + anilistpy.Anime(id).coverImage("large") + ">"

def mangaP(id):
    return "Title: " + anilistpy.Manga(id).title("english") + "<br><br>Description: " + anilistpy.Manga(id).description() + "<br><img src=" + anilistpy.Manga(id).coverImage("large") + ">"
