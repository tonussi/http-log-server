#!/usr/bin/env sh

# running experiment 1 clients and 2 threads with a read rate of 50%
sh ./scripts/experiment.sh kubernetes 1 2 50 e1/128-rw
# running experiment 1 clients and 4 threads with a read rate of 50%
sh ./scripts/experiment.sh kubernetes 1 4 50 e1/128-rw
# running experiment 1 clients and 8 threads with a read rate of 50%
sh ./scripts/experiment.sh kubernetes 1 8 50 e1/128-rw
# running experiment 2 clients and 4 threads with a read rate of 50%
sh ./scripts/experiment.sh kubernetes 2 4 50 e1/128-rw
# running experiment 1 clients and 16 threads with a read rate of 50%
sh ./scripts/experiment.sh kubernetes 1 16 50 e1/128-rw
# # running experiment 2 clients and 8 threads with a read rate of 50%
sh ./scripts/experiment.sh kubernetes 2 8 50 e1/128-rw
# # running experiment 1 clients and 32 threads with a read rate of 50%
sh ./scripts/experiment.sh kubernetes 1 32 50 e1/128-rw
# # running experiment 2 clients and 16 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 2 16 50 e1/128-rw
# # running experiment 1 clients and 64 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 1 64 50 e1/128-rw
# # running experiment 2 clients and 32 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 2 32 50 e1/128-rw
# # running experiment 2 clients and 36 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 2 36 50 e1/128-rw
# # running experiment 3 clients and 24 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 3 24 50 e1/128-rw
# # running experiment 2 clients and 38 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 2 38 50 e1/128-rw
# # running experiment 2 clients and 42 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 2 42 50 e1/128-rw
# # running experiment 2 clients and 48 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 2 48 50 e1/128-rw
# # running experiment 3 clients and 32 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 3 32 50 e1/128-rw
# # running experiment 2 clients and 52 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 2 52 50 e1/128-rw
# # running experiment 3 clients and 36 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 3 36 50 e1/128-rw
# # running experiment 3 clients and 42 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 3 42 50 e1/128-rw
# # running experiment 1 clients and 128 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 1 128 50 e1/128-rw
# # running experiment 2 clients and 64 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 2 64 50 e1/128-rw
# # running experiment 3 clients and 44 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 3 44 50 e1/128-rw
# # running experiment 3 clients and 64 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 3 64 50 e1/128-rw
# # running experiment 4 clients and 52 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 4 52 50 e1/128-rw
# # running experiment 2 clients and 128 threads with a read rate of 50%
# sh ./scripts/experiment.sh kubernetes 2 128 50 e1/128-rw

sleep 1
exit 0
