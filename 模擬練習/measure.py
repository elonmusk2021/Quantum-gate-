import numpy as np
from gate import X,Z,H,ket_i,ket_j
from collections import Counter
def measure(state):
    probabilities=np.abs(state.flatten())**2
    return np.random.choice([0,1], p=probabilities)

#prepare quantum state 
state = np.dot(H,ket_j)

results = [measure(state) for _ in range(1000)]
counts  = Counter(results)
print('measure result',counts)


