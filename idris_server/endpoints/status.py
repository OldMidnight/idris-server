from flask import Blueprint, request, jsonify, current_app

bp = Blueprint('status', __name__, url_prefix='/status')

@bp.route('/phone', methods=['POST'])
def update_phone_status():
  '''
  Update the phone status of the user.
  '''
  current_app.logger.info(request.data)
  data = request.get_json()
  return jsonify(), 201