#!/bin/bash

# Standalone
docker run --rm -it \
    -p 8000:8000 \
    --name stellar \
    stellar/quickstart:testing \
    --standalone \
    --enable-soroban-rpc