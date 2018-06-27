import numpy as np
import argparse
import cv2


orig= cv2.imread('images.jpg')
h,w=orig.shape[0],orig.shape[1]
image=orig.copy()
#image=cv2.resize(image,(w/2,h/2))
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray=cv2.bilateralFilter(gray,11,25,25)

cv2.imshow('gray',gray)
edged=cv2.Canny(gray,10,220)
cv2.imshow('edged',edged)
cv2.waitKey(0)
im, cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10] # get largest five contour area
screenCnt = None
cv2.waitKey(0)
for c in cnts:
    peri=cv2.arcLength(c, True)
    approx= cv2.approxPolyDP(c, 0.02*peri, True)

    if len(approx)==4:
        screenCnt = approx
        break
print screenCnt

cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
x,y,width,height=cv2.boundingRect(screenCnt)
print x,y,width,height
roi=image[y:y+height,x:x+width]
roi_gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
ret,roi_thresh=cv2.threshold(roi_gray,100,255,cv2.THRESH_BINARY)

cv2.imshow('roi_gray',roi_thresh)
cv2.imshow("Game Boy Screen",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
