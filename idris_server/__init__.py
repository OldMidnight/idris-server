from flask import Flask, request, jsonify
import logging, os
from http.client import HTTPConnection
from logging.config import dictConfig
from flask.logging import default_handler
from idris_server.endpoints import location, status

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# flask application factory
def create_app():
  '''Switches on logging of the requests module.'''
  HTTPConnection.debuglevel = 1

  requests_log = logging.getLogger("requests.packages.urllib3")
  requests_log.propagate = True
  requests_log.addHandler(default_handler)

  app = Flask(__name__)
  if os.environ['FLASK_ENV'] == "development":
    app.config.from_object('idris_server.config.DevConfig')
    app.logger.info("Starting Education with DevConfig...")
  else:
    app.config.from_object('idris_server.config.ProdConfig')
    app.logger.info('Starting Education with ProdConfig...')

  # register blueprints
  app.register_blueprint(location.bp)
  app.register_blueprint(status.bp)
  
  return app