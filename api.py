from flask import Flask, request, send_file
from video_capture import read

app = Flask(__name__)


QUALITIES = {
    "480p": (720, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080)
}


@app.route("/")
def get_image():
    quality = request.args.get("quality", default="480p")
    blur = request.args.get("blur", default=False)

    width, height = QUALITIES.get(quality, (None, None))

    if width is None:
        return "Error"

    read(width, height, blur)
    return send_file("image.jpg", mimetype="image/jpeg")



