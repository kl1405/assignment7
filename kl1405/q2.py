from numpy import *
def q2():
    # given the array: an array 0~24 and shaped 5*5
    a = arange(25).reshape(5,5)

    b = array([1., 5, 10, 15, 20])

    #reshape array b to a 5*1 array
    b = b.reshape(5,1)
    #divide each column element of a with reshaped b array
    array_q2 = divide(a,b)
    
    print 'divides each column element of a with b'
    print array_q2
 

if __name__ == '__main__':
    q2()