from flask import Flask, render_template, url_for
import os

# create application
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

app.add_url_rule('/favicon.ico',
                 redirect_to=url_for('static', filename='favicon.ico'))

if __name__ == '__main__':
	app.run()
