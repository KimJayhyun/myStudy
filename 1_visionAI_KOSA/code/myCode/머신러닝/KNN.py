### KNN : K-Nearest Neighbor ###
### 새로운 Data가 주어졌을 때, 기존 Data 가운데 K 거리안에 있는 Data의 개수를 통하여 Classify하는 머신러닝 기법이다. ###
from sklearn.linear_model import KNeighborsClassifier

# 모델 학습
knn = KNeighborsClassifier()