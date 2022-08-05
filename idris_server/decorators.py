import os
from flask import request, jsonify, current_app

# Decorator for checking ig the access token is valid.
def check_access_token(func):
  def wrapper(*args, **kwargs):
    valid_access_token = os.getenv('VALID_ACCESS_TOKEN')
    current_app.logger.info(valid_access_token)
    current_app.logger.info(request.headers)
    access_token = request.headers.get('Authorization')
    if access_token == valid_access_token:
      return func(*args, **kwargs)
    else:
      return jsonify(error='Invalid access token'), 401
  return wrapper