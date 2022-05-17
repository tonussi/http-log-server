#!/usr/bin/env sh

kubectl delete -f kubernetes/mysql/pv.yml
kubectl delete -f kubernetes/mysql/deploy.yml
