import pandas as pd
from sklearn import svm, metrics

# XOR 연산 데이터

input_Data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

xor_df = pd.DataFrame(input_Data)

# 학습데이터, label 분류

train_Data = xor_df.loc[:, 0:1]
label = xor_df.loc[:, 2]

# print(train_Data)
# print(label)

# 데이터 학습

clf = svm.SVC()
clf.fit(train_Data, label)

# 데이터 예측

pre = clf.predict(train_Data)

# 정확도 측정(정답률 확인)
# metrics 모듈에 accuracy_score() 사용

accuracy = metrics.accuracy_score(label, pre)
print(accuracy)





