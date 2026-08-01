
import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
	return flask.jsonify({"message": "Face News Detection service running"})


if __name__ == "__main__":
	# Run in development mode on localhost:5000
	app.run(host="127.0.0.1", port=5000, debug=True)
