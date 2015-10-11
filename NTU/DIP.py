# -*- coding: utf-8 -*-
import math
def blinear (img, ii, jj):    
    """
   (left_j,top_i)
            |_> a_________b
                |    |β   |
                |_α__|p   |
                |_________|    
                c         d        
    """
    
    left_j = math.floor(jj) 
    top_i  = math.floor(ii)    
    
    alpha = jj - left_j
    beta  = ii - top_i
#    print `left_i` ," ",  `top_j` , "|",    
    
    a = (top_i   ,left_j  )
    b = (top_i   ,left_j+1)
    c = (top_i+1 ,left_j  )
    d = (top_i+1 ,left_j+1)

    if img.shape[0]-1 <= top_i and img.shape[1]-1 <= left_j :
        b = (top_i-1  ,left_j)
        c = (top_i  ,left_j-1)
        d = (top_i  ,left_j)
    elif img.shape[0]-1 <= top_i :
        c = (top_i  ,left_j  )        
        d = (top_i  ,left_j+1)
    elif img.shape[1]-1 <= left_j :
        b = (top_i   ,left_j )
        d = (top_i+1 ,left_j )       
        
        
#    if   img.shape[0]-1 == top_i and img.shape[1]-1 == left_j : 
#                 
#    elif img.shape[0]-1 == top_i:  
#        weight = (1-alpha) * img[a[0]][a[1]] + \
#                 (alpha)   * img[b[0]][b[1]]
#                 
#    elif img.shape[1]-1 == left_j:        
#        weight = (1-beta) * img[a[0]][a[1]] + \
#                 (beta)   * img[c[0]][c[1]] 
#                 
#    else :
    weight = (1-alpha) * (1-beta) * img[a[0]][a[1]] + \
             (alpha)   * (1-beta) * img[b[0]][b[1]] + \
             (1-alpha) * (beta)   * img[c[0]][c[1]] + \
             (alpha)   * (beta)   * img[d[0]][d[1]]
                 
                   
    return weight
