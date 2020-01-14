from pycnic.core import Handler
from pycnic.errors import HTTP_400
import json
import requests

class Search(Handler):

    def get(self):
        if (not self.request.data.get("source")) or (not self.request.data.get("destination")):
            raise HTTP_400("You need to provide a source node and a destination node")
        noeuds = requests.get("http://localhost:5000/noeuds", headers = {'content-type': 'application/json'})
        liaisons = requests.get("http://localhost:5000/liaisons", headers = {'content-type': 'application/json'})
        print(noeuds)
        print(liaison)
        result = [test]
        return {
            "nodes": json.dumps(result)
        }
