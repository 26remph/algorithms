import flask


app = flask.Flask(__name__)


@app.route("/")
def index():
    # answer = [b'Hello!', b'Server works correctly!']
    # answer = [b'9', b'8', b'7', b'6', b'5', b'4', b'3', b'2', b'1', b'0']
    # return flask.jsonify([1, 2, "ошибка", 4])
    return flask.jsonify({"first": "1", "third": "3"})


@app.route("/first")
def first():
    return flask.jsonify([1, 2, 3])


@app.route("/second")
def second():
    return flask.jsonify([2, 4, 6])


@app.route("/third")
def third():
    return flask.jsonify([3, 6, 9])


if __name__ == "__main__":
    app.run()
