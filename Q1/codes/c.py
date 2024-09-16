from ctypes import *
c = CDLL('./c.so')
c.sqr.argtypes = [c_float]
c.sqr.restype = c_float

c.d1.argtypes = [c_float, c_float]
c.d1.restype = c_float

c.ratio.argtypes = [c_float, c_float]
c.ratio.restype = c_float

x1 = -2
y1 = -6
x2 = 7
y2 = -14

n1 = c.d1(c_float(x1), c_float(y1))
n2 = c.d1(c_float(x2), c_float(y2))
r = c.ratio(c_float(n1), c_float(n2))

print("D1 =", n1)
print("D2 =", n2)
print("Ratio =", r)

