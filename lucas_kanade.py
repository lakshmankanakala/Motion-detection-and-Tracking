import imutils
import numpy as np
import cv2
import time
from time import sleep
from scipy import signal
from PIL import Image
from numpy import *
import random
from matplotlib import pyplot as plt
from pylab import *
def LUCAS_KANADE(image1,image2):
        print('haii')
        I1 = np.array(image1)
        I2 = np.array(image2)
        Shape = np.shape(I1)

        Image1_smooth = cv2.GaussianBlur(I1, (3,3), 0)
        Image2_smooth = cv2.GaussianBlur(I2, (3,3), 0)
        # First Derivative in X direction
        Ix = signal.convolve2d(Image1_smooth,[[-0.25,0.25],[-0.25,0.25]],'same') + signal.convolve2d(Image2_smooth,[[-0.25,0.25],[-0.25,0.25]],'same')
        # First Derivative in Y direction
        Iy = signal.convolve2d(Image1_smooth,[[-0.25,-0.25],[0.25,0.25]],'same') + signal.convolve2d(Image2_smooth,[[-0.25,-0.25],[0.25,0.25]],'same')
        # First Derivative in XY direction
        It = signal.convolve2d(Image1_smooth,[[0.25,0.25],[0.25,0.25]],'same') + signal.convolve2d(Image2_smooth,[[-0.25,-0.25],[-0.25,-0.25]],'same')
        features = cv2.goodFeaturesToTrack(Image1_smooth,8000,0.01,10)
        feature = np.int0(features)
        for i in feature:
                x,y = i.ravel()
                cv2.circle(Image1_smooth,(x,y),3,0,-1)     #image,center,radius,colour of circle,thickness of line           

        u = v = np.nan*np.ones(Shape)
        for l in feature:
                j,i = l.ravel()
                IX = ([Ix[i-1,j-1],Ix[i,j-1],Ix[i+1,j+1],Ix[i-1,j],Ix[i,j],Ix[i+1,j],Ix[i-1,j+1],Ix[i,j+1],Ix[i+1,j-1]])# x-cmpnt of gradient vector
                IY = ([Iy[i-1,j-1],Iy[i,j-1],Iy[i+1,j+1],Iy[i-1,j],Iy[i,j],Iy[i+1,j],Iy[i-1,j+1],Iy[i,j+1],Iy[i+1,j-1]])# y-cmpnt of gradient vector
                IT = ([It[i-1,j-1],It[i,j-1],It[i+1,j+1],It[i-1,j],It[i,j],It[i+1,j],It[i-1,j+1],It[i,j+1],It[i+1,j-1]])#x-y cmpnt of gradient vector


                LK = (IX, IY)
                
                LK = np.matrix(LK)
                
                LK_T = np.array(np.matrix(LK)) 
                
                LK = np.array(np.matrix.transpose(LK)) # transpose of A
                
                A1 = np.dot(LK_T,LK) #Psedudo Inverse
                A2 = np.linalg.pinv(A1)
                A3 = np.dot(A2,LK_T)
                
                #sleep(2)
                (u[i,j],v[i,j]) = np.dot(A3,IT)
                print(v[i,j],u[i,j])
        colors = "rgb"
        
        c=colors[2]
        plt.imshow(I1,cmap = cm.gray)
        for i in range(Shape[0]):
	        for j in range(Shape[1]):
		        if abs(u[i,j])>t or abs(v[i,j])>t: 
			        plt.arrow(j,i,v[i,j],u[i,j],head_width = 5, head_length = 5, color = c)   ##plotting arrays
                                
			
        plt.show()






cap = cv2.VideoCapture(1)
t = 0.3
while cap.isOpened():
        ret, frame = cap.read()
        if ret:
                ret, frame = cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                #cv2.imshow('sd',frame)
                #cv2.waitKey(0)
                ret,frame = cap.read()
                gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                LUCAS_KANADE(gray, gray1)


