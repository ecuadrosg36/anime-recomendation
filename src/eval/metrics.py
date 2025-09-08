import numpy as np

def rmse(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    return float(np.sqrt(np.mean((y_true - y_pred)**2)))

def mae(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    return float(np.mean(np.abs(y_true - y_pred)))

def recall_at_k(truth, recs, k=10):
    truth = set(truth)
    topk = recs[:k]
    if not truth:
        return 0.0
    hit = len(truth.intersection(topk))
    return hit / len(truth)

def dcg_at_k(rels, k=10):
    import numpy as np
    rels = np.array(rels[:k], dtype=float)
    if rels.size == 0:
        return 0.0
    discounts = 1.0 / np.log2(np.arange(2, rels.size + 2))
    return float(np.sum(rels * discounts))

def ndcg_at_k(truth, recs, k=10):
    truth = set(truth)
    gains = [1.0 if i in truth else 0.0 for i in recs[:k]]
    ideal = sorted(gains, reverse=True)
    idcg = dcg_at_k(ideal, k=k)
    if idcg == 0:
        return 0.0
    return dcg_at_k(gains, k=k) / idcg
