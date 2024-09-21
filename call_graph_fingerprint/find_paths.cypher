MATCH p=(n)-[:calls*..20]->(lib)
WHERE lib.name STARTS WITH $target_lib_prefix
  AND NOT ()-[:calls]->(n)
WITH p
ORDER BY length(p)
RETURN apoc.text.join([x IN nodes(p)|x.name], '->') AS call_chain
