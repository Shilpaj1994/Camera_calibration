import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# prepare object points
nx = 7   # TODO: enter the number of inside corners in x
ny = 5   # TODO: enter the number of inside corners in y

# Make a list of calibration images
fname = '9.JPG'

img = cv2.imread(fname)
resize = cv2.resize(img, (640, 480))
    # cv2.imshow('Original', img)

# Convert to grayscale
gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Grayscale', gray)

# Histogram equilization
balanced = cv2.equalizeHist(gray)
    # cv2.imshow('Balanced', balanced)

# Find the chessboard corners
ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)

# If found, draw corners
if ret == True:
    # Draw and display the corners
    cv2.drawChessboardCorners(resize, (nx, ny), corners, ret)
    # plt.imshow(resize)
    cv2.imshow('Result', resize)

cv2.waitKey()
cv2.destroyAllWindows()
