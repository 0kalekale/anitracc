from anilistpy import MediaList
from flask import render_template
def _anime_current(username):
    try:
        # html tags
        br = '<br>'
        x = '>'
        y = '<'
        ca = r'</a>'
        ANIME_CURRENT_LIST_Object = MediaList(username, "ANIME", "CURRENT")

        
        # using built in html for now, will use render_template later
        
        ANIME_CURRENT_HTML = ''
        ANIME_CURRENT_TITLE_ROMAJI = ANIME_CURRENT_LIST_Object.title_list("romaji")
        ANIME_CURRENT_ID = ANIME_CURRENT_LIST_Object.id_list()
        for i in range(0, len(ANIME_CURRENT_TITLE_ROMAJI)):
            ANIME_CURRENT_HTML = ANIME_CURRENT_HTML + r"<a href='/anime/"+ str(ANIME_CURRENT_ID[i]) + r"'>" + ANIME_CURRENT_TITLE_ROMAJI[i] + ca + br
            
        _html = "<h1>CURRENTLY WATCHING:</h1><br>" + ANIME_CURRENT_HTML
        return _html
    
    except IndexError:
        pass   
    
def display_userpage(username):
    
    '''
    
    ANIME_PLANNING_LIST_Object = MediaList(username, "ANIME", "PLANNING")
    ANIME_COMPLETED_LIST_Object = MediaList(username, "ANIME", "COMPLETED")
    ANIME_DROPPED_LIST_Object = MediaList(username, "ANIME", "DROPPED")
    '''
    finalhtml = _anime_current(username)
    
    return finalhtml
