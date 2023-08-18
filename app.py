from flask import Flask

from flask import request

 
print(1)
app = Flask(__name__)

 

@app.route('/')

def hello():

 

    return '<h1>Hello, World - feature 2</h1>'
