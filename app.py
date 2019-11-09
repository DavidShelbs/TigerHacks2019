from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import sqlite3
import youtube_api

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    session['SEARCH'] = request.form.get('search')
    search_response = youtube_api.search(query=session['SEARCH'])
    videoId = []
    for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videoId.append(search_result['id']['videoId'])
    for id in videoId:
        print(id)
    return render_template('index.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    # app.run(debug=True, host='192.168.0.22', port=443, ssl_context='adhoc')
    app.run(debug=True,host='0.0.0.0', port=443, ssl_context='adhoc')
