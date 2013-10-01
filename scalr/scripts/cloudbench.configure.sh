#!/bin/bash
set -o errexit
set -o nounset


cat > $CLOUDBENCH_CONFIG << EOF
[environment]
fio = /usr/local/bin/fio

[benchmarks]
blocksizes = 128k
depths = 1,2,3,4
modes = read,write,randread,randwrite,randrw
EOF
