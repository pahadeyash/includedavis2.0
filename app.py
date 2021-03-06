from flask import Flask, render_template, send_from_directory
import os

# create application
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')

if __name__ == '__main__':
	app.run()
