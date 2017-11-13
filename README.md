# Camera_calibration
This is a project to calibrate the camera.

## Dependencies:
1. OpenCV library

## Files:
### 1. corner.py
	
Input: Single image

Output: Corners in the image

### 2. remove_distortion.py

Using glob module, intakes number of images and output is a pickle file containing 'objpoints' and 'imgpoints'

### 3. undistortion test.py
Intakes a test image and pickle files. Using calibration, outputs undistorted image.

### 4. test.py
Connect wired camera and display the frames.