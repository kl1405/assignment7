import math
from numpy import *
def q3():
    print'question 3'
    
    # generate a array which from 0 to 1 and 10*3 matrices
    
    array_q3=random.rand(10,3)#uniform random numbers in [0,1]
    
  
    
    column_index=argsort(abs(array_q3-0.5))[:,0].flatten()
    row_index=arange(len(array_q3))
    new_array=array_q3[row_index,column_index]
    

    print 'use argsort and fancy index to find closest to 0.5'
    print new_array
    

if __name__ == '__main__':
    q3()