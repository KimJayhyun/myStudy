import numpy as np

X = np.array([i for i in range(10)])

print(X.shape)

y = X.reshape(-1, 1)

print(y.shape)