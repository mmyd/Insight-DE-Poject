MATCH path=(p1:Package)-[rel:Has_dep]->(:Dependency)-[:Belongs_to]->(:Package)-[:Has_dep]->(:Dependency)
WHERE p1.name="vibenews" and rel.version contains "0.6.5" 
RETURN path
LIMIT 10;

MATCH path1=(:Platform{id:’dub’})-[:Has_manager]->(p1:Package)-[:Has_repo]->(:Repository) 
MATCH path2 = (:Dependency)-[:Belongs_to]->(p1:Package)-[:Has_dep]->(:Dependency)
RETURN path1,path2;

MATCH path=(:Dependency)-[:Belongs_to]->(p1:Package)-[:Has_dep]->(:Dependency)-[:Belongs_to]->(p2:Package)
MATCH path2=(:Platform)<-[:Has_manager]-(p1:Package)-[:Has_repo]->(:Repository)
MATCH path3=(p2:Package)-[:Has_repo]->(:Repository) 
RETURN path,path2,path3
LIMIT 2000;

MATCH path=(:Platform{id:"dub"})<-[:Has_manager]-(p1:Package)-[:Has_dep]->(:Dependency)-[:Belongs_to]->(p2:Package)
WHERE(p1:Package)-[:Has_repo]->(:Repository) or (p2:Package)-[:Has_repo]->(:Repository)
RETURN path
LIMIT 10;
