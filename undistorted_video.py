import cv2
import pickle

# Read in the saved objpoints and imgpoints
pickle_in = open("objpoints.pickle", "rb")
objpoints = pickle.load(pickle_in)

pickle_in1 = open("imgpoints.pickle", "rb")
imgpoints = pickle.load(pickle_in1)
# print(objpoints, imgpoints)

cap = cv2.VideoCapture(1)

def undistort(img):
    gray = img
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    dst = cv2.undistort(gray, mtx, dist, None, mtx)
    return dst


while True:
    ret, frame = cap.read()
    size = frame.shape[:2]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = undistort(gray)
    # blur = cv2.GaussianBlur(gray, (5, 5), 2)
    # edges = cv2.Canny(frame, 100, 300)

    cv2.imshow('Gray', gray)
    # cv2.imshow('Blur', blur)
    # cv2.imshow('Edges', edges)
    cv2.imshow('Original', frame)

    if cv2.waitKey(1) == 27:
        break