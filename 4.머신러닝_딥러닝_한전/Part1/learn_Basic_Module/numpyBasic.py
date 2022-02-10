import numpy as np

## h1 = np.zeros(10)
## h2 = np.ones(10)
## h3 = np.ones((5,5))

# print(h1)
# print(h2)
# print(h3)

## numpy에서 특수행렬을 만드는 함수
## eye(N, M=, k=, dtype) : 항등행렬
##    row, column, 대각 위치, data type

# a = np.eye(3,4,  k = 1)
# print(a)

## diag() 함수는 정방행렬에서 대각 요소만 추출하여 벡터를 만든다
## diag(y, k=) : k 대각의 위치

## diag() 함수는 벡터요소를 대각요소로하는 정방행렬을 만들어준다

x = np.arange(9).reshape(3, 3)

y = np.diag(x)

print(x)
print(y)

y = np.diag(x, k= -1)
print(y)

z = np.diag(y)

print(z)
