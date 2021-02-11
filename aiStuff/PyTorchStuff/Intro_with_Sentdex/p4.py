import torch.optim as optim
import random
import torch #data sachen -> großteil von ML sachen allda
import torchvision
from torchvision import transforms, datasets
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.nn.functional as F

# man möchte immer test und train data teilen, damit man die AI mit sachen testen kann, an die es sich noch nicht 'gewöhnt' hat

train = datasets.MNIST('', train=True, download=True, transform=transforms.Compose([transforms.ToTensor()]))

test = datasets.MNIST('', train=False, download=True, transform=transforms.Compose([transforms.ToTensor()]))

trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
testset = torch.utils.data.DataLoader(test, batch_size=10, shuffle=True)

class Net(nn.Module): # inherit from nn.Module
    def __init__(self):
        super().__init__() # ... damit sich auch die elternklasse initialisiert
        self.fc1 = nn.Linear(28 * 28, 64) #28*28 -> input... das andere outputneuronen nnLinear = dense Layer
        self.fc2 = nn.Linear(64,64)
        self.fc3 = nn.Linear(64,64)
        self.fc4 = nn.Linear(64,10)

    def forward(self, X):
        X = F.relu(self.fc1(X))
        X = F.relu(self.fc2(X))
        X = F.relu(self.fc3(X))
        X = self.fc4(X)
        
        return F.log_softmax(X, dim=1) #softmax -> output ist dann [0,0,0,1,0,0]... er nimmt die höchste zahl und macht sie eins und die anderen 0
    

# X = torch.rand((28, 28))
# X = X.view(-1, 28 * 28)
net = Net()
optimizer = optim.Adam(net.parameters(), lr=1e-3)


#loss -> wie falsch ist das model? 
#optimizer -> passt die Werte aufgrund von loss an... also weights and biases  

EPOCHS = 3

for epoch in range(EPOCHS):
    for data in trainset:
        # data is a batch if features and labels
        X, y = data
        net.zero_grad()
        output = net(X.view(-1, 28*28))
        loss = F.nll_loss(output, y)
        loss.backward()
        optimizer.step()
    print(loss)

correct = 0
total = 0

with torch.no_grad():
    for data in testset:
        X, y = data
        output = net(X.view(-1, 28**2))
        for idx, i in enumerate(output):
            if torch.argmax(i) == y[idx]:
                correct += 1
            total += 1

print('Acc: ', correct/total *100, '%')
# model.train()" and "model.eval()" activates and deactivates Dropout and BatchNorm, so it is quite important. "with torch.no_grad()" only deactivates gradient calculations, but doesn't turn off Dropout and BatchNorm. Your model accuracy will therefore be lower if you don't use model.eval() when evaluating the model.
