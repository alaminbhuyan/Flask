from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)

@app.route(rule="/")
def home():
    return "<h1>This is Home page</h1>"


@app.route(rule="/about")
def about():
    return "<h1>This is About page</h1>"



if __name__ == "__main__":
    app.run(debug=True)