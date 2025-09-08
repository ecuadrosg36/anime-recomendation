import numpy as np

class MFExplicitALSStub:
    '''
    Implementación ligera de ejemplo (stub) para ilustrar interfaz de CF explícito.
    Reemplace por ALS real (e.g., implicit, surprise) o Autoencoder en TensorFlow.
    '''
    def __init__(self, n_factors=64, reg=0.1, n_iters=10, random_state=42):
        self.n_factors = n_factors
        self.reg = reg
        self.n_iters = n_iters
        self.random_state = random_state
        self.user_factors = None
        self.item_factors = None

    def fit(self, interactions_csr):
        rs = np.random.RandomState(self.random_state)
        self.user_factors = rs.normal(scale=0.1, size=(interactions_csr.shape[0], self.n_factors))
        self.item_factors = rs.normal(scale=0.1, size=(interactions_csr.shape[1], self.n_factors))

    def predict(self, u_idx, i_idx):
        return float(self.user_factors[u_idx].dot(self.item_factors[i_idx]))
