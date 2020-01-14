from pycnic.core import WSGI
import Routes.search.py

class app(WSGI):
    routes = [('/search', Search())]