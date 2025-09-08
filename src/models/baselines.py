import polars as pl

class PopularityRecommender:
    def __init__(self, topn=1000):
        self.topn = topn
        self.popular_items = []

    def fit(self, interactions: pl.DataFrame, user_col="user_id", item_col="anime_id"):
        counts = interactions.groupby(item_col).count().sort("count", descending=True)
        self.popular_items = counts[item_col].to_list()

    def recommend(self, user_id, k=10, seen_items=None):
        seen = set(seen_items or [])
        recs = [i for i in self.popular_items if i not in seen]
        return recs[:k]
