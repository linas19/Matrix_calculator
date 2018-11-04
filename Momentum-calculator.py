import  numpy as np
print("Momentum calculator:")
# A force is acting on a body at point P {F}^T = [Fx,Fy,Fz]. The point is desribed in vectors
# {rp}^T=[rpx,rpy,rpz]. Force {F} if momentum {M} is equal: {M}={rp}x{F}=[rp]{F}
#Point P vectors:
print("rx vector")
rx = int(input())
print("ry vector")
ry = int(input())
print("rz vector")
rz = int(input())
r = np.matrix([[rx],[ry],[rz]])
r_asymetric = np.matrix([[0,-rz,ry], [rz,0,-rx],[-ry,rx,0]])
#Force F^T:
print("Fx vector")
Fx = int(input())
print("Fy vector")
Fy = int(input())
print("Fz vector")
Fz = int(input())
FT = np.matrix([[Fx,Fy,Fz]])
F = np.matrix([[Fx], [Fy], [Fz]])
#Momentum {M}={rp}x{F}=[rp]{F}:
M = r_asymetric * F
print(M)

# print("Input for x, y, z")

# x = int(input())
# y = int(input())
# z = int(input())

# antisymetric_matrix = np.matrix([[0,-z,y], [z,0,-x],[y,x,0]])
# print(antisymetric_matrix)
# x1 = int(2)
# y1 = int(4)

# a = np.matrix([[1,1,x1], [2,2,3], [4,5,6]])
# b = np.matrix([[2,2,y],[2,3,4],[4,5,6]])

# c = a * b - b
# print(c)
# print(antisymetric_matrix)
