# Download dataset: !gdown 1jh2p2DlaWsDo_vEWIcTrNh3mUuXd-cw6
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from icecream import ic


def tfidf_search(question, tfidf_vectorizer, context_embedded, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    cosine_scores = cosine_similarity(
        query_embedded, context_embedded).flatten()

    # Get top k cosine score and index it
    results = []

    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            "id": idx,
            "cosine_score": cosine_scores[idx]
        }
        results.append(doc_score)

    return results


def corr_search(question, tfidf_vectorizer, context_embedded, top_d=5):
    query_embedded = tfidf_vectorizer.transform(
        [question.lower()]).toarray()
    corr_scores = []

    for doc_vector in context_embedded:
        doc_vector = doc_vector.toarray()
        corr = np.corrcoef(query_embedded, doc_vector)[0, 1]
        corr_scores.append(corr)

    # Get top k cosine score and index it
    results = []
    corr_scores = np.array(corr_scores)

    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            "id": idx,
            "corr_score": corr_scores[idx]
        }
        results.append(doc_score)

    return results


if __name__ == '__main__':
    data = pd.read_csv("vi_text_retrieval.csv")
    context = data["text"]
    context = [doc.lower() for doc in context]

    ic(data.head())

    # Cau 10 -> B
    print("------------------- Cau 10 ---------------------")
    tfidf_vectorizer = TfidfVectorizer()
    context_embedded = tfidf_vectorizer.fit_transform(context)
    ic(context_embedded.toarray()[7][0])

    # Cau 11 -> D
    print("------------------- Cau 11 ---------------------")
    question = data.iloc[0]["question"]
    ic(question)
    results = tfidf_search(question, tfidf_vectorizer, context_embedded)
    ic(results[0]["cosine_score"])

    # Cau 12 -> B
    print("------------------- Cau 12 ---------------------")
    results = corr_search(question, tfidf_vectorizer, context_embedded)
    ic(results[1]["corr_score"])
