import os
from flask import Flask, request, render_template, send_from_directory
import subprocess
from waitress import serve

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/sitemap.xml')
def sitemap_xml():
    return send_from_directory(app.static_folder, 'sitemap.xml')

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
