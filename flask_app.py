import os
from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('flask_app/index.html')

if __name__ == "__main__":
    app.run(debug=True)