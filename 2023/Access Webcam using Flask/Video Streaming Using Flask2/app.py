import cv2
from flask import Flask, render_template, Response

app = Flask(__name__)


read_camera = cv2.VideoCapture(0)

def generateFrame():
    while True:
        success, frame = read_camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode(ext=".jpg", img=frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route(rule="/")
def home():
    return render_template(template_name_or_list="index.html")


@app.route(rule="/start", methods=["POST"])
def startVideo():
    return Response(response=generateFrame(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run(debug=True)