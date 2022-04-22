from flask import Flask
from video_capture import read

app = Flask(__name__)


@app.route("/")
def get_image():
    read()
    return "test"



