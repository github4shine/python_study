import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import datasets
iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.7, random_state=0)
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
score = clf.score(X_test, y_test)
print(score)
