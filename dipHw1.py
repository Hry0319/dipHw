# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:02:03 2015

@author: k3331863
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *
import random
import NTU.DIP as dip
import math
#import scipy

#img = cv2.imread ("lena.bmp",1)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#img = cv2.imread('lenaColor.bmp',cv2.IMREAD_ANYCOLOR)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB);
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
##plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()


ScaleRate     = 2.0
theta         = 30.0

img = cv2.imread('lena.png',cv2.IMREAD_ANYCOLOR)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB);


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
#        print "%3.2f ,%3.2f |" % (ii,jj),
        scaleImg[i][j] += dip.blinear(img,ii,jj)
#    print "\n______________________________________________\n"

     
plt.subplot(221)   
plt.imshow(scaleImg, cmap = 'gray')
plt.title('scaleImg')
#cv2.imwrite("blinearScale.png", scaleImg);
#img = cv2.resize(img, (maxScaleCol, maxScaleRow))  #default bilinear interpolation
#cv2.imwrite("cv2.png", img)



x0 = img.shape[1]/2
y0 = img.shape[0]/2
height = int(math.sqrt(img.shape[0]**2 + img.shape[1]**2) +0.5)
width =  height 
tmp = int(width/2)
RotateImg = np.zeros((height, width))
theta = (theta/180.0) * np.pi
rotMatrix = np.array([[np.cos(theta), np.sin(theta)], [-1*np.sin(theta), np.cos(theta)]])
print rotMatrix

for y in range(imgRow):
    for x in range(imgColumn):   
        targetx = (x - x0) 
        targety = (y - y0)
        orgxy = np.array([targetx,targety],dtype=float)
        target = np.dot(rotMatrix, orgxy)
        nx = int(target[0]+0.5)+tmp
        ny = int(target[1]+0.5)+tmp
        RotateImg[ny][nx] = img[y][x]





cv2.imwrite("biCubic.png", RotateImg);
plt.subplot(222)   
plt.imshow(RotateImg, cmap = 'gray')
plt.title('RotateImg')