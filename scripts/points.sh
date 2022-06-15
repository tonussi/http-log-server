#!/usr/bin/env sh

sh ./scripts/experiment.sh kubernetes 1 $(expr 2 \/ 1) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 1 $(expr 4 \/ 1) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 $(expr 4 \/ 2) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 1 $(expr 8 \/ 1) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 $(expr 8 \/ 2) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 1 $(expr 16 \/ 1) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 $(expr 16 \/ 2) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 1 $(expr 32 \/ 1) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 $(expr 32 \/ 2) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 1 $(expr 64 \/ 1) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 3 $(expr 24 \/ 3) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 $(expr 36 \/ 2) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 $(expr 38 \/ 2) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 $(expr 42 \/ 2) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 3 $(expr 32 \/ 3) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 $(expr 48 \/ 2) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 $(expr 52 \/ 2) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 3 $(expr 36 \/ 3) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 3 $(expr 42 \/ 3) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 $(expr 64 \/ 2) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 1 $(expr 128 \/ 1) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 3 $(expr 44 \/ 3) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 3 $(expr 64 \/ 3) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 4 $(expr 52 \/ 4) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 4 $(expr 64 \/ 4) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 2 $(expr 128 \/ 2) 50 raw/e1/128-2-rw
sh ./scripts/experiment.sh kubernetes 4 $(expr 72 \/ 4) 50 raw/e1/128-2-rw

sleep 1
exit 0
