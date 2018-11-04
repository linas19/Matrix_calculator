import  numpy as np
print("Non linear transport dynamics calculator. Momentum? (M)")
whatToDo = input()
if whatToDo == "M":
	# Kuna veikia taske P jega {F}^T = [Fx,Fy,Fz]. Tasko padeti apibrezia vektorius
	# {rp}^T=[rpx,rpy,rpz]. Jegos {F} jegu momentas {M} lygus: {M}={rp}x{F}=[rp]{F}
	#Tasko P padeties vektoriai:
	rx = int(input())
	ry = int(input())
	rz = int(input())
	r = np.matrix([[rx],[ry],[rz]])
	r_asymetric = np.matrix([[0,-rz,ry], [rz,0,-rx],[-ry,rx,0]])
	#Jega F^T:
	Fx = int(input())
	Fy = int(input())
	Fz = int(input())
	FT = np.matrix([[Fx,Fy,Fz]])
	F = np.matrix([[Fx], [Fy], [Fz]])
	#Jegu momentas {M}={rp}x{F}=[rp]{F}:
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
