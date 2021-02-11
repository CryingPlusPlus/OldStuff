import random
import math
import pickle

class DenseLayer:
    def __init__(self, inputs, neurons):
        self.n_inputs = inputs
        self.n_neurons = neurons
        self.weights = [[random.uniform(-1, 1) for j in range(self.n_inputs)] for i in range(self.n_neurons)] 
        self.biases = [random.uniform(-1, 1) for i in range(self.n_neurons)]
    
    def forward(self, X):
        X = [sum(X[i] * self.weights[k][i] for i in range(len(X))) + self.biases[k] for k in range(self.n_neurons)]
        return X


class NN:
    def __init__(self, n_inputs, hidden, n_outputs):
        self.form = [n_inputs] + hidden + [n_outputs]
        self.layers = [DenseLayer(self.form[i - 1], self.form[i]) for i in range(1, len(self.form))]

    def forward(self, X):
        for layer in self.layers:
            X = self.relu(layer.forward(X))
        return X

    def relu(self, X):
        # if X > 0:
            # return X
        # else:
            # return 0
        return [Xs if Xs > 0 else 0 for Xs in X]

    def train(self, training_data):
        # error = [data[1] - self.forward(data[0]) for data in training_data]
        for tSet in training_data:
            X, y = tSet
            yTest = self.forward(X)
            error = [y[i] - yTest[i] for i in range(len(y))]


training_data = [
        [[0], [math.sin(0)]],
        [[2], [math.sin(2)]]
        ]

myNN =  NN(1, [7, 7], 1)
# test -> sinus finktion modellieren danach erst MNIST
