from wsgiref.simple_server import make_server

def web_app(environment, response):
 	status = '200 ok'
 	headers = [('Content-type', 'text/html; charset=utf-8')]
 	response(status, headers)

 	return[b'<strong>First WSGI</strong>']

with make_server('', 8000, web_app) as server:
 	print("Serving on port 8000...\nVisit http://127.0.0.1:8000\nTo kill the server enter 'control + C' ")

 	server.serve_forever()