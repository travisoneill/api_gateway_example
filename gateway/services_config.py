import os
from flask import Flask

#setup arg parser to handle development flag
# parser = argparse.ArgumentParser()
# parser.add_argument('-d', '--development', action='store_true')
# args = parser.parse_args()
# environment = 'development' if args.development else 'production'

#to add services insert key value pair of the name of the service and
#the port you want it to run on when running locally
SERVICES = {
    'default': 8000,
    'static': 8001
}

def make_app(environment, name):
    flask_app = Flask(__name__)
    flask_app.config['SERVICE_MAP'] = map_services(environment)
    return flask_app

def map_services(environment):
    '''Generates a map of services to correct urls for running locally
    or when deployed'''
    url_map = {}
    for service, local_port in SERVICES.items():
        if environment == 'production':
            url_map[service] = production_url(service)
        if environment == 'development':
            url_map[service] = local_url(local_port)
    return url_map

def production_url(service_name):
    '''Generates url for a service when deployed to App Engine'''
    project_id = os.environ.get('GAE_LONG_APP_ID') or 'flask-algo'
    project_url = '{}.appspot.com'.format(project_id)
    if service_name == 'default':
        return 'https://{}'.format(project_url)
    else:
        return 'https://{}-dot-{}'.format(service_name, project_url)

def local_url(port):
    '''Generates url for a service when running locally'''
    return 'http://localhost:{}'.format(str(port))
