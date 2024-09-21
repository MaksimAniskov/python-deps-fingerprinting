ARG NEO4J_VERSION
FROM neo4j:5.23

ENV NEO4J_AUTH=none
ENV NEO4J_PLUGINS=[\"apoc\"]

COPY wrapper.sh wrapper.sh
ENTRYPOINT ["./wrapper.sh"]

COPY *.cypher .
