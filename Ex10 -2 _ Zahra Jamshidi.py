import numpy as np
import matplotlib.pyplot as plt
vec1=np.array([-1,4,-9])
mat1=np.array([[1,3,5],[7,-9,2],[4,6,8]])
vec2=(np.pi/4)*vec1
vec2=np.cos(vec2)
vec3=vec1+2*vec2
vec4=mat1+vec3
print(mat1)
print(mat1.transpose())
print(round(np.linalg.det(mat1)))
print(mat1.trace())
print(vec1.min())
print(np.where(vec1==vec1.min()))
print(mat1.min())
A=np.array([[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]])
if A.sum(axis=0).max()==A.sum(axis=0).min()==A.sum(axis=1).min()==A.sum(axis=1).max()==A.sum(axis=1).min()==sum(np.diagonal(A))==sum(np.diagonal(A))==sum(np.fliplr(A).diagonal()):
    print("Magic")
else:
    print("Not Magic")
M=np.random.rand(10,10)
MUL=M[0:5,0:5]
MUR=M[0:5,5:10]
MLL=M[5:10,0:5]
MLR=M[5:10,5:10]
