#! /usr/bin/python3
import sys
import requests
import urllib3
from pprint import pprint
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from requests.auth import HTTPBasicAuth

template_id = sys.argv[1]

res = requests.post('https://192.168.0.83/api/v2/job_templates/'+template_id+'/launch/', verify=False, auth=HTTPBasicAuth('admin','password123'))
pprint(res.json())

