from flask import Flask, request, render_template


app = Flask(__name__)


@app.route(rule="/")
def home():
    return render_template("index.html")

@app.route(rule="/upload", methods=["POST"])
def uploadImg():
    if request.method == "POST":
        file = request.files.get("file")
        file.save(dst=f"static/images/{file.filename}")
    return "Successfully uploaded"


if __name__ == "__main__":
    app.run(debug=True)
