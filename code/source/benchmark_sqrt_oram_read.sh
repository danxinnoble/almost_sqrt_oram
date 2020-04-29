#!/bin/bash

PROG=sqrt_oram_access_benchmark
PROG_NAME=Programs/${PROG}
FILE_NAME=Programs/${PROG}/${PROG}.mpc
FILE_NAME_TMP=${FILE_NAME}.duplicate

ms=(4 16)
ts=(80 20)


for i in {0..2}; do

  m=${ms[${i}]}
  t=${ts[${i}]}

  cp ${FILE_NAME} ${FILE_NAME_TMP}
  
  sed -i 's/SED_TO_VALUE_OF_M/'${m}'/g' ${FILE_NAME}
  sed -i 's/SED_TO_NUMBER_OF_REPEATS/'${t}'/g' ${FILE_NAME}

  ./benchmark.sh ${PROG_NAME} 3 1 0 true true 0 1 2

  mv communication.txt communication.txt.${m}.${t}

  rm ${FILE_NAME}
  mv ${FILE_NAME_TMP} ${FILE_NAME}

done
