import flask

from requests import HTTPError


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


@app.route("/users")
def users():
    return flask.jsonify([
        {
            "id": 1,
            "username": "first",
            "last_name": "Петрова",
            "first_name": "Елизавета",
            "email": "e.petrova@server.none",
        },
        {
            "id": 2,
            "username": "second",
            "last_name": "Иванов",
            "first_name": "Василий",
            "email": "vas.ivanov@server.none",
        },
        {
            "id": 3,
            "username": "third",
            "last_name": "Иванов",
            "first_name": "Виктор",
            "email": "vik.ivanov@server.none",
        },
    ])


@app.route("/users/<user_id>")
def user_by_id(user_id):
    if user_id == "1":
        raise HTTPError(404)
    return flask.jsonify({
        "id": user_id,
        "username": "first",
        "last_name": "Ivanov",
        "first_name": "Vasily",
        "email": "t@ya.ro",
    })


if __name__ == "__main__":
    app.run()
