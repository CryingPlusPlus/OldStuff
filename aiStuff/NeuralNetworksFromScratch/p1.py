import random
import numpy as np
# inputs = [1, 2, 3, 2.5] # inputs halt 
# weights1 = [random.uniform(0,1) for i in range(4)] # weight von connection
# weights2 = [random.uniform(0,1) for i in range(4)] # weight von connection
# weights3 = [random.uniform(0,1) for i in range(4)] # weight von connection
# bias1 = 2 # jedes Neuron hat ein bias
# bias2 = 4 # jedes Neuron hat ein bias
# bias3 = 3 # jedes Neuron hat ein bias

inputs = [[random.uniform(0,1) for i in range(4)] for i in range(3)]
weights = [[random.uniform(0,1) for i in range(4)] for i in range(3)]
biases = [random.uniform(0,1) for i in range(3)]

weights1 = [[random.uniform(0,1) for i in range(3)] for i in range(3)]
biases1 = [random.uniform(0,1) for i in range(3)]

# output = [
        # inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1,
        # inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2,
        # inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] + bias3
        # ] 
# print(output)

l_output = np.dot(inputs, np.array(weights).T) + biases # immer zuerst die weights beim dotproduct -> iteriert durch die matrix gibt error weil es nicht durch einen verktor iterieren kann 
l1_output = np.dot(l_output, np.array(weights1).T) + biases1 #
# batch size = 32 ca....
# print(output)
print(l_output)
print(l1_output)

