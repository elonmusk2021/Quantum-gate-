import numpy as np
from gate import X,Z,H,ket_i,ket_j
# bit_flip
def bit_flip(state, min_p=0 , max_p=1):
    p=np.random.uniform(min_p,max_p)
    rand_value=np.random.rand()
    flipped = rand_value<p
    if flipped:
        return np.dot(X,state),"flip happened"
    return state,'No flip'

#phase flip 
def phase_flip(state, min_p=0 , max_p=1):
    p=np.random.uniform(min_p,max_p)
    rand_value=np.random.rand()
    flipped = rand_value<p
    if flipped:
        return np.dot(Z,state),"flip happened"
    return state,'No flip'

state = ket_i
for _ in range(5):  
    noisy_state, status = phase_flip(state)
    print('After noise:\n', noisy_state)
    print('Status:', status)
    print("-" * 30)    