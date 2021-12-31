from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import numpy as np

# X = np.array([x for x in range(0, 11)])
X_plot = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

X = X_plot.reshape(-1, 1)
y = np.array([13, 25, 34, 47, 59, 62, 79, 88, 90, 100])

## train_test_split 
# train, test Data 임의로 나눠줌
# https://rfriend.tistory.com/519
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
# print(X_test)
# print(predictions)

plt.plot(X_plot, y, "r--")
plt.plot(X_test, y_test, "g-")
plt.show()
