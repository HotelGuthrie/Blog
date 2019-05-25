import sys
sys.path.insert(0, './helloworld')
from wsgi import WSGI


app = wsgi.application
