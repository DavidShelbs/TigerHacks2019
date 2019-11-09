from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import sqlite3
import youtube_api
import wget
import parse_lang
from contextlib import contextmanager
import sys
import os
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
    session['SEARCH'] = request.form.get('search')
    search_response = youtube_api.search(query=session['SEARCH'])
    for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videoID = search_result['id']['videoId']
    print(videoID)
    url = 'http://www.nitrxgen.net/youtube_cc/' + videoID + '.csv'
    with suppress_stdout():
        filename = wget.download(url)
    eng_index = parse_lang.parse_lang(videoID + ".csv")
    os.remove(filename)
    url = 'http://www.nitrxgen.net/youtube_cc/' + videoID + '/' + eng_index + '.srt'
    with suppress_stdout():
        filename = wget.download(url)
    ## TODO: Do something with the file
    # os.remove(filename)
    return render_template('index.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    # app.run(debug=True, host='192.168.0.22', port=443, ssl_context='adhoc')
    app.run(debug=True,host='0.0.0.0', port=80)
