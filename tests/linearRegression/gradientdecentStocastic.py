import numpy as np
import math

## Should be able to recover this
trueW = np.array([1,2,3,4,5])

#reverse the function 
def generate ():
    x =np.random.rand(len(trueW))
    y=trueW.dot(x) + np.random.random()
    return (x,y)
    
trainExamples=[generate() for i in range(1000000)]

#trainExamples =[
#    (1,1),
#    (2,3),
#    (4,3)
#]

def phi(x):
    return np.array(x)

def initialWeightVector():
    return np.zeros(len(trueW))

def trainLoss(w):
    return 1.0/len(trainExamples)*sum((w.dot(phi(x))-y)**2 for x,y in trainExamples)

def gradentTrainLoss(w):
    return 1.0/len(trainExamples)*sum(2*(w.dot(phi(x))-y)*phi(x) for x,y in trainExamples)


def loss (w,i) :
    x,y=trainExamples[i]
    return (w.dot(phi(x))-y)**2

def gradientLoss(w,i) :
    x,y=trainExamples[i]
    return 2*(w.dot(phi(x))-y)*phi(x)

def stocasticGradientDecent(trainLoss,gradentTrainLoss,n,initialWeightvector):
    w=initialWeightVector()
    eta=0.1
    numUpdates=0
    for t in range (500):
        for i in range(n) :
            value=trainLoss(w,i)
            gradient=gradentTrainLoss(w,i)
            numUpdates +=1
            eta=1.0/math.sqrt(numUpdates)
            w=w-eta*gradient
        print(f'epoch {t}: w {w},F{w}= {value} ,gradientD={gradient}')

stocasticGradientDecent(loss,gradientLoss,len(trainExamples),initialWeightVector)
