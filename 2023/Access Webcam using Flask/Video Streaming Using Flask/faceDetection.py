from flask import Flask,render_template,Response
import cv2


app = Flask(__name__)

capture_video = cv2.VideoCapture(0)


def generateFrame():
    while True:
        success, frame = capture_video.read()
        if not success:
            break
        else:
            # Load the Cascade Classifier
            face_cascade = cv2.CascadeClassifier("model/haarcascade_frontalface_default.xml")
            eye_detector = cv2.CascadeClassifier("model/haarcascade_eye.xml")

            # Convert color frame into gray
            gray_frame = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
            # Detect the faces
            faces = face_cascade.detectMultiScale(image=gray_frame, scaleFactor=1.1, minNeighbors=6)
            # Display Rectangle
            for (x, y, width, height) in faces:
                cv2.rectangle(img=frame, pt1=(x, y), pt2=(x + width, y + height), color=(255, 0, 255), thickness=2)
                eyes = eye_detector.detectMultiScale(image=frame, scaleFactor=1.2, minNeighbors=5)
                for (x, y, width, height) in eyes:
                    cv2.rectangle(img=frame, pt1=(x, y), pt2=(x + width, y + height), color=(255, 0, 245), thickness=2)

            ret, buffer = cv2.imencode(ext=".jpg", img=frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route(rule="/")
def home():
    return render_template(template_name_or_list="index.html")


@app.route(rule="/video")
def liveVideo():
    return Response(response=generateFrame(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(debug=True)