from sklearn import svm

xor_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

# 주어진 데이터 분리한다.
# 학습 데이터와 레이블을 분리

train_data = []
label = []

for row in xor_data:
    p = row[0]
    q = row[1]
    res = row[2]

    train_data.append([p,q])
    label.append(res)

# SVM 알고리즘을 사용하는 머신러닝 객체를 만든다. 
# SVM : 분류 and 회귀 가능
# SVC : Classifier
# SVR : Regression
clf = svm.SVC()

# fit() Method : 학습기계에 데이터를 학습시킨다.
clf.fit(train_data, label)

# predic() Method : 학습데이터를 이용한 예측 
pre = clf.predict(train_data)
print("예측 결과", pre)


ok = 0
total = 0

for idx, answer in enumerate(label):
    p = pre[idx]
    
    if p == answer:
        ok += 1

    total += 1


print('정확도', ok , "/", total)







