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
        #print("anime_current....")
        
        # using built in html for now, will use render_template later
        
        ANIME_CURRENT_HTML = ''
        ANIME_CURRENT_TITLE_ROMAJI = ANIME_CURRENT_LIST_Object.title_list("romaji")
        ANIME_CURRENT_ID = ANIME_CURRENT_LIST_Object.id_list()
        for i in range(0, len(ANIME_CURRENT_TITLE_ROMAJI)):
            ANIME_CURRENT_HTML = ANIME_CURRENT_HTML + r"<a href='/anime/"+ str(ANIME_CURRENT_ID[i]) + r"'>" + ANIME_CURRENT_TITLE_ROMAJI[i] + ca + br
            
        _html = "<h2>CURRENTLY WATCHING:</h2><br>" + ANIME_CURRENT_HTML
        return _html
    except IndexError:
        return "nothing watching."
def _anime_planning(username):
    try:
        # html tags
        br = '<br>'
        x = '>'
        y = '<'
        ca = r'</a>'
        ANIME_PLANNING_LIST_Object = MediaList(username, "ANIME", "PLANNING")
        #print("anime_planning...")
        
        # using built in html for now, will use render_template later
        
        ANIME_PLANNING_HTML = ''
        ANIME_PLANNING_TITLE_ROMAJI = ANIME_PLANNING_LIST_Object.title_list("romaji")
        ANIME_PLANNING_ID = ANIME_PLANNING_LIST_Object.id_list()
        for i in range(0, len(ANIME_PLANNING_TITLE_ROMAJI)):
            ANIME_PLANNING_HTML = ANIME_PLANNING_HTML + r"<a href='/anime/"+ str(ANIME_PLANNING_ID[i]) + r"'>" + ANIME_PLANNING_TITLE_ROMAJI[i] + ca + br
            
        _html = "<h2>PLANNING:</h2><br>" + ANIME_PLANNING_HTML
        return _html
    except IndexError:
        return "nothing planning"
    
def display_userpage(username):
    br = r'<br>'
        
    '''

    ANIME_COMPLETED_LIST_Object = MediaList(username, "ANIME", "COMPLETED")
    ANIME_DROPPED_LIST_Object = MediaList(username, "ANIME", "DROPPED")
    '''
    try: 
        finalhtml = _anime_current(username) + br + _anime_planning(username)
        
        return finalhtml
    except TypeError:
        return "type error - 500."
