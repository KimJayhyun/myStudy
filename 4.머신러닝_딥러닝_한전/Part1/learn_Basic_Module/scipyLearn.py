# scipy에서 scikit-learn 알고리즘을 구현할 때
# 많이 사용하는 모듈은 scipy.sparse이다.
# 이 떄, 희소 행렬기능은 주요 기능 중의 하나이다.
# 희소 행렬(sparse matrix) : 0을 많이 포함한 2차원 배열?



import numpy as np
from scipy import sparse

b1 = np.eye(4, dtype= int)
print(b1)

# sparse.csr_matrix()
# Compressed Sparse Row, Compress Row Storage
# 행의 인덱스를 저장해서 압축
sparse_matrix = sparse.csr_matrix(b1)
print(sparse_matrix)


b2 = np.eye(5, k = - 1, dtype=int)
print(b2)

sparse_matrix = sparse.csr_matrix(b2)
print(sparse_matrix)

b3 = np.arange(16).reshape(4,4)
print(b3)

x = np.diag(b3)
print(x)

y = np.diag(x)
print(y)

sparse_matrix = sparse.csr_matrix(y)
print(sparse_matrix)

# 희소행렬을 직접 만들 때 사용하는 포멧
# COO 포멧 (Coordinate 포멧)
print()
data = np.ones(4)
print(data)

row_indeices = np.arange(4)
col_indices = np.arange(4)

eye_coo = sparse.coo_matrix((data, (row_indeices, col_indices)))

print(eye_coo)