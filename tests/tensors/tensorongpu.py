import torch
import numpy as np

if torch.cuda.is_available() :
    print ("Run on GPU")
    device=torch.device("cuda")
    x=torch.ones(300,300,600,device=device) #send on device
    y=torch.ones(300,300,600)    
    y=y.to(device)                            # same on device 
    z=x+y                                     #executed on GPU
else:
    print("Run on CPU")
    x=torch.ones(300,300,6000) #send on device
    y=torch.ones(300,300,6000)
    z=x+y 