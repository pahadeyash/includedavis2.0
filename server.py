from flask import Flask
from flask import render_template

@app.route('/')
def root():
	return render_template('index.html')

app = Flask(__name__)

