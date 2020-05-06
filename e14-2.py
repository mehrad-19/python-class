import numpy as np
import matplotlib.pyplot as plt
vec1 = np.array([-1,4,-9])
mat1 = np.array([[1,3,5],[7,-9,2],[4,6,8]])
vec2=(np.pi/4)*vec1
vec3=np.cos(vec1)
vec4=vec1+2*vec2
vec5=np.matrix(mat1)*np.matrix(vec4)

transpose=np.transpose(mat1)

det=np.linalg.det(mat1)

Trace=np.trace(mat1)

minimum=np.min(vec1)

position_of_smallest = np.argmin(vec1)

minimum=np.min(mat1)

A=np.array([[17,24,1,8,15],
            [23,5,7,14,16],
            [4,6,13,20,22],
            [11,18,25,2,9]])
B=np.sum(A,axis=0)
C=np.sum(A,axis=1)

B_min=B.min(axis=0)
B_max=B.max(axis=0)
c_min=C.min(axis=0)
c_max=C.max(axis=0)

A_diag=np.diag(A)
A_diag_sum=np.sum(A_diag)

A_flip=np.fliplr(A)
A_flip_diag=np.sum(A_flip)


if B_min==B_max==c_min==c_max==A_diag_sum==A_flip_diag:
    print("True") 
