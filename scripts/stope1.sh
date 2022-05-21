#!/usr/bin/env sh
KUBERNETES_DIR=$1
export N_CLIENTS=$2
export N_THREADS=$3
export READ_RATE=$4
SCENE=$5

export SERVICE_NAME=http-log-server

echo "deleting client..."
envsubst < $KUBERNETES_DIR/http-log-client.yml | kubectl delete -f -

echo "deleting server..."
kubectl delete -f $KUBERNETES_DIR/http-log-server.yml
