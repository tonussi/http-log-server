#!/usr/bin/env sh

PV=$1
PVC=$2

kubectl delete pvc $PVC &
kubectl delete pv $PV &
kubectl get pvc $PVC
kubectl get pv $PV

echo "check status terminating?"

kubectl patch pvc $PVC -p '{"metadata":{"finalizers":null}}'
kubectl patch pv $PV -p '{"metadata":{"finalizers":null}}'

kubectl get pvc $PVC
kubectl get pv $PV
