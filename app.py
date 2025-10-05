#  Flask:

from flask import Flask
''' it create the instance of the Flask class,
Which will be your WSGI(web server Gateway Interface) apllication'''

#  WSGI application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to this Flask Course. This should be an good course ?"

@app.route("/index")
def index():
    return "Welcome to the index page"

if __name__=="__main__":
    app.run(debug=True)