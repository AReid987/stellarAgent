#!/bin/bash

# Testnet

docker run --rm -it \
    -p 8000:8000 \
    --name stellar \
    stellar/quickstart:testing \
    --testnet \
    --enable-soroban-rpc