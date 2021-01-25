from anilistpy import Media
from flask import redirect
def update_progress(id, token, progress, media):
    a = Media.setprogress(id, token, progress)
    url = r'/'+media.lower()+r'/'+str(id)
    return redirect(url)
    
