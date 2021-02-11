# kernals sind funktionen die eine höhere dimension eines punktes berechnen -> solange machen bis klassen entstanden
# sind in die man hyperplanes zeichnen kan
# SVM Soppurt Vector Machine
#SVMC Support Vector Machine Classification
#SVM ist zwar schwieriger zu initialiseiren aber sit meist besser als Kneighbors

import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics

cancer = datasets.load_breast_cancer()

X = cancer.data
Y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1) # splitting data into train and test data
classes = ['malignant', 'benign']

clf = svm.SVC(kernel='linear', C=2)

clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

acc = metrics.accuracy_score(y_test, y_pred)

print (acc)