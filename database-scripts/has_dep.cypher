// Create relationships between dep and packege2
LOAD CSV FROM '' AS row
MATCH (package:Package {id: row[8]})
MATCH (dep:Dependency {id: row[0]})
MERGE (dep)-[:Belongs_to]->(package);