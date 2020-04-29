#!/bin/bash

PROG=linear_oram_read_benchmark
PROG_NAME=Programs/${PROG}
FILE_NAME=Programs/${PROG}/${PROG}.mpc
FILE_NAME_TMP=${FILE_NAME}.duplicate

for m in 4 8 16 32 64; do

  cp ${FILE_NAME} ${FILE_NAME_TMP}
  
  sed -i 's/SED_TO_VALUE_OF_M/'${m}'/g' ${FILE_NAME}

  ./benchmark.sh ${PROG_NAME} 3 1 1 false false 0 1 2

  mv communication.txt communication.txt.${m}

  rm ${FILE_NAME}
  mv ${FILE_NAME_TMP} ${FILE_NAME}

done
