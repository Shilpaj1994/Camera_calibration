# import numpy as np
# import cv2
# import glob
#
# # termination criteria
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
#
# # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
# objp = np.zeros((6*8, 3), np.float32)
# objp[:, :2] = np.mgrid[0:8, 0:6].T.reshape(-1, 2)
#
# # Arrays to store object points and image points from all the images.
# objpoints = []  # 3d point in real world space
# imgpoints = []  # 2d points in image plane.
#
# images = glob.glob('*.JPG')
# test_img = cv2.imread('1.JPG')
# test_img = cv2.resize(test_img, (640, 480))
#
# for fname in images:
#     img = cv2.imread(fname)
#     img = cv2.resize(img, (640, 480))
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     balanced = cv2.equalizeHist(gray)
#
#     # Find the chess board corners
#     ret, corners = cv2.findChessboardCorners(gray, (7, 5), None)
#
#     # If found, add object points, image points (after refining them)
#     if ret == True:
#         objpoints.append(objp)
#
#         corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
#         imgpoints.append(corners2)
#
#         # Draw and display the corners
#         img = cv2.drawChessboardCorners(img, (7, 5), corners2, ret)
#         cv2.imshow('img', img)
#         cv2.waitKey(500)
#
# ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, (640, 480), None, None)
# dst = cv2.undistort(test_img, mtx, dist, None, mtx)
#
# cv2.imshow('Disp', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()



import pickle
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read in the saved objpoints and imgpoints
pickle_in = open("objpoints.pickle", "rb")
objpoints = pickle.load(pickle_in)

pickle_in1 = open("imgpoints.pickle", "rb")
imgpoints = pickle.load(pickle_in1)

print(objpoints, imgpoints)

# Read in an image
img = cv2.imread('2.JPG')
img = cv2.resize(img, (640, 480))

# TODO: Write a function that takes an image, object points, and image points
# performs the camera calibration, image distortion correction and
# returns the undistorted image
def cal_undistort(img, objpoints, imgpoints):
    # img = cv2.imread('1.jpg')
    # img = cv2.resize(img, (640, 480))
    img = img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    ret, corners = cv2.findChessboardCorners(gray, (7, 5), None)
    img = cv2.drawChessboardCorners(img, (7, 5), corners, ret)
    # cv2.imshow('Disp', img)
    # cv2.waitKey()

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    dst = cv2.undistort(img, mtx, dist, None, mtx)

    return dst


undistorted = cal_undistort(img, objpoints, imgpoints)
cv2.imshow('Disp', undistorted)

cv2.waitKey()
cv2.destroyAllWindows()


# f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
# f.tight_layout()
# ax1.imshow(img)
# ax1.set_title('Original Image', fontsize=50)
# ax2.imshow(undistorted)
# ax2.set_title('Undistorted Image', fontsize=50)
# plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)