from os import path
import json
from flask import redirect
def checkconfig():
    configpath = 'instance/config.json'  
    if path.exists(configpath):
        print("all set")
        return True
    else:
        print("no instance found, run `make setup`")
        return False
        
def writetoken(token):
    if checkconfig():
        config = open('instance/config.json', 'w+')
        json = '{\"token\": \"' + token +'\"}'
        config.write(json)
        config.close
        
    return redirect('/')
def readtoken():
    config = open('instance/config.json', 'r')
    tkn = json.loads(config.read())['token']    
    return tkn

'''
writetoken(">implying read")
readtoken()
'''
