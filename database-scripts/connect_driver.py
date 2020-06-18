# pip install neo4j-driver

from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
    "bolt://100.26.209.30:34711", 
    auth=basic_auth("neo4j", "******"))
session = driver.session()

cypher_query = '''
MATCH (n)
RETURN id(n) AS id
LIMIT 10
'''

results = session.run(cypher_query,
  parameters={})

for record in results:
  print(record['id'])
