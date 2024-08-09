# Search with APACHE SOLR

### Add documents

- Connect to the solr with pysolr.
- Add relevant documents to the required index.

### Keyword search

- Simple keyword search in a particular field.
- Keyword search with flexible options using edismax query parser.
- Hybrid search:
  - Initially do the keyword search.
  - Rank the results based on cosine similarity score.
  - For ranking results we can use multiple methods.
