import os
import argparse
from flask import Flask

#setup arg parser to handle development flag
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--development', action='store_true')

app = Flask(__name__)

@app.route('/hello')
def say_hello():
    '''responds to request from frontend via gateway'''
    return 'Static File Server says hello!'

@app.route('/')
def root():
    '''serves index.html'''
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_file(path):
    '''serves static files required by index.html'''
    mimetype = ''
    if path.split('.')[1] == 'css':
        mimetype = 'text/css'
    if path.split('.')[1] == 'js':
        mimetype = 'application/javascript'
    return app.send_static_file(path), 200, {'Content-Type': mimetype}

if __name__  == "__main__":
    args = parser.parse_args()
    port = 8001 if args.development else os.environ.get('PORT')
    app.run(port=port)
