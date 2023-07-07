#!/bin/bash

docker run -d --name elastic \
    -v $(pwd):/usr/share/elasticsearch/data \
    --net elastic \
    -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch:7.17.10


# $(pwd) permet de récuperé le chemin absolu du répertoir dans lequel vous travaillez