import cv2
import glob
import numpy as np


def undistort(img):
    frame = img

    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((6 * 7, 3), np.float32)
    objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

    # Arrays to store object points and image points from all the images.
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.

    images = glob.glob('*.jpg')

    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)

        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)

            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, (7, 6), corners2, ret)
            cv2.imshow('img', img)
            cv2.waitKey(500)

    cv2.destroyAllWindows()




cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    undistort(frame)
#     size = frame.shape[:2]
#     # print(size)
#
#     # undistort = cv2.undistort(frame, size, 1, 1, size)
#
#     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # blur = cv2.GaussianBlur(gray, (5, 5), 2)
#     # edges = cv2.Canny(frame, 100, 300)
#     #
#     # cv2.imshow('Grya', gray)
#     # # cv2.imshow('Blur', blur)
#     # cv2.imshow('Edges', edges)
#     cv2.imshow('Original', frame)
#     # cv2.imshow('Undistorted image', undistort)
#
    if cv2.waitKey(1) == 27:
        break
