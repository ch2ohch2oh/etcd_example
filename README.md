# Etcd Docker Compose Examples

This repository provides examples of running etcd clusters using Docker Compose, including both single-node and multi-node configurations, along with Python pytest examples to demonstrate basic etcd operations.

## Prerequisites

*   Docker
*   Docker Compose (or `docker compose` plugin)
*   Python 3.x (for running tests directly, though Docker Compose handles it)

## Single-Node Etcd Cluster

### Usage

1.  **Start the etcd cluster:**

    ```bash
    docker compose up -d
    ```
2.  **Interact with etcd:**
    *   Using `etcdctl`:
        ```bash
        docker compose exec etcd etcdctl put mykey "this is a test"
        docker compose exec etcd etcdctl get mykey
        ```
    *   Using REST API (example for `mykey`):
        ```bash
        curl -L http://localhost:2379/v3/kv/range -X POST -d '{"key": "bXlrZXk="}'
        ```
3.  **Run tests:**

    ```bash
    docker compose run tests
    ```
    This command starts etcd (if not running), sets up the test environment, and executes pytest.

### Cleanup

```bash
docker compose down
```

## Multi-Node Etcd Cluster

### Usage

1.  **Start the multi-node etcd cluster:**

    ```bash
    docker compose -f docker-compose-multi.yml up -d
    ```
2.  **Interact with etcd:**
    *   Using `etcdctl` (example: put on `etcd1`, get on `etcd2`):
        ```bash
        docker compose -f docker-compose-multi.yml exec etcd1 etcdctl put mykey "this is a test on multi-node"
        docker compose -f docker-compose-multi.yml exec etcd2 etcdctl get mykey
        ```
3.  **Run tests:**

    ```bash
    docker compose -f docker-compose-multi.yml run tests
    ```

### Cleanup

```bash
docker compose -f docker-compose-multi.yml down
```