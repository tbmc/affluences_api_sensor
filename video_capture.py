import cv2 as cv

video_capture = cv.VideoCapture(0)
opened = video_capture.isOpened()

if not opened:
    print("Cannot open stream")
    exit(1)


def read():
    _, image = video_capture.read()
    cv.imshow("Video", image)
    cv.waitKey()
    cv.destroyAllWindows()

