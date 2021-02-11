#%%
import random
from time import time

def timer(f):
    def inner():
        a = time()
        f()
        b = time()
        print('Time needed:', b - a)
    return inner

#%%
@timer
def makeListe():
    [random.randint(0, 1000) for _ in range(int(10e4))]

makeListe()
makeListe()

#%%
#this is a Variable
a = "Hello"
b = "Wolrd"
print(a, b)
# %%
class World:
    def __init__(self, Message="Hello World"):
        self.Message = Message
    def __call__(self, *args, **kwargs):
        print(self.Message, *args, **kwargs)

w = World("Hello World2")
w
h = (("Hello World"), "Python is dynamicly typed")
print(h[0], h[1])
