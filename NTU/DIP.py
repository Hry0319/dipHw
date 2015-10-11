# -*- coding: utf-8 -*-
def blinear (img, ii, jj):    
    """
   (left_j,top_i)
                a_________b
                |    |β   |
                |_α__|p   |
                |_________|    
                c         d        
    """
    
    left_j = int(jj) 
    top_i  = int(ii)      
#    print `top_i`,`left_j2`
    
    alpha = jj - left_j 
    beta  = ii - top_i  
    

    if img.shape[0]-1 == top_i :
        top_i  -= 1
    if img.shape[1]-1 == left_j :
        left_j -= 1         
     
    a = (top_i   ,left_j  )
    b = (top_i   ,left_j+1)
    c = (top_i+1 ,left_j  )
    d = (top_i+1 ,left_j+1)  
    
    
    weight = (1-alpha) * (1-beta) * img[a[0]][a[1]] + \
             (alpha)   * (1-beta) * img[b[0]][b[1]] + \
             (1-alpha) * (beta)   * img[c[0]][c[1]] + \
             (alpha)   * (beta)   * img[d[0]][d[1]]
                 
                   
    return weight
