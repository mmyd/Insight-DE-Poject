// Create relationships between package and platform
LOAD CSV WITH HEADERS FROM '' AS row
MATCH (package:Package {id: row.id})
MATCH (platform:Platform {name: row.platform})
MERGE (package)-[:Has_manager]->(platform);