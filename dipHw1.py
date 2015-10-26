# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:30:24 2015

@author: Patrick
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt
import NTU.DIP as dip

ScaleRate     = 133.73

img = cv2.imread('solid.png',cv2.IMREAD_ANYCOLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB);


#=========================================================================================#
#=========================================================================================#

imgRow     = img.shape[0]
imgColumn  = img.shape[1]
#print `row`, `column`
maxScaleRow = int(imgRow    * ScaleRate +0.5)
maxScaleCol = int(imgColumn * ScaleRate +0.5)
#print `maxScaleRow`, `maxScaleCol`
scaleImg = np.zeros((maxScaleRow, maxScaleCol))
for i in range(maxScaleRow):
    for j in range(maxScaleCol):
        ii = (i/ScaleRate)-0.5
        jj = (j/ScaleRate)-0.5
#        scaleImg[i][j] += dip.blinear(img,ii,jj)
        scaleImg[i][j] += dip.BiCubic(img,ii,jj)
#        print `ii`,`jj`


cv2.imwrite("scaleImg_.png", scaleImg);

plt.subplot(221)
plt.imshow(scaleImg, cmap = 'gray')
plt.title('scaleImg')

#=========================================================================================#
#=========================================================================================#

theta         = 30.0
img2 = cv2.imread('lena.png',cv2.IMREAD_ANYCOLOR)

imgRow     = img2.shape[0]
imgColumn  = img2.shape[1]
theta = (theta/180.0) * np.pi
height = int(img2.shape[1]*np.sin(theta) + img2.shape[0]*np.cos(theta) + 0.5)
width  = int(img2.shape[1]*np.cos(theta) + img2.shape[0]*np.sin(theta) + 0.5)
print `height`, `width`
RotateImg = np.zeros((height, width))
x0 = int(width/2+0.5)
y0 = int(height/2+0.5)
RotMatrix = np.array([[np.cos(theta), -1*np.sin(theta)], [np.sin(theta), np.cos(theta)]])
inv_RotMatrix = np.linalg.inv(RotMatrix)
#print inv_rotMatrix

for y in range(height):
    for x in range(width):
        Point = np.array([x-x0,y-y0])
        orgPoint = np.dot(Point, inv_RotMatrix)
        orgPoint[0] += float(imgColumn/2)
        orgPoint[1] += float(imgRow/2)
        if ((orgPoint[0] >= 0) and (orgPoint[0] < imgColumn)) and ((orgPoint[1] >= 0) and (orgPoint[1] < imgRow)):
#            RotateImg[y][x] = dip.blinear(img ,orgPoint[1],orgPoint[0])
            RotateImg[y][x] = dip.BiCubic(img2 ,orgPoint[1],orgPoint[0])

cv2.imwrite("RotateImg.png", RotateImg);
plt.subplot(222)
plt.imshow(RotateImg, cmap = 'gray')
plt.title('RotateImg')

#=========================================================================================#
#=========================================================================================#