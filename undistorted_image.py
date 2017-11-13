import pickle
import cv2

# Read in the saved objpoints and imgpoints
pickle_in = open("objpoints.pickle", "rb")
objpoints = pickle.load(pickle_in)

pickle_in1 = open("imgpoints.pickle", "rb")
imgpoints = pickle.load(pickle_in1)
# print(objpoints, imgpoints)

# Read in an image
img = cv2.imread('9.JPG')
img = cv2.resize(img, (640, 480))
original_image = img


# TODO: Write a function that takes an image, object points, and image points
# performs the camera calibration, image distortion correction and
# returns the undistorted image
def cal_undistort(img, objpoints, imgpoints):
    img = img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # ret, corners = cv2.findChessboardCorners(gray, (7, 5), None)
    # img = cv2.drawChessboardCorners(img, (7, 5), corners, ret)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    dst = cv2.undistort(img, mtx, dist, None, mtx)

    return dst


undistorted = cal_undistort(img, objpoints, imgpoints)
cv2.imshow('Undistorted', undistorted)
cv2.imshow('Original', original_image)

cv2.waitKey()
cv2.destroyAllWindows()