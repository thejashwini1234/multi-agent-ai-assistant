from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

def get_embeddings(texts):

    vectors = vectorizer.fit_transform(texts)

    return vectors.toarray()

def embed_query(query):

    return vectorizer.transform(
        [query]
    ).toarray()