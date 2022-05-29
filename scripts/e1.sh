#!/usr/bin/env sh
KUBERNETES_DIR=$1
export N_CLIENTS=$2
export N_THREADS=$3
export READ_RATE=$4
SCENE=$5

export SERVICE_NAME=http-log-server

echo "apply server..."
kubectl apply -f $KUBERNETES_DIR/http-log-server.yml

sleep 5

echo "wait all replicas to be ready..."
until [ "$(kubectl get sts -l app=http-log-server -o jsonpath="{.items[0].status.replicas}")" = "$(kubectl get sts -l app=http-log-server -o jsonpath="{.items[0].status.readyReplicas}")" ]
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
kubectl wait --for=condition=complete --timeout=60s job.batch/http-log-client

TEST=$(expr $N_CLIENTS \* $N_THREADS)-$N_CLIENTS

echo "collecting throughput log..."
kubectl cp $(kubectl get pods -l app=http-log-server -o=jsonpath='{.items[0].metadata.name}'):/tmp/logs/throughput.log logs/lucas/$SCENE/throughput/$TEST.log
kubectl cp $(kubectl get pods -l app=http-log-server -o=jsonpath='{.items[0].metadata.name}'):/tmp/logs/operations.log logs/lucas/$SCENE/sts-0/operations/$TEST.log
kubectl cp $(kubectl get pods -l app=http-log-server -o=jsonpath='{.items[1].metadata.name}'):/tmp/logs/operations.log logs/lucas/$SCENE/sts-1/operations/$TEST.log
kubectl cp $(kubectl get pods -l app=http-log-server -o=jsonpath='{.items[2].metadata.name}'):/tmp/logs/operations.log logs/lucas/$SCENE/sts-2/operations/$TEST.log
kubectl cp $(kubectl get pods -l app=http-log-server -o=jsonpath='{.items[3].metadata.name}'):/tmp/logs/operations.log logs/lucas/$SCENE/sts-3/operations/$TEST.log

echo "collecting latency log..."
mkdir -p logs/lucas/$SCENE/latency
kubectl logs $(kubectl get pods -l app=http-log-client -o=jsonpath='{.items[0].metadata.name}') > logs/lucas/$SCENE/latency/$TEST.log

echo "deleting client..."
kubectl delete -f $KUBERNETES_DIR/http-log-client.yml

echo "deleting server..."
kubectl delete -f $KUBERNETES_DIR/http-log-server.yml
