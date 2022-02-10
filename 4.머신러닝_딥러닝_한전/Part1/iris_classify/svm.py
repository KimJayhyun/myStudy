from sklearn import svm, metrics
import random, re
import os

csvPath = os.getcwd()
csvPath += '\\머신러닝_딥러닝\\Part1\\iris_classify\\tableconvert_csv_b8zx66.csv'

# 붓꽃의 데이터를 읽기
csv = []

with open(csvPath, 'r', encoding= 'utf-8') as fp:
    for line in fp:
        
        line = line.strip()
        cols = line.split(',')
        
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n        

        cols = list(map(fn, cols))
        csv.append(cols)
# 헤더 제거
del csv[0]

# shuffling csv
random.shuffle(csv)

# train, test data 구분
total_len = len(csv)
train_len = int(total_len * 2 / 3)


train_data =[]
train_label = []

test_data = []
test_label = []

for i in range(total_len):
    data = csv[i][:4]
    label = csv[i][4]

    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else :
        test_data.append(data)
        test_label.append(label)


clf = svm.SVC()

# 학습 시키기
clf.fit(train_data, train_label)

# 테스트
predict = clf.predict(test_data)

# 정확도
ac_score = metrics.accuracy_score(test_label, predict)

print(total_len)
print(ac_score)







    








