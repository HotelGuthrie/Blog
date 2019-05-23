import sys
sys.path.insert(0, './hello')
from helloworld import wsgi


app = wsgi.application
