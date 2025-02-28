import numpy as np

def cartesian_to_polar(x, y):
    """直角座標 (x, y) 轉換為極座標 (r, θ)"""
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)  # arctan2(y, x) 計算角度
    return r, theta

def polar_to_cartesian(r, theta):
    """極座標 (r, θ) 轉換為直角座標 (x, y)"""
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def cartesian_to_spherical(x, y, z):
    """直角座標 (x, y, z) 轉換為球座標 (r, θ, φ)"""
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z / r) if r != 0 else 0  # θ: 夾角 (0 到 π)
    phi = np.arctan2(y, x)  # φ: 方位角 (-π 到 π)
    return r, theta, phi

def spherical_to_cartesian(r, theta, phi):
    """球座標 (r, θ, φ) 轉換為直角座標 (x, y, z)"""
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z