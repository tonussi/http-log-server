#!/usr/bin/env sh

sh scripts/experiment.sh kubernetes 1 2  50 raw/e1/512-rw; sleep 45;
sh scripts/experiment.sh kubernetes 1 4  50 raw/e1/512-rw; sleep 45;
sh scripts/experiment.sh kubernetes 1 8  50 raw/e1/512-rw; sleep 45;
sh scripts/experiment.sh kubernetes 2 4  50 raw/e1/512-rw; sleep 45;
sh scripts/experiment.sh kubernetes 1 16 50 raw/e1/512-rw; sleep 45;
sh scripts/experiment.sh kubernetes 2 8  50 raw/e1/512-rw; sleep 45;
sh scripts/experiment.sh kubernetes 2 10 50 raw/e1/512-rw; sleep 45;
sh scripts/experiment.sh kubernetes 2 12 50 raw/e1/512-rw; sleep 45;
sh scripts/experiment.sh kubernetes 2 14 50 raw/e1/512-rw; sleep 45;
sh scripts/experiment.sh kubernetes 1 32 50 raw/e1/512-rw; sleep 45;
sh scripts/experiment.sh kubernetes 2 16 50 raw/e1/512-rw; sleep 45;
sh scripts/experiment.sh kubernetes 1 64 50 raw/e1/512-rw; sleep 45;

sh scripts/experiment.sh kubernetes 1 2  100 raw/e1/512-r; sleep 45;
sh scripts/experiment.sh kubernetes 1 4  100 raw/e1/512-r; sleep 45;
sh scripts/experiment.sh kubernetes 1 8  100 raw/e1/512-r; sleep 45;
sh scripts/experiment.sh kubernetes 2 4  100 raw/e1/512-r; sleep 45;
sh scripts/experiment.sh kubernetes 1 16 100 raw/e1/512-r; sleep 45;
sh scripts/experiment.sh kubernetes 2 8  100 raw/e1/512-r; sleep 45;
sh scripts/experiment.sh kubernetes 2 10 100 raw/e1/512-r; sleep 45;
sh scripts/experiment.sh kubernetes 2 12 100 raw/e1/512-r; sleep 45;
sh scripts/experiment.sh kubernetes 2 14 100 raw/e1/512-r; sleep 45;
sh scripts/experiment.sh kubernetes 1 32 100 raw/e1/512-r; sleep 45;
sh scripts/experiment.sh kubernetes 2 16 100 raw/e1/512-r; sleep 45;
sh scripts/experiment.sh kubernetes 1 64 100 raw/e1/512-r; sleep 45;

sh scripts/experiment.sh kubernetes 1 2  0 raw/e1/512-w; sleep 45;
sh scripts/experiment.sh kubernetes 1 4  0 raw/e1/512-w; sleep 45;
sh scripts/experiment.sh kubernetes 1 8  0 raw/e1/512-w; sleep 45;
sh scripts/experiment.sh kubernetes 2 4  0 raw/e1/512-w; sleep 45;
sh scripts/experiment.sh kubernetes 1 16 0 raw/e1/512-w; sleep 45;
sh scripts/experiment.sh kubernetes 2 8  0 raw/e1/512-w; sleep 45;
sh scripts/experiment.sh kubernetes 2 10 0 raw/e1/512-w; sleep 45;
sh scripts/experiment.sh kubernetes 2 12 0 raw/e1/512-w; sleep 45;
sh scripts/experiment.sh kubernetes 2 14 0 raw/e1/512-w; sleep 45;
sh scripts/experiment.sh kubernetes 1 32 0 raw/e1/512-w; sleep 45;
sh scripts/experiment.sh kubernetes 2 16 0 raw/e1/512-w; sleep 45;
sh scripts/experiment.sh kubernetes 1 64 0 raw/e1/512-w; sleep 45;
