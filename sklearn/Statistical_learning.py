from sklearn import datasets

#load iris data
iris= datasets.load_iris()
data=iris.data
print(data.shape)

#load digits data
digits =datasets.load_digits()
print(digits.images.shape)

import matplotlib.pyplot as plt
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r) 
