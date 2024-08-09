import pysolr
import time

# Connect to Solr
solr_url = 'http://localhost:8983/solr/hybrid_search'
solr = pysolr.Solr(solr_url, always_commit=True, timeout=10)

def simple_keyword_search(query):
    # Search exact keywords in a particular field only
    results = solr.search('content:'+query)
    return results

def keyword_search(query):
    # Use edismax query parser for flexible search
    query_string = f'{query}'
    params = {
        'defType': 'edismax',       # Use edismax query parser
        'qf': 'title content',      # Fields to search
        'q': query_string,          # Query string
        'mm': '100%',                # Minimum match (100% means all terms must match)
        'fuzziness': 'AUTO'         # Auto fuzziness
    }
    results = solr.search(**params)
    return results

# Example search
start_time = time.time()
query = "pythn~ learn" # Adding ~ for fuzzy search
results = keyword_search(query)
print(f'time: {time.time()-start_time}')
print("Results are:")
for result in results:
    print(result)  # Print each result object