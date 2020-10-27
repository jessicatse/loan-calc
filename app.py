#Azure uses app.py and looks for it to do whatever it tells it to do
# All our code will be in here

from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/") #/ means root, .route is function, when the git request shows up to the server and it's blank, it wants whatever is in root
# function returns the index.html
# if url asking for specific resource, then ask it to do specific things
def index():
    return render_template('index.html') #returning page, execute html

#flask is a python file executing python functions
# @ is the decorator
# when the 
@app.route('/mike')
def mike():
    return render_template('mike.html')

if __name__ == '__main__':
    app.run(debug=True)

