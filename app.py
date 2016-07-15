#This file sets up the Flask application and uses the fresh_tomatoes.html
#created from fresh_tomatoes.py output

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("fresh_tomatoes.html")   #Looks for this file in templates folder


#__name__ is the in-built variable that is equal to __main__ only
# if the file is directly run and not imported

if __name__=="__main__":
    app.run()
