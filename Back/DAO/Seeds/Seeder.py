import os
import json
import random
import requests
from operator import itemgetter

with open('nodes.json') as json_data:
    noeuds = json.load(json_data)

# for noeud in noeuds:
#     response = requests.post("http://localhost:5000/noeuds", data = json.dumps(noeud), headers = {'content-type': 'application/json'})
#     print(response)

with open('links.json') as json_data_links:
    liaisons = json.load(json_data_links)

# for liaison in liaisons:
#     response = requests.post("http://localhost:5000/liaisons", data = json.dumps(liaison), headers = {'content-type': 'application/json'})
#     print(response)

with open('linksId.json') as json_data_links:
    liaisons = json.load(json_data_links)

with open('nodesId.json') as json_data:
    noeuds = json.load(json_data)

# newNodes = []

# for noeud in noeuds :
#     tempLiaison = []
#     for liaison in liaisons:
#         if liaison["source"] == noeud["_id"] or liaison["destination"] == noeud["_id"]:
#             tempLiaison.append(liaison["_id"])
#     newNodes.append(noeud)
#     newNodes[-1]["liaisons"] = tempLiaison

# with open('FinalNodes.json', 'w') as fichier:
#     json.dump(newNodes, fichier)

with open('FinalNodes.json') as json_data:
    noeudsfinal = json.load(json_data)

for noeud in noeudsfinal:
    response = requests.put("http://localhost:5000/noeuds/"+noeud["_id"], data = json.dumps(noeud), headers = {'content-type': 'application/json'})
    print(response.text)
