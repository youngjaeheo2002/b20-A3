# required imports; you may add more in the future; currently, we will only use render_template 
from flask import Flask, render_template 

def containsNumbers(s):
    for character in s:
        if character.isdigit():
            return True

    return False


def allStripped(s):
    valid_symbols = "!@#$%^&*()_-+={}[]"

    result = ""
    for character in s:
        if character.isalpha() or character in valid_symbols:
            result+=character

    return result


def user(s):
    #if s contains numbers
    if containsNumbers(s) or s[0].isspace():
        return allStripped(s)
    elif not s.isupper() and not s.islower():
        return s.capitalize()
    elif s.isupper():
        return s.lower()
    elif s.islower():
        return s.upper()
    
# tells Flask that "this" is the current running app 
app = Flask(__name__) 
 
# setup the default route 
# this is the page the site will load by default (i.e. like the home page) 

@app.route('/')
def root():
    return "<p>Hello!</p>"
@app.route('/<name>') 
def root1q(name): 
    # tells Flask to render the HTML page called index.html 
    return "<p> Hello! " +user(name) + "</p>" 
 
# run the app when app.py is run 
if __name__ == '__main__': 
    app.run(debug=True)