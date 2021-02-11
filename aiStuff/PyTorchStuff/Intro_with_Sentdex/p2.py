import torch #data sachen -> großteil von ML sachen allda
import torchvision
from torchvision import transforms, datasets
import matplotlib.pyplot as plt

# man möchte immer test und train data teilen, damit man die AI mit sachen testen kann, an die es sich noch nicht 'gewöhnt' hat

train = datasets.MNIST('', train=True, download=True, transform=transforms.Compose([transforms.ToTensor()]))

test = datasets.MNIST('', train=False, download=True, transform=transforms.Compose([transforms.ToTensor()]))

trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
testset = torch.utils.data.DataLoader(test, batch_size=10, shuffle=True)

for data in trainset:
    # print(data)
    break

x, y = data[0][0], data[1][0]

plt.imshow(x.view(28, 28))
plt.show()
print(x.shape)
# training Data sollte balanced sein -> sonst kann es zu verwirrungen führen.
