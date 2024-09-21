LOAD CSV FROM "file:///intermediate_files/stat_analysis.tsv" AS line
FIELDTERMINATOR "\t" 
MERGE (callee:node{name:line[1]})
MERGE (caller:node{name:line[2]})
MERGE (caller)-[:calls]->(callee)
