# This package allows servers, requests, urls, etc.
from flask import Flask, request, render_template, redirect, url_for
# Create app var from Flask package
app = Flask(__name__)

# This packages allows for saving files to app dir
import os
import pandas as pd
# Set path to upload csv (path of current app dirnae)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Create get route, function to run on request
@app.route('/')
def home_route():
    return render_template('upload.html')

# Create post route, function to run on request
@app.route('/results', methods=['POST', 'GET'])
def send_csv():
    if request.method == 'POST':
        if request.files['file'].filename == '' or request.files['file'].filename.endswith('.xlsx') == False:
            return redirect(url_for("home_route"))
        else:
            target = os.path.join(APP_ROOT, 'static/uploads')
            file = request.files['file']
            input_one = request.form['input_one']
            input_two = request.form['input_two']
            filename = file.filename
            destination = "/".join([target, filename])
            file.save(destination)

            # os.remove(destination)
            # csvfinal.to_csv(target + '/UPCstoUploadtoAdmin.csv')

            return render_template('results.html')
    else:
            return redirect(url_for("home_route"))

# This runs the server (provided by Flask)
if __name__ == '__main__':
    app.run(debug=True)
