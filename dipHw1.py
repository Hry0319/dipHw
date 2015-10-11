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


ScaleRate = 0.8

img = cv2.imread('lena.bmp',cv2.IMREAD_ANYCOLOR)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB);


imgRow     = img.shape[0] 
imgColumn  = img.shape[1]
#print `row`, `column`

maxScaleRow = int(imgRow    * ScaleRate)
maxScaleCol = int(imgColumn * ScaleRate)
#print `maxScaleRow`, `maxScaleCol`

scaleImg = np.zeros((maxScaleRow,maxScaleCol), dtype=float)
#scaleImg = np.ndarray(shape = (maxScaleRow, maxScaleCol), dtype = float, order = 'F')
#for i in range(maxScaleRow):
#    for j in range(maxScaleCol):
#        scaleImg[i][j] = 0


for i in range(maxScaleRow):
    for j in range(maxScaleCol):        
        ii = float(i)/ScaleRate
        jj = float(j)/ScaleRate
#        print `ii`,",",`jj` ,"|",
#        if imgRow-1 == int(ii) and imgColumn-1 == int(jj):            
            
        scaleImg[i][j] = dip.blinear(img,ii,jj)
#    print "\n\n"
    

     
#plt.subplot(111)   
#plt.imshow(scaleImg, cmap = 'gray')
#plt.title('scaleImg')
cv2.imwrite("blinearScale.png", scaleImg);


img = cv2.resize(img, (maxScaleCol, maxScaleRow))  #default bilinear interpolation
cv2.imwrite("cv2.png", img)






x0 = img.shape[1]/2
y0 = img.shape[0]/2

maxRotateRow = math.sqrt(img.shape[0]**2 + img.shape[1]**2)
maxRotateCol = maxRotateRow  


