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

import scipy

#img = cv2.imread ("lena.bmp",1)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#img = cv2.imread('lenaColor.bmp',cv2.IMREAD_ANYCOLOR)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB);
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
##plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()

ScaleRate = 3

img = cv2.imread('lena-org.png',cv2.IMREAD_ANYCOLOR)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB);


column  = img.shape[1]
row     = img.shape[0]

maxScaleRow = int( row    * ScaleRate)
maxScaleCol = int( column * ScaleRate) 
scaleImg = np.zeros(shape=(maxScaleRow,maxScaleCol))

for i in range(maxScaleRow):
    for j in range(maxScaleCol):
        ii = ((i/ScaleRate))
        jj = ((j/ScaleRate))
        print jj, 
#        scaleImg[i][j] = dip.blinear(img,ii,jj) 
     
#plt.subplot(221)   
#plt.imshow(scaleImg, cmap = 'gray')
#plt.title('scaleImg')
cv2.imwrite("blinearScale.png", scaleImg);


#img = cv2.resize(img, (381, 381))  #default bilinear interpolation
#cv2.imwrite("cv2___.png", img)






x0 = img.shape[1]/2
y0 = img.shape[0]/2

maxRotateRow = math.sqrt(img.shape[0]**2 + img.shape[1]**2)
maxRotateCol = maxRotateRow  


