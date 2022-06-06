#!/usr/bin/env sh
export KUBERNETES_DIR=$1
export N_CLIENTS=$2
export N_THREADS=$3
export READ_RATE=$4
export SCENE=$5
export PORT=8001
export PAYLOAD_SIZE=1
export QTY_ITERATION=1000
export THINKING_TIME=0.2
export PERCENTAGE_SAMPLING=90
export SERVICE_NAME=http-log-server

echo "apply server..."
envsubst < $KUBERNETES_DIR/http-log-server.yml | kubectl apply -f -

sleep 5

echo "wait all replicas to be ready..."
until [ "$(kubectl get deployments -l app=http-log-server -o jsonpath="{.items[0].status.replicas}")" = "$(kubectl get deployments -l app=http-log-server -o jsonpath="{.items[0].status.readyReplicas}")" ]
do
  sleep 5;
done

echo "wait server to be running..."
until [ "$(kubectl get pods -l app=http-log-server -o jsonpath="{.items[0].status.phase}")" = "Running" ]
do
  sleep 5;
done

echo "apply clients..."
envsubst < $KUBERNETES_DIR/http-log-client.yml | kubectl apply -f -

echo "wait job to complete..."
kubectl wait --for=condition=complete --timeout=5m job.batch/http-log-client

TEST=$(expr $N_CLIENTS \* $N_THREADS)-$N_CLIENTS

echo "collecting throughput log..."
mkdir -p logs/$SCENE/throughput
kubectl logs $(kubectl get pods -l app=http-log-server -o=jsonpath='{.items[0].metadata.name}') > logs/$SCENE/throughput/$TEST.log

echo "collecting latency log..."
mkdir -p logs/$SCENE/latency
kubectl logs $(kubectl get pods -l app=http-log-client -o=jsonpath='{.items[0].metadata.name}') > logs/$SCENE/latency/$TEST.log

echo "deleting client..."
kubectl delete -f $KUBERNETES_DIR/http-log-client.yml

echo "deleting server..."
kubectl delete -f $KUBERNETES_DIR/http-log-server.yml

sleep 1
exit 0
