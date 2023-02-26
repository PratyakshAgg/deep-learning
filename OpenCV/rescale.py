import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Works for Images, Videos and Live Video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Works only for Live Videos
    capture.set(3, width)
    capture.set(4, height)


# Recording Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale = 0.50)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


img = cv.imread('Photos/cat_large.jpg')
img_resized = rescaleFrame(img, scale=0.50)

cv.imshow('Cat', img)
cv.imshow('Cat Resized', img_resized)

cv.waitKey(0)