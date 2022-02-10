# 대표적인 분류 알고리즘 
# SVM, KNN
# KNN : K-Nearest Neighbors 
# Input과 Distance가 가장 가까운 K 개의 학습 데이터를 찾고 그 학습 데이터의 label을 활용
import random
import numpy as np
from sklearn.datasets import load_iris
iris_Data = load_iris()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_Data['data'], iris_Data['target'], random_state = 0)

# KNN을 사용하기 위해서는 neighbors 모듈의 KNeighborsClassifier 함수를 사용
# KNeighborsClassifier()의 중요한 parameter는 n_neighobrs이고 K를 설정한다.

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

# 훈련 데이터셋을 가지고 모델을 만들려면 fit Method를 사용한다.
# fit Method의 return은 knn 객체를 retrun한다.

knn.fit(X_train, y_train)

# 다음 np 객체를 채집한 붓꽃의 새로운 Data라고 가정
# scikit-learn에서는 항상 데이터가 2차원 배열이라고 예측

import random
a = [random.uniform(4, 6), random.uniform(2,4), random.uniform(1,3), random.uniform(0,2)]
X_newData = np.array(
    [ list(map(lambda x : round(x, 1), a)) ]
    )

print(X_newData)
print()

prediction = knn.predict(X_newData)
print(prediction)

print(iris_Data['target_names'][prediction])

y_predict = knn.predict(X_test)

# 정확도 계산하기 위해서 numpy의 mean() Method를 이용
# knn객체의 score() Method를 사용

print(np.mean(y_predict == y_test))


