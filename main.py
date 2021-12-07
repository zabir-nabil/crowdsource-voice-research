#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://dev.to/thetrebelcc/how-to-run-a-flask-app-over-https-using-waitress-and-nginx-2020-235c

from flask import Flask, redirect, url_for
from flask import request
from flask import render_template
from waitress import serve
import os, string
import time

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        print(request)
        try:
            name = request.form.get('name')
            if name == None:
                return "Kindly, fill up your full name in English."
            name = name.translate(str.maketrans('', '', string.punctuation))
            name = name.replace(" ", "-")
            if len(name) < 3:
                return "Invalid full name."
        except:
            return "Invalid full name. Kindly, fill up the details."
            
        bdate = request.form.get('bdate')
        gender = request.form.get('gender')
        f = request.files['audio_data']

        timestamp = int(time.time())

        audio_file_name = os.path.join("audio_db", name + "_" + bdate + "_" + gender + "_" + str(timestamp) + ".wav")
        with open(audio_file_name, 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')

        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")



if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000, url_scheme='https')