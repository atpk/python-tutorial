from transformers import pipeline
import pysolr
import json

# Connect to Solr
solr_url = 'http://localhost:8983/solr/hybrid_search'
solr = pysolr.Solr(solr_url, always_commit=True, timeout=10)

# Load a pre-trained BERT model for semantic search
semantic_search = pipeline('feature-extraction', model='bert-base-uncased', device=0)

def get_semantic_embedding(text):
    embeddings = semantic_search(text)
    return embeddings[0][0]

def keyword_search(query):
    results = solr.search(query)
    print(f'keyword search results: {results}')
    return results

def hybrid_search(query):
    # Perform keyword search
    keyword_results = keyword_search('content:'+query)# '*:*' to get all results
    
    # Check if there are any results
    if len(keyword_results) == 0:
        print("No keyword search results found.")
        return []

    # Perform semantic search
    query_embedding = get_semantic_embedding(query)

    # Rank Solr results based on semantic similarity
    ranked_results = []
    for result in keyword_results:
        if 'content' in result:
            doc_embedding = get_semantic_embedding(result['content'][0])
            similarity = cosine_similarity(query_embedding, doc_embedding)
            ranked_results.append((similarity, result))
        else:
            print(f'Missing content field in result: {result}')

    # Sort results by similarity
    ranked_results.sort(key=lambda x: x[0], reverse=True)
    print(f'ranked results: {ranked_results}')

    # Extract and return the sorted results
    sorted_results = [result[1] for result in ranked_results]
    return sorted_results

def cosine_similarity(vec1, vec2):
    dot_product = sum(p*q for p,q in zip(vec1, vec2))
    magnitude = (sum([val**2 for val in vec1]) * sum([val**2 for val in vec2])) ** 0.5
    if not magnitude:
        return 0
    return dot_product / magnitude

# Example search
query = "Programming Python"
results = hybrid_search(query)
print("results are: ")
for result in results:
    print(result)