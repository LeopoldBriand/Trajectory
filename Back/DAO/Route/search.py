from pycnic.core import Handler
from pycnic.errors import HTTP_400

class Search(Handler):

    def get(self):
        if (not self.request.data.get("source")) or (not self.request.data.get("destination")):
            raise HTTP_400("You need to provide a source node and a destination node")

        return {
            "nodes": ["A", "B"]
        }
