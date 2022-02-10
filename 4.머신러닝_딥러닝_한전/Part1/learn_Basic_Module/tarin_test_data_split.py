from sklearn.datasets import load_iris
iris_Data = load_iris()


# 훈련 데이터와 테스트 데이터를 나누기 위한 함수
# train_test_split 모듈에 있는 train_test_split()
# train_test_split 모듈은 sklearn.model_selection
from sklearn.model_selection import train_test_split

# skit-learn에서 데이터는 대문자 X, 레이블은 소문자 y로 표기

X_train, X_test, y_train, y_test = train_test_split(iris_Data['data'], iris_Data['target'], random_state = 0)

# train_test_split의 retrun type은 numpy 배열

print(X_train.shape)
print(X_test.shape)