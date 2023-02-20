from flask import Flask, jsonify


app = Flask(__name__)


@app.route(rule="/")
def home():
    return "This is the home page"


@app.route(rule="/user")
def userInfo():
    info = {
        "name": "Alamin",
        "email": "alaminbhuyan321@gmail.com",
        "age": 23,
        "address": "Uttara, Dhaka-1230",
        "phone": "01875780315"
    }
    return jsonify(info)


if __name__ == "__main__":
    app.run(debug=True)