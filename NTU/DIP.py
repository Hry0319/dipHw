# -*- coding: utf-8 -*-
import math
def blinear (img, ii, jj):
    
#    a_________b
#    |    |β   |
#    |_α__|p   |
#    |_________|    
#    c         d
    
    left_i = math.floor(ii) 
    top_j  = math.floor(jj)
    
    a = (left_i     ,top_j    )
    b = (left_i     ,top_j + 1)
    c = (left_i + 1 ,top_j    )
    d = (left_i + 1 ,top_j + 1)
    
    alpha = ii - left_i
    beta  = jj - top_j
#    print `alpha`+","+`beta`
    
    weight = (3-alpha)*(3-beta)*img[a[0]][a[1]] + \
             (alpha)  *(3-beta)*img[b[0]][b[1]] + \
             (3-alpha)*(beta)  *img[c[0]][c[1]] + \
             (alpha)  *(beta)  *img[d[0]][d[1]]
             
#    weight2 = (1-alpha)*(1-beta)*img[a[0]][a[1]]+(alpha)*(1-beta)*img[b[0]][b[1]]+(1-alpha)*(beta)*img[c[0]][c[1]]+(alpha)*(beta)*img[d[0]][d[1]]
#    print `weight`+","+`weight2`    
     
    return weight/9
