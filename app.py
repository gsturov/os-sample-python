from prometheus_client import make_wsgi_app
from wsgiref.simple_server import make_server

print('____ adding metric _____')
from prometheus_client import Counter
c = Counter('__test_counter', 'Description of counter')
c.inc(500)

app = make_wsgi_app()
httpd = make_server('', 8080, app)
httpd.serve_forever()
