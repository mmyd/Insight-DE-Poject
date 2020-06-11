// Create relationships between package and repo
LOAD CSV WITH HEADERS FROM '' AS row
MATCH (p:Package {id: row.id})
MATCH (r:Repository {id: row.repository_id})
MERGE (p)-[:Has_repo]->(r);