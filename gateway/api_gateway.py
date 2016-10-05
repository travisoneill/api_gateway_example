import requests
import sys
from flask import Flask
import services_config
app = Flask(__name__)

@app.route('/')
def root():
    '''Gets index.html from the static file server'''
    res = requests.get(app.config['SERVICE_MAP']['static'])
    return res.content

@app.route('/hello/<service>')
def say_hello(service):
    '''Recieves requests from the buttons on the front end and resopnds
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
    '''Handles static file requests from index.html'''
    url = app.config['SERVICE_MAP']['static']
    res = requests.get(url + '/' + path)
    return res.content, 200, {'Content-Type': res.headers['Content-Type']}


# if __name__  == "__main__":
#     if len(sys.argv) > 1 and sys.argv[1] == '--development':
#         app.config['SERVICE_MAP'] = services_config.map_services('development')
#         app.config['DEBUG'] = True
#         app.run(port=int(8000))
#     else:
#         app.config['SERVICE_MAP'] = services_config.map_services('production')
#         app.run()
