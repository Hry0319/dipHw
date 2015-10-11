# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:02:03 2015

@author: k3331863
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *


#img = cv2.imread ("lena.bmp",1)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#img = cv2.imread('lenaColor.bmp',cv2.IMREAD_ANYCOLOR)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB);
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
##plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()


img = cv2.imread('81.png',cv2.IMREAD_ANYCOLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB);

width = img.shape[1]
height = img.shape[0]
x0 = img.shape[1]/2
y0 = img.shape[0]/2

maxRow = math.sqrt(img.shape[0]**2 + img.shape[1]**2)
maxCol = maxRow
#print maxCol    #1347.62494782

scale1 = np.zeros(shape=(maxRow+1,maxCol+1))
#print scale1.shape


