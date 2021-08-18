soothingSongs = [
	{
		"id": 1,
		"SoothingSongs": "https://www.youtube.com/watch?v=h3uJKEDsyCM"
	},
	{
		"id": 2,
		"SoothingSongs": "https://www.youtube.com/watch?v=xgc1SlB9gk4"
	},
	{
		"id": 3,
		"SoothingSongs": "https://www.youtube.com/watch?v=CcsUYu0PVxY"
	},
	{
		"id": 4,
		"SoothingSongs": "https://www.youtube.com/watch?v=CcsUYu0PVxY"
	},
	{
		"id": 5,
		"SoothingSongs": "https://www.youtube.com/watch?v=lFcSrYw-ARY"
	},
	{
		"id": 6,
		"SoothingSongs": "https://www.youtube.com/watch?v=_zScs9cYWsw"
	},
	{
		"id": 7,
		"SoothingSongs": "https://www.youtube.com/watch?v=KRA26LhuTP4"
	},
	{
		"id": 8,
		"SoothingSongs": "https://www.youtube.com/watch?v=ZFxw4lfzckI"
	},
	{
		"id": 9,
		"SoothingSongs": "https://www.youtube.com/watch?v=bP9gMpl1gyQ"
	}
]

import flask
from flask import request, jsonify
import random

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Soothing Songs Recommendation</h1>
<p>A prototype API for Soothing Soothing Songs Recommendation.</p>'''


@app.route('/api/songs/all', methods=['GET'])
def api_all():
    return jsonify(soothingSongs)


@app.route('/api/songs/random', methods=['GET'])
def api_id():
    results = []
    r = random.randint(1,9)
    # r0 = str(r)
    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for song in soothingSongs:
        if song['id'] == r:
            results.append(song)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)
if __name__ == "__main__":
    app.run(debug = True, use_reloader=False)