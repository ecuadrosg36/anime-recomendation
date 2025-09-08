import numpy as np

class MFImplicitStub:
    '''
    Implementación ligera de ejemplo (stub) para CF implícito (sólo interfaz de demostración).
    Reemplace por 'implicit' (als/bpr) o 'lightfm' (BPR/WARP) en producción.
    '''
    def __init__(self, n_factors=64, random_state=42):
        self.n_factors = n_factors
        self.random_state = random_state
        self.user_factors = None
        self.item_factors = None

    def fit(self, interactions_csr):
        rs = np.random.RandomState(self.random_state)
        self.user_factors = rs.normal(scale=0.1, size=(interactions_csr.shape[0], self.n_factors))
        self.item_factors = rs.normal(scale=0.1, size=(interactions_csr.shape[1], self.n_factors))

    def score_all_items(self, u_idx):
        return self.user_factors[u_idx].dot(self.item_factors.T)
