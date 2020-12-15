#!/bin/sh
parentdir="$(dirname $(dirname $(dirname "$(pwd)")))"
echo $parentdir
docker container stop bglapi-filters-positive-test
docker container rm bglapi-filters-positive-test
docker run --name bglapi-filters-positive-test \
           -v $parentdir/config:/config/ \
           -v $parentdir/data/socket/:/var/run/postgresql/ \
           -v $(pwd)/:/app/ \
           --net=host \
           -it bglapi-filters-positive-test