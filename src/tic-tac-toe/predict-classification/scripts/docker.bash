#!/usr/bin/env bash

cd ..

echo "UID: $(id -u)"
echo "GID: $(id -g)"

docker --debug buildx build --build-arg UID="$(id -u)" --build-arg GID="$(id -g)" --no-cache --progress plain .
docker-compose up

#docker --debug build -t dockerfile-image --build-arg UID="$(id -u)" --build-arg GID="$(id -g)" .
#docker run -d --name docker-container docker-image
