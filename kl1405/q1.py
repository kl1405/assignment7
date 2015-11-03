import numpy as np

def q1():

    # create the array 
    array_q1=np.arange(1,16).reshape(3, 5).T
    #3 rows and 5 colums with the first row being 1,2,3,4,5 and then transpose
    print array_q1 
    
    def question1a():
        # contain the 2nd and 4th rows
        array_q1a=array_q1[[1,3],:]
        
        print 'a) 2nd and 4th rows'
        print array_q1a
    def question1b():
        # contain the 2nd colunm
        array_q1b=array_q1[:,1]
        
        print 'b) an array that contains the 2nd column'
        print array_q1b
    def question1c():
        # choose the rectangel section
        array_q1c=array_q1[np.arange(1,4)]
        
        print 'c) new array that contains all the elements in the rectangular section between the coordinates[1,0] to [3,2]'      
        print array_q1c
    def question1d():
        # pick from 3 to 11
        array_q1d=np.array([i for i in array_q1.flat if 2<i<12])
        print 'd) elements between 3 and 11'
        print array_q1d
   # print all the arrays
    question1a()
    question1b()
    question1c()
    question1d()
if __name__ == '__main__':
    q1()