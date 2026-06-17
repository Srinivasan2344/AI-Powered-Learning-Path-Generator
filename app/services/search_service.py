from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def semantic_search(query, resources):

    query_embedding = model.encode(query)

    scores = []

    for resource in resources:

        embedding = model.encode(
            resource["content"]
        )

        similarity = np.dot(
            query_embedding,
            embedding
        ) / (
            np.linalg.norm(query_embedding)
            * np.linalg.norm(embedding)
        )

        scores.append(
            (
                similarity,
                resource["title"]
            )
        )

    scores.sort(reverse=True)

    return scores[:3]