#!/bin/bash

# turn on bash's job control
set -m

# Start neo4j process and put it in the background
tini -g -- /startup/docker-entrypoint.sh neo4j &

# wait for Neo4j
wget --retry-connrefused --tries=20 --waitretry=10 -O /dev/null http://localhost:7474

cypher-shell -f import_stat_analysis.cypher

IFS=',' read -ra target_lib_prefixes <<< "$1"
for prefix in "${target_lib_prefixes[@]}"; do
  echo $prefix
  cypher-shell -f find_paths.cypher -P "{target_lib_prefix: \"$prefix\"}" --format plain
done 
