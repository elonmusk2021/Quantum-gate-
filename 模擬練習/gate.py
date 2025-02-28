import numpy as np
import scipy as sc
from scipy.linalg import expm
# define  gate
X = np.array([[0,1],[1,0]])
Z = np.array([[1,0],[0,-1]])
Y = np.array([[0,-1j],[1j,0]])
H = (1/np.sqrt(2))*np.array([[1,1],[1,-1]])
S = np.array([[1,0],[0 ,1j]])
SW = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
I = np.array([[1,0],[0,1]])


#def operator
#rotate
def R_x(theta):
    return expm(-1j * (theta / 2) * X)

def R_y(theta):
    return expm


#define initial state 
ket_i=np.array([[0],[1]])
ket_j=np.array([[1],[0]])
def Bloch_vec(theta , phi):
    return np.array([[np.cos(phi)*np.sin(theta)],[np.sin(phi)*np.sin(theta)],[np.cos(theta)]])



