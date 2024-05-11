import torch
import numpy as np
x=torch.ones(3,3,3,dtype=torch.int)
y=torch.ones(3,3,3,dtype=torch.int)
print(x)
print(y)
x.add_(y)
print(x)