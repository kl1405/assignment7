import matplotlib.pyplot as plt
import numpy as np

def q4():
    

    # a. Construct a grid with meshgrid
    # reference: http://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html
    nx,ny = (1000,1000)
    x = np.linspace(-2,1,nx)
    y = np.linspace(-1.5,1.5,ny)
    xv, yv = np.meshgrid(x,y)
    
    # b. iteration
    N_max = 50
    some_threshold = 50
    c = xv + 1j*yv
    z = c
    for v in range(N_max):
        z = z**2 + c

    # c. Form a 2D boolean mask indicating which points are in the set
    mask = (np.abs(z) < some_threshold)

    #save result to an image with: 
    plt.imshow(mask.T, extent=[-2,1,-1.5,1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')

