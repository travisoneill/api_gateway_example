import requests
import os
import argparse
from flask import Flask
import services_config

#setup arg parser to handle development flag
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--development', action='store_true')
args = parser.parse_args()
environment = 'development' if args.development else 'production'
app = Flask(__name__)
services_config.make_app(app, environment)
# app.config['SERVICE_MAP'] = services_config.map_services(environment)


@app.route('/')
def root():
    '''Gets index.html from the static file server'''
    res = requests.get(app.config['SERVICE_MAP']['static'])
    return res.content

@app.route('/hello/<service>')
def say_hello(service):
    '''Recieves requests from buttons on the front end and resopnds
    or sends request to the static file server'''
    #if 'gateway' is specified return immediate
    if service == 'gateway':
        return 'Gateway says hello'
    responses = []
    url = app.config['SERVICE_MAP'][service]
    res = requests.get(url + '/hello')
    responses.append(res.content)
    return '\n'.encode().join(responses)

@app.route('/<path>')
def static_file(path):
    '''Gets static files required by index.html to static file server'''
    url = app.config['SERVICE_MAP']['static']
    res = requests.get(url + '/' + path)
    return res.content, 200, {'Content-Type': res.headers['Content-Type']}

if __name__ == '__main__':
    port = os.environ.get('PORT') or 8000
    app.run(port=port)
