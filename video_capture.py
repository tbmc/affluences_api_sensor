import cv2 as cv

video_capture = cv.VideoCapture(0)
opened = video_capture.isOpened()

if not opened:
    print("Cannot open stream")
    exit(1)


def read(width: int, height: int, blur: bool):
    _, image = video_capture.read()
    resized = cv.resize(image, (width, height))
    to_write = resized
    if blur:
        to_write = cv.GaussianBlur(to_write, (51, 51), 0)
    cv.imwrite("image.jpg", to_write)

