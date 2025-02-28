import numpy as np

def SVD_dec(A):
    """手動計算奇異值分解 (SVD)"""
    
    
    AtA = A.T @ A
    eigenvalues_V, V = np.linalg.eig(AtA)  

    AAt = A @ A.T
    eigenvalues_U, U = np.linalg.eig(AAt)  

    singular_values = np.sqrt(np.abs(eigenvalues_V))

    m, n = A.shape
    Sigma = np.zeros((m, n))
    np.fill_diagonal(Sigma, singular_values)  

    
    sorted_indices = np.argsort(singular_values)[::-1]  # 降序排列

    # 只對 U 和 V 進行排序
    U = U[:, :len(sorted_indices)]  
    V = V[:, sorted_indices]  # 重新排列 V
    
    return U, Sigma, V.T  # V^T

# 測試
A = np.array([[1,2,3],[4,5,1]])
U, Sigma, Vt = SVD_dec(A)

print("U matrix:")
print(U)
print("\nS matrix:")
print(Sigma)
print("\nV^T matrix:")
print(Vt)
