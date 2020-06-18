//create dependency 
LOAD CSV WITH HEADERS FROM ' ' AS line
CREATE (:Dependency {id:line.id, name: line.name, kind:line.kind,optional:line.optinal,requirement:line.requirement})
CREATE INDEX ON :Dependency(id)