from typing import List
from sentence_transformers import SentenceTransformer

class SynopsisEmbedder:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts: List[str]):
        return self.model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
