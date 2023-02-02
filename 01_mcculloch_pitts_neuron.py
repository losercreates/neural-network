import numpy as np

class Neuron:
    def __init__(self, weights):
        self.weights = weights
        n = len(weights)
        self.threshold = np.dot(np.ones(n), weights)

    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs)
        return 1 if total >= self.threshold else 0

num_of_inputs = int(input("Enter number of inputs: "))
weights = np.ones(num_of_inputs)
neuron = Neuron(weights)

print("Enter the inputs (each in a newline) in the form of 1 or 0: ")
lst=[]
i=0
while(i<num_of_inputs):
    ele = int(input())
    if ele not in [1,0]:
        print("Please enter 1 or 0")
        continue
    lst.append(ele)
    i+=1
inputs=np.array(lst)
print("The AND operation on the following inputs is: ")
print(neuron.feedforward(inputs))