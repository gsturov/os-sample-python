from flask import Flask
from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from werkzeug.serving import run_simple
application = Flask(__name__)

from prometheus_client import Counter
c = Counter('__test_counter', 'Description of counter')
c.inc()

print('____ adding metric _____')

@application.route("/")
def hello():
    c.inc()
    return "Hello World 2!"

print('____ adding metrics handler _____')
app_dispatch = DispatcherMiddleware(application, {
    '/metrics': make_wsgi_app()
})
run_simple(hostname="localhost", port=8090, application=app_dispatch)