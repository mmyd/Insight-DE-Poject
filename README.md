# Pacakge Master
A knowledge graph of package dependency

## Motivation
- If a company plans to investigate or design a software, how the researcher can discover demand or opening for OSS market ?  
- A junior engineer try to install a tool but they are too much packages and version issue. He has no idea to how to do without clearly knowing the package dependencies.

## Architecture
![Alt text](https://github.com/mmyd/Insight-DE-Poject/blob/master/Screen%20Shot%202020-06-15%20at%201.54.15%20PM.png?raw=true "Optional Title")

## Data Modeling
![Alt text](https://github.com/mmyd/Insight-DE-Poject/blob/master/Screen%20Shot%202020-06-17%20at%2010.35.54%20PM.png?raw=true "Optional Title")

## Challenge
### Improve the performance of writing relationship to Neo4j
### Solution:
- Preprocess: Aggregation the statements using Spark
- Increase heap size
- Create index on nodes
- Batch transaction using periodical commit
### Result:
- update a million records with around 2G — 4G per transaction => 10M nodes / relationships with 32G heap per transaction

 
## Visualization
![Alt text](https://github.com/mmyd/Insight-DE-Poject/blob/master/graph%20(1).png?raw=true "Optional Title")
