from ctypes import *
c = CDLL('./c.so')

c.d1.argtypes = [c_float, c_float]
c.d1.restype = c_float

a = 6 
b = 8

n1 = c.d1(c_float(a), c_float(b))

print("length of side C =", n1)


