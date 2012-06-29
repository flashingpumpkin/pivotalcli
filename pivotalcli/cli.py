"""
Pivotal Tracker Command Line Client

Usage:
	pivotalcli add <name> [--type=<type>, --labels=<labels>, --project=<project> --token=<token>]

"""
from pivotalcli import __version__
from docopt import docopt
from pivotalcli.helpers import *
import json
import os
import requests
import urllib
import sys

arguments = docopt(__doc__, version = " ".join(["Pivotal CLI", __version__]))

def main():

    if arguments['add']:
        data = {
            'story[name]': arguments['<name>'],
            'story[labels]': arguments.get('--labels') or '',
            'story[type]': arguments.get('--type') or 'feature',
            }

        url = 'https://www.pivotaltracker.com/services/v3/projects/%s/stories?%s' % (
            arguments.get('--project') or get_project(),
            urllib.urlencode(data))

        resp = requests.post(url, headers = {'X-TrackerToken': arguments.get('--token') or get_token()})

        if resp.status_code == 200:
            print resp.content
        else:
            print resp.content
            sys.exit(1)
