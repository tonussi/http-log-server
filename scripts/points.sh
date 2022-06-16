#!/usr/bin/env sh

sh ./scripts/experiment.sh kubernetes 1 2 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 1 4 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 2 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 1 8 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 4 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 1 16 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 8 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 1 32 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 16 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 1 64 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 3 8 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 18 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 19 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 21 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 3 10 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 24 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 26 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 3 12 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 3 14 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 32 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 1 128 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 3 14 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 3 21 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 4 13 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 4 16 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 64 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 4 18 50 raw/e1/128-2-rw

sleep 1
exit 0
