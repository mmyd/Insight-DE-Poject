// Create relationships between dependency and platform
LOAD CSV FROM '' AS row
MATCH (platform:Platform {id: row[4]})
MATCH (dep:Dependency {id: row[0]})
MERGE (dep)-[:Has_manager]->(platform);