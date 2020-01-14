from pycnic.core import WSGI
from Routes.search import Search

class app(WSGI):
    routes = [('/search', Search())]