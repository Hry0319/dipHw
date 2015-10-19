# -*- coding: utf-8 -*-
def cubic ():
#test0 = np.matrix([[4, 2], [3, 1]])
#data  = np.matrix([9,8])
#print data*test0
    return



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
