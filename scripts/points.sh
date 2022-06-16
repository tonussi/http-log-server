#!/usr/bin/env sh

sh ./scripts/experiment.sh kubernetes 1 2 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 1 4 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 2 2 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 1 8 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 2 4 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 1 16 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 2 8 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 1 32 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 2 16 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 1 64 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 3 8 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 2 18 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 2 19 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 2 21 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 3 10 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 2 24 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 2 26 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 3 12 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 3 14 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 2 32 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 1 128 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 3 14 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 3 21 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 4 13 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 4 16 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 2 64 100 raw/e1/128-r
sleep 10
sh ./scripts/experiment.sh kubernetes 4 18 100 raw/e1/128-r
sleep 10

sleep 1
exit 0
