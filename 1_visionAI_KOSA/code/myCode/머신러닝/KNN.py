## 참고 자료
# https://hleecaster.com/ml-knn-classifier-example/

### KNN : K-Nearest Neighbor ###
### 새로운 Data가 주어졌을 때, 기존 Data 가운데 K 거리안에 있는 Data의 개수를 통하여 Classify하는 머신러닝 기법이다. ###
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

import random

# Test distance function
# [x, y, type]

dataset = [[2.7810836,2.550537003,0],
[1.465489372,2.362125076,0],
[3.396561688,4.400293529,0],
[1.38807019,1.850220317,0],
[3.06407232,3.005305973,0],
[7.627531214,2.759262235,1],
[5.332441248,2.088626775,1],
[6.922596716,1.77106367,1],
[8.675418651,-0.242068655,1],
[7.673756466,3.508563011,1]]

# X
X = []
for data in dataset:
    X.append(data[0:2])

# X = np.array(X).reshape(-1, 1)

# y
y = []
for data in dataset:
    y.append(data[2])

# y = np.array(y)

# # train_test_split


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 42, test_size= 0.3, shuffle=True)

# randomList = random.sample(range(10), 7)
# randomList.sort()

# X_train = []
# X_test = []
# y_train = []
# y_test = []

# for i in range(10):
#     if i in randomList:
#         X_train.append(X[i])
#         y_train.append(y[i])
#     else :
#         X_test.append(X[i])
#         y_test.append(y[i])



# print(X_train)

# 모델 학습
knn = KNeighborsClassifier(n_neighbors = 7)
knn.fit(X_train, y_train)

# for test in X_test: 
#     # test = np.array(test).reshape(-1, 1)
#     pred = knn.predict(test)
#     print(test, pred)

pred = knn.predict(X_test)
print(X_test)
print(pred)

accuracy = accuracy_score(y_test, pred)
print(accuracy)
