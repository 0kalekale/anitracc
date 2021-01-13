# methods for route /search/manga/id and /search/anime/id
import anilistpy

def animeS(sQ):
    Sobj = anilistpy.animeSearch(sQ)
    return "<a href=\"/anime/" + str(Sobj.id(0))+ "\">" + Sobj.title(0)+ "</a>"
def mangaS(sQ):
    Mobj = anilistpy.mangaSearch(sQ)
    return "<a href=\"/manga/" + str(Mobj.id(0))+ "\">" + Mobj.title(0)+ "</a>"