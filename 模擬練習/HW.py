from gate import X, I
import numpy as np
from scipy.linalg import expm

def Ry(theta):
    return np.array([[np.cos(theta / 2), -np.sin(theta / 2)],
                     [np.sin(theta / 2), np.cos(theta / 2)]])

def tprod(A, B, C):
    return np.kron(np.kron(A, B), C)

def C_U(n, control, target, U):
    size = 2**n
    CU = np.eye(size, dtype=complex)
    for i in range(size):
        bin_str = format(i, f'0{n}b')
        if bin_str[control] == '1':
            j = i ^ (1 << (n - 1 - target))  # 調整為從左到右的量子位索引
            CU[i, i] = U[0, 0]
            CU[i, j] = U[0, 1]
            CU[j, i] = U[1, 0]
            CU[j, j] = U[1, 1]
    return CU

n = 4

# 定義基本閘
R = tprod(I, I, Ry(np.pi / n))
Ri = tprod(I, I, Ry(-np.pi / n))
CX12 = C_U(3, 1, 2, X)
CX02 = C_U(3, 0, 2, X)

# 組合電路
circuit = R @ CX12 @ R @ CX02 @ Ri @ CX12 @ Ri

# 托福利閘
size = 8
I_3 = np.eye(size)
P_11 = np.zeros((4, 4))
P_11[3, 3] = 1  # |11> 前兩個量子位
P11_I = np.kron(P_11, I)
P11_X = np.kron(P_11, X)
Toff = I_3 - P11_I + P11_X

# 相位因子
P_100 = np.zeros((8, 8))
P_100[4, 4] = 1  # |100>
Phase = I_3 - 2 * P_100

# 驗證
adjusted_circuit = Phase @ circuit
difference = np.allclose(adjusted_circuit, Toff, atol=1e-10)
print("Circuit matches Toffoli up to phase factor:", difference)

if not difference:
    print("Adjusted Circuit:\n", adjusted_circuit)
    print("Toffoli:\n", Toff)
    print("Difference:\n", adjusted_circuit - Toff)