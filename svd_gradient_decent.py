import numpy as np

def svd(M: np.array, k:int, iterations: int=1000, lr: float=1e-3):
    
    def svd_step(M: np.array, iterations: int, lr: float):
        m, n = M.shape
        u = np.zeros(m) + 0.1
        v = np.zeros(n) + 0.1
        for _ in range(iterations):
            for i in range(m):
                for j in range(n):
                    err = M[i, j] - u[i]*v[j]
                    u[i], v[j] = u[i]+lr*v[j]*err, v[j]+lr*u[i]*err
                    
        return u.reshape(-1, 1), v.reshape(-1, 1)
    
    if k == 0:
        return [], []
    u, v = svd_step(M, iterations, lr)
    
    us, vs = svd(M-u@v.T, k-1, iterations, lr)
    return [u] + us, [v] + vs