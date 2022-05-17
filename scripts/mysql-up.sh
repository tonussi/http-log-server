#!/usr/bin/env sh

kubectl apply -f kubernetes/mysql/pv.yml
kubectl apply -f kubernetes/mysql/deploy.yml
