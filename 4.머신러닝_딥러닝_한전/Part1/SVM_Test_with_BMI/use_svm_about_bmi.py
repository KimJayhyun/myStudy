import os
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

csvPath = os.getcwd()
csvPath += '\\머신러닝_딥러닝\\Part1\\SVM_Test_with_BMI\\bmi.csv'

csv = pd.read_csv(csvPath)


label = csv['label']

h = csv.height / 200
w = csv['weight'] / 100

data = pd.concat([h, w], axis= 1)

X_train, X_test, y_train, y_test = train_test_split(data, label)

clf = svm.SVC()
clf.fit(X_train, y_train)

y_predict = clf.predict(X_test)

ac_score = metrics.accuracy_score(y_test, y_predict)

print(ac_score)



