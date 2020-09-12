#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def determinant(mat,n): 
  
    temp = [0]*n   
    total=1 
    det=1  
   
    for i in range(0,n): 
        index=i  
  
        # finding the index which has non zero value   
        while(mat[index][i] == 0 and index < n): 
            index+=1
     
        if(index == n): # if there is non zero element 
            # the determinat of matrix as zero 
            continue
  
        if(index != i): 
            # loop for swaping the diagonal element row and index row 
            for j in range(0,n): 
                mat[index][j],mat[i][j] = mat[i][j],mat[index][j] 
                  
            # determinant sign changes when we shift rows     
            det = det*int(pow(-1,index-i)) 
    
        # storing the values of diagonal row elements  
        for j in range(0,n): 
            temp[j] = mat[i][j] 
           
        #traversing every row below the diagonal element 
        for j in range(i+1,n): 
            num1 = temp[i]     # value of diagonal element 
            num2 = mat[j][i]   # value of next row element 
  
              
            for k in range(0,n): 
                 mat[j][k] = (num1*mat[j][k]) - (num2*temp[k]) 
  
            total = total * num1  
  
    #mulitplying the diagonal elements to get determinant 
    for i in range(0,n): 
         det = det*mat[i][i] 
  
  
    return int(det/total) #Det(kA)/k=Det(A);   
  

