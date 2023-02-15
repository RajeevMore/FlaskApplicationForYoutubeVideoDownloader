import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from pytube import YouTube
from flask import Flask

UPLOAD_FOLDER = 'static/downloaded_folder/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
@app.route('/download', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'link' in request.form :
        youtube_link = request.form['link']
        video = YouTube(youtube_link)
        stream = video.streams.get_highest_resolution()
        stream.download(UPLOAD_FOLDER)
        msg = f'Video downloaded and stored at {UPLOAD_FOLDER}'
    return render_template('downloader.html', msg = msg)


if __name__ == "__main__" :
     app.run(debug=True)