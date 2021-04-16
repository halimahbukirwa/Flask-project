from flask import Flask
app = Flask(__name__)

@app.route('/')
def movie():
    choice = {{'Title':'The Old Guard','Minutes':126,'Genre':'Adventure'},
               {'Title':'Blended','Minutes':118,'Genre':'Romantic Comedy'},
               {'Title':'Sonic The Hedgehog','Minutes':100,'Genre':'Animation'}}
    return choice
