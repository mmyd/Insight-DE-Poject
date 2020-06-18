# Library Compass
- A knowledge graph of package dependency 
- Locate the right version library for your project

## Motivation
- If a company plans to invest or design a software, how can researchers discover demand or opening for OSS market ?  
- A junior engineer tries to install a tool but they are too much packages and version issues. He has no idea to how to do that without clearly knowing the package dependencies.

## Architecture
![Alt text](https://github.com/mmyd/Insight-DE-Poject/blob/master/images/pipeline.png?raw=true "Optional Title")

## Data Modeling
![Alt text](https://github.com/mmyd/Insight-DE-Poject/blob/master/images/data_model.png?raw=true "Optional Title")

## Challenge
### Improve the performance of writing relationship to Neo4j
### Solution:
- Preprocess: Aggregate the statements using Spark
- Increase heap size
- Create index on nodes
- Batch transaction using periodical commit
### Result:
- update a million records with around 2G-4G per transaction => 10M nodes / relationships with 32G heap per transaction

 
## Visualization
![Alt text](https://github.com/mmyd/Insight-DE-Poject/blob/master/images/graph.png?raw=true "Optional Title")
