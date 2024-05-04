import torch 
print ("Checking Cuda Available")
print(torch.cuda.is_available())
print ("Checking GPU count")
if torch.cuda.device_count() == 1 :
    print ("GPU exists")
    print ("Checking GPU NAME")
    torch.cuda.current_device()
    print (torch.cuda.get_device_name(0))
    print ("All Good !!")
else : 
    print ("GPU Check Failed")

