# Problems from page 29 of 'Matrices and Society'

import numpy as np
from numpy.linalg import inv

a = np.matrix( [[1,2],[3,4]] )
b = np.matrix( [[4,-2],[-3,1]] )
c = np.matrix( [[1,0],[0,-1],[2,2]] )
d = np.matrix( [[1,0,2],[2,-1,0]] )

print("Matrix a")
print(a)
print("Matrix b")
print(b)
print("Matrix c")
print(c)
print("Matrix d")
print(d)

print('a+b')
print(a+b)

print('a-b')
print(a-b)

print('a+c')
try:
    print(a+c)
except ValueError:
    print("You can't add a+c")

print('ab')
print(a*b)

print('ba')
print(b*a)

print('ac')
try:
    print(a*c)
except ValueError:
    print("Dimensions do not allow for multiplication")

print('ca')
try:
    print(c*a)
except ValueError:
    print("Dimensions do not allow for multiplication")

print('bd')
try:
    print(b*d)
except ValueError:
    print("Dimensions do not allow for multiplication")

print('db')
try:
    print(d*b)
except ValueError:
    print("Dimensions do not allow for multiplication")

print('cd')
try:
    print(c*d)
except ValueError:
    print("Dimensions do not allow for mulitplication")

print('dc')
try:
    print(d*c)
except ValueError:
    print("Dimensions do not allow for mulitplication")

print('abc')
try:
    print(a*b*c)
except ValueError:
    print("Dimensions do not allow for mulitplication")

print('abd')
try:
    print(a*b*d)
except ValueError:
    print("Dimensions do not allow for mulitplication")

print('\n')
ainv = inv(a)
binv = inv(b)
print('Inverse of a')
print(ainv)
print('\n')
print('Inverse of b')
print(binv)

