from flask import Flask, request, render_template


app = Flask(__name__)

@app.route(rule="/")
def home():
    return render_template("index.html")

# make a link page
@app.route(rule="/page")
def message_page():
    return render_template("message.html")


@app.route(rule="/page/<value>")
def message_page2(value):
    return render_template("message.html", value=value)




if __name__ == "__main__":
    app.run(debug=True)