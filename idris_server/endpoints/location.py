from flask import Blueprint, request, jsonify

bp = Blueprint('location', __name__, url_prefix='/location')

@bp.route('/', methods=['PUT'])
def update_location():
  '''
  Update the location of the user.
  '''
  data = request.get_json()
  print(data)
  return jsonify(data)