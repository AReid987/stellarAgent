#!/bin/#!/bin/bash

# futurenet
docker run --rm -it \
    -p 8000:8000 \
    --name stellar \
    stellar/quickstart:soroban-dev \
    --futurenet \
    --enable-soroban-rpc