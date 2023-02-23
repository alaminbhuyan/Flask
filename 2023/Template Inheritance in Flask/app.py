from flask import Flask,render_template


app = Flask(__name__)


@app.route(rule="/")
def homePage():
    return render_template("index.html")


@app.route(rule="/profile")
def profilePage():
    return render_template("profile.html")


@app.route(rule="/about")
def aboutPage():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)