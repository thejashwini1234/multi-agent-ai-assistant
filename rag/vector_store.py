import faiss
import numpy as np

class VectorStore:

    def __init__(self):

        self.texts = []

        self.index = None

    def add_embeddings(
        self,
        texts,
        embeddings
    ):

        self.texts = texts

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            np.array(
                embeddings
            ).astype('float32')
        )

    def search(
        self,
        query_embedding,
        k=3
    ):

        distances, indices = self.index.search(
            np.array(
                query_embedding
            ).astype('float32'),
            k
        )

        results = []

        for idx in indices[0]:

            results.append(
                self.texts[idx]
            )

        return results