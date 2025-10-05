from flask import Flask , render_template
#  Import the flask:
#  how to imtregate the html file:
#  Flask:
''' it create the instance of the Flask class,
Which will be your WSGI(web server Gateway Interface) apllication'''

#  WSGI application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html><h1> Welcome to Html Flask wed</h1></html>"

@app.route("/index")
def index():
    return render_template("index.html") # we can use go inside the templete folder and find index.html and use it

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)