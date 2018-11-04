import  numpy as np
print("Non linear transport dynamics calculator. Momentum? (M)")
whatToDo = input()
if whatToDo == "M":
	# A force is acting on a body at point P {F}^T = [Fx,Fy,Fz]. The point is desribed in vectors
	# {rp}^T=[rpx,rpy,rpz]. Force {F} if momentum {M} is equal: {M}={rp}x{F}=[rp]{F}
	#Point P vectors:
	rx = int(input())
	ry = int(input())
	rz = int(input())
	r = np.matrix([[rx],[ry],[rz]])
	r_asymetric = np.matrix([[0,-rz,ry], [rz,0,-rx],[-ry,rx,0]])
	#Force F^T:
	Fx = int(input())
	Fy = int(input())
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
