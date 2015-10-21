# -*- coding: utf-8 -*-
import cv2
import numpy as np


def BiCubic(img,y,x):
    width  = img.shape[1]-1
    height = img.shape[0]-1
    x0 = int(x)
    y0 = int(y)
    alpha = x - x0
    beta  = y - y0
    
    mm = np.zeros((4, 4))  
    
    Yindex = 0
    Yend   = 4
    Xindex = 0
    Xend   = 4    
    
    if y0 == 0 and x0 == 0:
        Xindex = 1
        Yindex = 1
    elif y0 == 0:
        Yindex = 1
    elif x0 == 0:
        Xindex = 1
        
    if y0 == height and x0 == width:
        Xend = 1
        Yend = 1
    elif y0 == height-1 and x0 == width-1:
        Xend = 2
        Yend = 2
    if y0 == height:
        Yend = 1
    elif y0 == height-1:
        Yend = 2
    if x0 == width:
        Xend = 1
    elif x0 == width-1:
        Xend = 2
    
    
    for i in range(Yindex, Yend):
        for j in range(Xindex, Xend):
            mm[i][j] = 1
            
            
    for i in range(4):
        for j in range(4):
            if mm[i][j] == 1:
                mm[i][j] = img[y0-1+i][x0-1+j]
                
    y0 = Cubic(mm[0][0],mm[0][1],mm[0][2],mm[0][3],alpha)
    y1 = Cubic(mm[1][0],mm[1][1],mm[1][2],mm[1][3],alpha)
    y2 = Cubic(mm[2][0],mm[2][1],mm[2][2],mm[2][3],alpha)
    y3 = Cubic(mm[3][0],mm[3][1],mm[3][2],mm[3][3],alpha)
    
    ans = Cubic(y0,y1,y2,y3,beta)
        
    return ans

def Cubic(p0,p1,p2,p3,x):
    ff1 = (p3-p1)/2
    f1  = p2
    ff0 = (p2-p0)/2
    f0  = p1
    c = ff0
    d = f0
    a = ff1-2*f1+c+2*d
    b = f1-a-c-d
        
    return a*x**3 + b*x**2 + c*x + d
    
    
def rotateImage(image, angle):
    image_center = tuple(np.array(image.shape)/2)
    rot_mat = cv2.getRotationMatrix2D(image_center,angle,1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape,flags=cv2.INTER_CUBIC)
    return result

def blinear (img, ii, jj):    
    """
   (left_j,top_i)
                a_________b
                |    |β   |
                |_α__|p   |
                |_________|    
                c         d        
    """
    if ii < 0:
        ii = 0
    if jj < 0:
        jj = 0   
    left_j = int(jj)
    top_i  = int(ii)      

#    print `top_i`,`left_j2`    
    alpha = jj - left_j 
    beta  = ii - top_i      
    rows = img.shape[0]-1
    cols = img.shape[1]-1
        
    if   top_i < rows and left_j < cols :    
#        if top_i == 0 and left_j == 0:
#            alpha = 0
#            beta  = 0
#        elif top_i == 0:
#            beta = 0
#        elif left_j == 0:
#            alpha = 0            
        a = (top_i   ,left_j  )
        b = (top_i   ,left_j+1)
        c = (top_i+1 ,left_j  )
        d = (top_i+1 ,left_j+1) 
                 
    elif  top_i >= rows and left_j >= cols : 
        a = (top_i   ,left_j  )
        b = (0, 0)
        c = (0, 0)
        d = (0, 0)
    
    elif top_i >= rows :
        a = (top_i   ,left_j  )
        b = (top_i   ,left_j+1)
        c = a
        d = b    
        
    elif left_j >= cols : 
        a = (top_i   ,left_j  )
        b = a
        c = (top_i+1 ,left_j  )
        d = c     
     
    weight = (1-alpha) * (1-beta) * img[a[0]][a[1]] + \
             (alpha)   * (1-beta) * img[b[0]][b[1]] + \
             (1-alpha) * (beta)   * img[c[0]][c[1]] + \
             (alpha)   * (beta)   * img[d[0]][d[1]]
                   
    return weight
