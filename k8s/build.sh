#!/bin/bash

docker build -t etcd-test-app:latest .

echo "Loading image into minikube..."

minikube image load etcd-test-app:latest