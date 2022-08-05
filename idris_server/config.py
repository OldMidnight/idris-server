import os

# This file is used to configure the Flask server.
class Config(object):
  SECRET_KEY = os.environ['SECRET_KEY']

class DevConfig(Config):
  DEBUG = True
  PROPAGATE_EXCEPTIONS = False

class ProdConfig(Config):
  DEBUG = False
  PROPAGATE_EXCEPTIONS = True