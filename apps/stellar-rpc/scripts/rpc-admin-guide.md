# Admin Guide

[Stellar Docs - Admin Guide](https://developers.stellar.org/docs/data/rpc/admin-guide)

## Standalone

- run docker image
- Query Horizon API

```bash
  curl "<http://localhost:8000>"
```

- Add it as a configured network:

```bash
  stellar network add standalone \
    --rpc-url "http://localhost:8000/soroban/rpc" \
    --network-passphrase "Standalone Network ; February 2017"
```

- generate unique key

```bash
  stellar keys generate alice
```

- deploying a contrct

```bash
  stellar contract deploy \
    --wasm target/wasm32-unknown-unknown/release/[project_name].wasm \
    --source alice \
    --network standalone
```

- invoking a contract

```bash
  stellar contract invoke \
    --id C... \
    --source alice \
    --network standalone \
    -- \
    hello \
    --to friend
```

## Testnet

- configure

```bash

  stellar network add testnet \
    --rpc-url "http://localhost:8000/soroban/rpc" \
    --network-passphrase "Test SDF Network ; September 2015"
```

## Futurenet

- configure

```bash
  stellar network add futurenet \
    --rpc-url "http://localhost:8000/soroban/rpc" \
    --network-passphrase "Test SDF Future Network ; October 2022"
```
