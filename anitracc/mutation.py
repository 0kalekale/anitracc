from anilistpy import Media
from flask import redirect
def update_progress(id, token, progress, media):
    try:
        a = Media.setprogress(id, token, progress)
        url = r'/'+media.lower()+r'/'+str(id)
        return redirect(url)
    except:
        return redirect('/login')
def update_status_(id, token, status, media):
    try:
        a = Media.setstatus(id, token, status)
        url = r'/'+media.lower()+r'/'+str(id)
        return redirect(url)
    except: 
        return redirect('/login')
