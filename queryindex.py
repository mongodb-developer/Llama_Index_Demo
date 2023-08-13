query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)
