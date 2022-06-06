#!/usr/bin/env sh
KUBERNETES_DIR=kubernetes

kubectl delete -f $KUBERNETES_DIR/http-log-client.yml
kubectl delete -f $KUBERNETES_DIR/http-log-server.yml
