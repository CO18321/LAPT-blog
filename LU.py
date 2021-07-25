# LU decomposition
from numpy import array
from scipy.linalg import lu

# define a square matrix of 3x3
A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)

P, L, U = lu(A)

print(P)
print(L)
print(U)

# reconstruct
B = P.dot(L).dot(U)
print(B)


