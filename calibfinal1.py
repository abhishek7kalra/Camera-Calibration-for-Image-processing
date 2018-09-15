import numpy as np
import cv2
cap = cv2.VideoCapture(0)
# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
n=0
while(n<15):
    tf, frame = cap.read()       
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7,6),None)   
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners)    
        # Draw and display the corners
        cv2.drawChessboardCorners(frame, (7,6), corners,ret)
        cv2.imshow('x', gray)
        cv2.imshow('Single frame', frame)
        key= cv2.waitKey(0)
        n=n+1
        print tf
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
cap.release()
cv2.destroyAllWindows()
      