from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

# print(type(iris))

# print(type(iris['data']))

X_train, X_test, y_train, y_test = train_test_split(
    iris['data'],
    iris['target'],
    test_size = 0.3,
    shuffle = True,
    stratify = iris.target,
    random_state= 42    
)

lr = LogisticRegression()
lr.fit(X_train, y_train)

pred = lr.predict(X_test)
print(pred)

accuracy = accuracy_score(y_test, pred)
print(accuracy)

prob = lr.predict_proba(X_test)
print(prob)