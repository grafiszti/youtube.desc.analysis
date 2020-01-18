from typing import List

import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


class Doc2VecVectorizer:
    def __init__(self, vector_size: int = 300):
        self.vector_size = vector_size

    def fit_transform(self, texts: List[str]):
        documents = [TaggedDocument(doc.split(), [i]) for i, doc in enumerate(texts)]
        model = Doc2Vec(documents, vector_size=self.vector_size, window=4, min_count=2, workers=4)
        return np.array([model.docvecs[i] for i in range(len(texts))])
