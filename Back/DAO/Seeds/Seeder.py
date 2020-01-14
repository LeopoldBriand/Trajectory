import os
import json
import random
import requests
from operator import itemgetter

with open('nodes.json') as json_data:
    noeuds = json.load(json_data)

nodesFinal = []

for noeud in noeuds:
    response = requests.post("http://localhost:5000/noeuds", data = json.dumps(noeud), headers = {'content-type': 'application/json'})
    print(response)

