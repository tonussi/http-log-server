#!/usr/bin/env sh

sh ./scripts/experiment.sh kubernetes 2 1 50 e1/128-rw
sh ./scripts/experiment.sh kubernetes 4 1 50 e1/128-rw
sh ./scripts/experiment.sh kubernetes 4 2 50 e1/128-rw
sh ./scripts/experiment.sh kubernetes 8 1 50 e1/128-rw
sh ./scripts/experiment.sh kubernetes 8 2 50 e1/128-rw
sh ./scripts/experiment.sh kubernetes 16 1 50 e1/128-rw
sh ./scripts/experiment.sh kubernetes 16 2 50 e1/128-rw
sh ./scripts/experiment.sh kubernetes 32 1 50 e1/128-rw
sh ./scripts/experiment.sh kubernetes 32 2 50 e1/128-rw
sh ./scripts/experiment.sh kubernetes 64 1 50 e1/128-rw
sh ./scripts/experiment.sh kubernetes 24 3 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 36 2 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 38 2 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 42 2 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 32 3 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 48 2 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 52 2 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 36 3 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 42 3 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 64 2 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 128 1 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 44 3 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 64 3 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 52 4 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 64 4 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 128 2 50 e1/128-rw
# sh ./scripts/experiment.sh kubernetes 72 4 50 e1/128-rw

sleep 1
exit 0
