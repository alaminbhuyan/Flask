from flask import Flask, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os



UPLOAD_FOLDER = "static/uploads/"



ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}


app = Flask(__name__)

app.secret_key = "secret_key"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route(rule="/")
def home():
    return render_template(template_name_or_list="home.html")


@app.route(rule="/", methods=["GET", "POST"])
def upload_file():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Image successfully uploaded and displayed below')
            return render_template(template_name_or_list='home.html', filename=filename)
        else:
            flash('Allowed image types are - png, jpg, jpeg, gif')
            return redirect(location=request.url)


@app.route(rule="/display/<filename>")
def display_image(filename):
    return redirect(location=url_for('static', filename='uploads/' + filename), code=301)




if __name__ == '__main__':
    app.run(debug=True)


# to run flask app write = flask run
# to run flask app write = python app.py
