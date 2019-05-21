from wsgiref.simple_server import make_server


class WebApp:

	def __init__(self, environment, response):
		self.environment = environment
		self.response = response

	def __iter__(self):
		status = '200 OK'
		response_headers = [('Content-type', 'text/html')]
		self.response(status, response_headers)

		yield b"<strong>First class based WSGI</strong>"


with make_server('', 8000, WebApp) as server:
	print("Serving on port 8000... \nVisit http://127.0.0.1:8000\nTo kill the server enter 'control + C'")

	server.serve_forever()