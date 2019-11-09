from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import sqlite3
import youtube_api
import wget
import parse_lang
from contextlib import contextmanager
import img_download
import sys
from os import path
app = Flask(__name__)

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    #find videoID from youtube
    session['SEARCH'] = request.form.get('search')
    search_response = youtube_api.search(query=session['SEARCH'])
    for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videoID = search_result['id']['videoId']
    #get .srt file
    if not path.exists("srt/"+videoID+".srt"):
        url = 'http://www.nitrxgen.net/youtube_cc/' + videoID + '.csv'
        wget.download(url, out="csv/"+videoID+".csv", bar=None)
        eng_index = parse_lang.parse_lang("csv/"+videoID + ".csv")
        url = 'http://www.nitrxgen.net/youtube_cc/' + videoID + '/' + eng_index + '.srt'
        filename = wget.download(url, out="srt/"+videoID+".srt", bar=None)
    ## TODO: Do something with the file
    # os.remove(filename)
    with suppress_stdout():
        img_download.downloadimages("hi")
    return render_template('index.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    # app.run(debug=True, host='192.168.0.22', port=443, ssl_context='adhoc')
    app.run(debug=True,host='0.0.0.0', port=80)
