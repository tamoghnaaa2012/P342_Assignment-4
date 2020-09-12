#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def partial_pivot(m,v):
    n = len(m)
    for i in range (n-1):
        if m[i][i] ==0:
            for j in range (i+1,n):
                if abs(m[j][i])> abs(m[i][i]):
                    m[i],m[j] = m[j],m[i]
                    v[i],v[j] = v[j],v[i]
                
    return (m,v)


def luDecomposition(A,b):
    
    n = len(A)
    
    # (1) Extract the b vector
    #b = [0 for i in range(n)]
    #for i in range(0,n):
    #    b[i]=A[i][n]
    
    
    L=[[0.0]*n for i in range(n)]
    U=[[0.0]*n for i in range(n)]
    
    
    #create the pivot matrix P and the multiplied matrix PA
    
    partial_pivot(A,b)
    #PA = matrix_mult(P,A)
    
    #perform the LU decomposition
    
    
    for i in range(n):
        for k in range(i,n):
            sum=0
            for j in range(i):
                sum += (L[i][j]*U[j][k])
           #Evaluating U(i,k)    
            U[i][k]= A[i][k]-sum
                
                
        for k in range(i,n):
            if(i==k):
                L[i][i]=1  #diagonal as 1
            else:
                sum=0
                for j in range(i):
                    sum +=(L[k][j]*U[j][i])
                        
                L[k][i] = ((A[k][i]- sum)/U[i][i])
                
                
                
    return(L,U) 

def forward_sub(L,b):
    
    n = len(L)
    y= [[0*n] for i in range(n)]       #range(start, stop, step)
    for i in range(n):
        sum = 0
        for j in range(i):
            sum = sum + L[i][j]*y[j]
            
        y[i]=(b[i][0]-sum)/L[i][i]   
        
    return(y)

def back_sub(U,y):
    
    
    n = len(U)
    # (6) Perform substitution Ux=y
    x =[0]*n
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            y[i] = y[i]-U[i][j]*x[j]
        x[i]= y[i]/U[i][i]    
                                 

    return (x)

