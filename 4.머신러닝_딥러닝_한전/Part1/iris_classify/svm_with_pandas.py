import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import os

# 데이터 읽어오기
csvPath = os.getcwd()
csvPath += '\\머신러닝_딥러닝\\Part1\\iris_classify\\tableconvert_csv_b8zx66.csv'

csv = pd.read_csv(csvPath)

# 데이터 분류
csv_data = csv[ ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
csv_label = csv.variety

# train, test data split
X_train, X_test, y_train, y_test = train_test_split(csv_data, csv_label)

# 데이터 학습
clf = svm.SVC()
clf.fit(X_train, y_train)
y_predict = clf.predict(X_test)


ac_score = metrics.accuracy_score(y_test, y_predict)

print(ac_score)
