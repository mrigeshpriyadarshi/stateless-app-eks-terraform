import json
import os
from flask import Flask
from flask import jsonify, request


app = Flask(__name__)

@app.errorhandler(404)
def not_found(error=None):
	message = {
		'status': 404,
		'message': 'Not Found: ' + request.url,
	}
	resp = jsonify(message)
	resp.status_code = 404
	return resp

	# API SECTION

@app.route('/api/v1/connect')
def connect():
	# validate the received values
	with app.app_context():
		resp = jsonify('Howdy from Stateless API!')
		resp.status_code = 200
		return resp


@app.route('/api/v1/post', methods=['POST'])
def api_get_users():
	_json = request.json
	# validate the received values
	if 'name' in _json and request.method == 'POST':
		resp = jsonify("Hello " + _json['name'])
		resp.status_code = 200
		return resp
	else:
		return not_found()

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)