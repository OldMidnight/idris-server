from flask import Blueprint, request, jsonify, current_app
from idris_server.db import status_db
from idris_server.decorators import check_access_token

bp = Blueprint('status', __name__, url_prefix='/status')

@bp.route('/', methods=['POST'])
@check_access_token
def update_status():
  '''
  Update the status of the user.
  '''
  current_app.logger.info(request.data)
  data = request.get_json()

  status_db.insert(data)

  return jsonify(), 201 