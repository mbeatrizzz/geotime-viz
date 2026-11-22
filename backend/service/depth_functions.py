# depth_functions.py
import numpy as np

def L2_depth(x, data):
    # Calcula a matriz de covariância
    cov = np.cov(np.transpose(data))

    if np.sum(np.isnan(cov)) == 0:
        det = np.linalg.det(cov)
        
        if det == 0 or det < 1e-8:  
            epsilon = 1e-8 
            cov += np.eye(cov.shape[0]) * epsilon
        
        sigma = np.linalg.inv(cov)
    else:
        sigma = np.eye(data.shape[1])

    # Calcula as profundidades
    depths = (-1) * np.ones(len(x))
    for i in range(len(x)):
        tmp1 = (x[i] - data)
        tmp2 = np.matmul(tmp1, sigma)
        tmp3 = np.sum(tmp2 * tmp1, axis=1)
        depths[i] = 1 / (1 + np.mean(np.sqrt(tmp3)))

    return depths

def spatial_depth(x, data):
    """Affine-invariant spatial depth (Eq. 3): 1 - || mean_j u(L (x - z_j)) ||,
    with u(v) = v/||v||, u(0) = 0, and L the inverse square root of the covariance."""
    data = np.asarray(data, dtype=float)
    x = np.asarray(x, dtype=float)
    cov = np.atleast_2d(np.cov(np.transpose(data)))

    if np.sum(np.isnan(cov)) == 0:
        # symmetric eigendecomposition; floor eigenvalues so a constant variable
        # (singular covariance) does not make the whitening matrix non-invertible
        w, v = np.linalg.eigh(cov)
        w = np.maximum(w, 1e-8)
        lambda1 = np.linalg.inv(np.matmul(v, np.diag(np.sqrt(w))))
    else:
        lambda1 = np.eye(data.shape[1])

    diff = (x[:, None, :] - data[None, :, :]) @ lambda1.T      # [len(x), len(data), V]
    norm = np.linalg.norm(diff, axis=2, keepdims=True)
    unit = np.divide(diff, norm, out=np.zeros_like(diff), where=norm > 0)
    return 1 - np.linalg.norm(unit.sum(axis=1) / len(data), axis=1)
