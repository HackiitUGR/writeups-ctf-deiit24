#!/bin/sh

docker rm clientside
docker rmi clientside
docker build . -t clientside
docker run -p 31423:31423 --name clientside clientside
