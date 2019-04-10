import os
from flask import Flask, request, send_from_directory, redirect
import requests

#import json
#import itertools
#import flask
from pytube import YouTube

app = Flask(__name__)


# Stampa l'environment in cui parte il server
print(os.environ['FLASK_ENV'])


@app.route('/')
@app.route('/home')
def hello():
    url = request.args.get('url')
    silentSpeed = request.args.get('silent')
    soundSpeed = request.args.get('sound')
    YouTube(url).streams.first().download("public", filename="download")

    converFile(silentSpeed, soundSpeed)
    return redirect("http://localhost:5000/public/converted.mp4", code=302)


@app.route('/public/<path:path>')
def send_js(path):
    return send_from_directory('public', path)


def converFile(silentSpeed, soundSpeed):
    os.system("gnome-terminal -e 'python ./jumpcutter.py --input_file public/download.mp4 --output_file public/converted.mp4 --sounded_speed "+soundSpeed+" --silent_speed "+soundSpeed+" --frame_margin 23 --frame_rate 25'")


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
