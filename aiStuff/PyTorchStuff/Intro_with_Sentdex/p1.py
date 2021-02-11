import torch

x = torch.Tensor([5, 3])
y = torch.Tensor([2, 1])

# a tensor ist ein vieldimensionaler vektor

x = torch.zeros([2, 5])
print(x, x.shape)
print('\n')

y = torch.rand([2, 5])
print('y =', y)

y = y.view([1,10]) #reshape = view
print('y =', y)
print('\n')


