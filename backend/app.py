import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../static')

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), '..', 'frontend')

@app.route('/')
def index():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/builder')
def builder():
    return send_from_directory(FRONTEND_DIR, 'builder.html')

@app.route('/view-form')
def view_form():
    return send_from_directory(FRONTEND_DIR, 'view-form.html')

if __name__ == '__main__':
    app.run(debug=True)
