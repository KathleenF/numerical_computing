import numpy as np
from numpy import *
from scipy import optimize

A = np.array([[-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, -1, 1, 0, 0, -1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, -1, 0, 0, -1, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, -1, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, -1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]])
            #[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

b = np.array([[-7669,],[-16680],[7593],[9358],[19929],[0],
              [0],[-15089],[-5136],[8080],[-5379],[4993]])#,[1000]])

A = np.array([[-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, -1, 1, 0, 0, -1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, -1, 0, 0, -1, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, -1, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, -1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],              
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

B = np.array([[-7669,],[-16680],[7593],[9358],[19929],[0],
              [0],[-15089],[-5136],[8080],[-5379],[4993],[13400],[3050],[4200],
              [1200],[2300]])

b = np.array([[-7669,],[-16680],[7593],[9358],[19929],[0],
              [0],[-15089],[-5136],[8080],[-5379],[4993]])

#dependent 4,9,10,15,16,17
c = np.linalg.lstsq(A,B)[0]


#print np.dot(A,c)
#c = c[0:12][:]



A = np.zeros((12,17))
A[0][0] = 1
A[1][0] = -1
A[1][1] = 1
A[2][1] = -1
A[2][2] = 1
A[3][2] = -1
A[0][3] = -1
A[4][3] = 1
A[1][4] = 1
A[5][4] = -1
A[2][5] = -1
A[6][5] = 1
A[3][6] = 1
A[7][6] = -1
A[4][7] = -1
A[5][7] = 1
A[5][8] = -1
A[6][8] = 1
A[6][9] = -1
A[7][9] = 1
A[4][10] = -1
A[8][10] = 1
A[5][11] = 1
A[9][11] = -1
A[6][12] = -1
A[10][12] = 1
A[7][13] = 1
A[11][13] = -1
A[8][14] = 1
A[9][14] = -1
A[9][15] = 1
A[10][15] = -1
A[10][16] = 1
A[11][16] = -1
#print A


x0 = np.array([[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]])
x0 = np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print x0.shape, A.shape, b.shape, x0.T.shape
def con1(x):
    return np.subtract(np.dot(A,x),b.squeeze())[0]
    
def con2(x):
    x = x.T
    return np.subtract(b,np.dot(A,x))

x = x0.T
c = c.T
print np.dot(c,x)
d = np.subtract(np.dot(A,x0),b.squeeze())[0]
print d


    
def opt(x):
    x = x.T
    return np.dot(c,x)

print optimize.fmin_cobyla(opt, x0, con1)

'''
#print c
x = np.dot(A,c)
d = c
for i in range(0,17):
    d[i][0] = d[i][0] + 11000
print c
#print c
#print d
#print np.dot(A,d), x




-1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
1 -1 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0
0 1 -1 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 -1 0 0 0 0 0 0 0 0 0 0
0 0 0 -1 0 0 0 1 0 0 1 0 0 0 0 0 0
0 0 0 0 1 0 0 -1 1 0 0 -1 0 0 0 0 0
0 0 0 0 0 -1 0 0 -1 1 0 0 1 0 0 0 0
0 0 0 0 0 0 1 0 0 -1 0 0 0 -1 0 0 0
0 0 0 0 0 0 0 0 0 0 -1 0 0 0 -1 0 0 
0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 -1 0 
0 0 0 0 0 0 0 0 0 0 0 0 -1 0 0 1 -1
0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1

-7669
-16680
7593
9358
19929
0
0
-15089
-5136
8080
-5379
4993
'''
