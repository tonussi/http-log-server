#!/usr/bin/env sh

sh ./scripts/experiment.sh kubernetes 1 2 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 1 4 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 2 2 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 1 8 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 2 4 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 1 16 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 2 8 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 1 32 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 2 16 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 1 64 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 3 8 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 2 18 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 2 19 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 2 21 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 3 10 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 2 24 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 2 26 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 3 12 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 3 14 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 2 32 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 1 128 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 3 14 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 3 21 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 4 13 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 4 16 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 2 64 0 raw/e1/128-w
sh ./scripts/experiment.sh kubernetes 4 18 0 raw/e1/128-w

sleep 1
exit 0
