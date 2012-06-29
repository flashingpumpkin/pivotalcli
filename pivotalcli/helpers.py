import os, json

CONFIG = None

def parse_config(filename):
    global CONFIG
    if CONFIG is None:
        CONFIG = json.load(open(filename))
    return CONFIG

def get_config():
    folder = os.getcwd()
    while folder != '/':
        if '.pivotal.json' in os.listdir(folder):
            return parse_config(os.path.join(folder, '.pivotal.json'))
        folder = os.path.split(folder)[0]
    raise Exception('No .pivotalcli file found')

def get_token():
    return os.environ.get('PIVOTAL_TOKEN', get_config().get('TOKEN'))

def get_project():
    return os.environ.get('PIVOTAL_PROJECT', get_config().get('PROJECT'))
