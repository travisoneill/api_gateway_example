import os

#to add services insert key value pair of the name of the service and
#the port you want it to run on when running locally
SERVICES = {
    'default': 5000,
    'static': 8001
}

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
    project_id = os.environ.get('GAE_LONG_APP_ID')
    project_url = project_id + '.appspot.com'
    if service_name == 'default':
        return 'https://{project_url}'
    else:
        return 'https://{service_name}-dot-{project_url}'

def local_url(port):
    '''Generates url for a service when running locally'''
    return 'http://localhost:' + str(port)
