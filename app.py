from flask import Flask,render_template,request
import os
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/super-resolution')
def SR():
    return render_template('super-resolution.html')
@app.route('/deblurring')
def deblurr():
    return render_template('deblurr.html')
@app.route('/colorization')
def colorize():
    return render_template('colorize.html')
@app.route('/upload',methods = ['GET','POST'])
def upload():
    if request.method == "POST":
        f = request.files['image']
        f.save(secure_filename(f.filename))
    return render_template("super-resolution.html")
app.run(debug=True)