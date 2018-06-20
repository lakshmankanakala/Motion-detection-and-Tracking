import cv2
import numpy as np


cap = cv2.VideoCapture('C:/Users/rgukt/Desktop/vid.mp4')
previousFrame=None

while(cap.isOpened()):

  ret, frame = cap.read()

  if previousFrame is not None:
      #use previous frame here
      pass

  #save current frame
  previousFrame=frame


  gray = cv2.cvtColor(previousFrame, cv2.COLOR_BGR2GRAY)
  gray =cv2.resize(gray,(500,500))
  #cv2.imshow("grayframe",gray)
  ret, frame = cap.read()
  gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  gray1 = cv2.resize(gray1,(500,500))
  
  difference = cv2.absdiff(gray1, gray)
  
  ret,thresh = cv2.threshold(difference, 40, 255, 0)
  
  im2, cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  final_frame = cv2.resize(frame,(500,500))
  for cn in cnts:
    if cv2.arcLength(cn,True)> 10:
      (x, y, w, h) = cv2.boundingRect(cn)
      cv2.rectangle(final_frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
      cv2.imshow('frame',final_frame)
    
  if cv2.waitKey(100) & 0xFF == ord('q'):
       break

cap.release()
cv2.destroyAllWindows()
