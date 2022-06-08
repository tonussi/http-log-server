#!/usr/bin/env sh

echo "running experiment 1 clients and $(expr 2 \/ 1) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 1 $(expr 2 \/ 1) 20 e1/1e6-20rw

echo "running experiment 1 clients and $(expr 4 \/ 1) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 1 $(expr 4 \/ 1) 20 e1/1e6-20rw

echo "running experiment 1 clients and $(expr 8 \/ 1) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 1 $(expr 8 \/ 1) 20 e1/1e6-20rw

echo "running experiment 2 clients and $(expr 8 \/ 2) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 2 $(expr 8 \/ 2) 20 e1/1e6-20rw

echo "running experiment 1 clients and $(expr 16 \/ 1) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 2 $(expr 16 \/ 1) 20 e1/1e6-20rw

echo "running experiment 2 clients and $(expr 16 \/ 2) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 3 $(expr 16 \/ 2) 20 e1/1e6-20rw

echo "running experiment 1 clients and $(expr 32 \/ 1) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 3 $(expr 32 \/ 1) 20 e1/1e6-20rw

echo "running experiment 2 clients and $(expr 32 \/ 2) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 4 $(expr 32 \/ 2) 20 e1/1e6-20rw

echo "running experiment 1 clients and $(expr 64 \/ 1) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 4 $(expr 64 \/ 1) 20 e1/1e6-20rw

echo "running experiment 2 clients and $(expr 64 \/ 2) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 5 $(expr 64 \/ 2) 20 e1/1e6-20rw

echo "running experiment 2 clients and $(expr 72 \/ 2) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 5 $(expr 72 \/ 2) 20 e1/1e6-20rw

echo "running experiment 3 clients and $(expr 72 \/ 3) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 6 $(expr 72 \/ 3) 20 e1/1e6-20rw

echo "running experiment 2 clients and $(expr 76 \/ 2) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 6 $(expr 76 \/ 2) 20 e1/1e6-20rw

echo "running experiment 2 clients and $(expr 84 \/ 2) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 7 $(expr 84 \/ 2) 20 e1/1e6-20rw

echo "running experiment 2 clients and $(expr 96 \/ 2) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 7 $(expr 96 \/ 2) 20 e1/1e6-20rw

echo "running experiment 3 clients and $(expr 96 \/ 3) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 7 $(expr 96 \/ 3) 20 e1/1e6-20rw

echo "running experiment 2 clients and $(expr 104 \/ 2) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 8 $(expr 104 \/ 2) 20 e1/1e6-20rw

echo "running experiment 3 clients and $(expr 108 \/ 3) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 8 $(expr 108 \/ 3) 20 e1/1e6-20rw

echo "running experiment 3 clients and $(expr 126 \/ 3) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 8 $(expr 126 \/ 3) 20 e1/1e6-20rw

echo "running experiment 1 clients and $(expr 128 \/ 1) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 8 $(expr 128 \/ 1) 20 e1/1e6-20rw

echo "running experiment 2 clients and $(expr 128 \/ 2) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 8 $(expr 128 \/ 2) 20 e1/1e6-20rw

echo "running experiment 3 clients and $(expr 132 \/ 3) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 9 $(expr 132 \/ 3) 20 e1/1e6-20rw

echo "running experiment 3 clients and $(expr 192 \/ 3) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 9 $(expr 192 \/ 3) 20 e1/1e6-20rw

echo "running experiment 4 clients and $(expr 208 \/ 4) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 10 $(expr 208 \/ 4) 20 e1/1e6-20rw

echo "running experiment 2 clients and $(expr 256 \/ 2) threads with a read rate of 50%"
sh ./scripts/experiment.sh kubernetes 10 $(expr 256 \/ 2) 20 e1/1e6-20rw

sleep 1
exit 0
