import torch
import numpy as np
a=torch.ones(5)
print(a)
b=a.numpy()
print(type(b))
a.add_(1)
c=torch.from_numpy(b)

print(a)
print(b)
print(c)