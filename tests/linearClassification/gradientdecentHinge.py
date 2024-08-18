import numpy as np
trainExamples =[
    # x y pairs
    ((0,2),1),
    ((-2,0),1),
    ((1,-1),-1)
]

def phi(x):
    return np.array(x)

def initialWeightVector():
    return np.zeros(2)

def trainLoss(w):
    return 1.0/len(trainExamples)*sum(max(1 - w.dot(phi(x))*y , 0 ) for x,y in trainExamples)

def gradentTrainLoss(w):
    return 1.0/len(trainExamples)*sum(-phi(x) * y if 1 - w.dot(phi(x))*y >0 else 0 for x,y in trainExamples)

def gradientDecent(trainLoss,gradentTrainLossF,initialWeightvector):
    w=initialWeightVector()
    eta=0.1
    for t in range (500):
        value=trainLoss(w)
        gradient=gradentTrainLoss(w)
        w=w-eta*gradient
        print(f'epoch {t}: w {w},F{w}= {value} ,gradientD={gradient}')

gradientDecent(trainLoss,gradentTrainLoss,initialWeightVector)
