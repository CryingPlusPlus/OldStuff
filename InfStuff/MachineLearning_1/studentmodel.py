import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style


data = pd.read_csv("student-mat.csv", sep=";")  # get data from csv seperator = ;

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]  # runtertrimmen der daten auf das was wir wollen

predict = "G3"  # das was wir predicten wollen wird auch label genannt

X = np.array(data.drop([predict], 1))  # Features; Input
Y = np.array(data[predict])  # Labels; Output

#while True:
#    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)
#    linear = linear_model.LinearRegression()
#    linear.fit(x_train, y_train)
#    acc = linear.score(x_test, y_test)
#    print(acc)
#    if acc > 0.97:
#        with open('studentmodel.pickle', 'wb') as f:
#            pickle.dump(linear, f)
#            print('pickled')
#            break

pickle_in = open('studentmodel.pickle', 'rb')
linear = pickle.load(pickle_in)
pickle_in.close()

#acc = linear.score(x_test, y_test)
#print(acc)
print('\n')
style.use('ggplot')
pyplot.scatter(data['G1'], data['G3'])
pyplot.xlabel('G1')
pyplot.ylabel('Final Grade')
pyplot.show()
