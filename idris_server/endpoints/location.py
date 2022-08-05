import os
from flask import Blueprint, request, jsonify
from idris_server.db import status_db
from idris_server.decorators import check_access_token

bp = Blueprint('location', __name__, url_prefix='/location')

@bp.route('/', methods=['Get'])
@check_access_token
def get_location():
  '''
  Get the location of the user.
  '''
  location = status_db.all()[-1]['location']
  return jsonify(location=location), 200