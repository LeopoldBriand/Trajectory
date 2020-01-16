from pycnic.core import Handler
from pycnic.errors import HTTP_400
import json
import requests
from . import intineraireAlgo 

class Search(Handler):

    def get(self):
        if (not self.request.data.get("source")) or (not self.request.data.get("destination")):
            raise HTTP_400("You need to provide a source node and a destination node")
        requestNoeuds = requests.get("http://localhost:5000/noeuds", headers = {'content-type': 'application/json'})
        requestLiaisons = requests.get("http://localhost:5000/liaisons", headers = {'content-type': 'application/json'})
        noeudsJson = requestNoeuds.json()
        liaisonsJson = requestLiaisons.json()
        noeuds = []
        liaisons = []
        for item in noeudsJson:
            noeuds.append(intineraireAlgo.Noeud(nom = item["name"], id = item["_id"], liaisons = item["liaisons"]))
        for item in liaisonsJson:
            liaisons.append(intineraireAlgo.Liaison(id = item["_id"], distance = item["distance"], noeud1 = item["source"], noeud2 = item["destination"]))
        Algo = intineraireAlgo.Main(noeuds, liaisons, self.request.data.get("source"), self.request.data.get("destination") )
        result = Algo.goToNewHorizon()
        resultat = []
        noms = []
        for node in result:
            resultat.append(node.id)
            noms.append(node.nom)
        return {
            "nodes": resultat,
            "noms": noms
        }
