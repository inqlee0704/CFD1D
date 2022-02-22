#!/bin/bash
# ./batch_CFD_post.sh SABD TLC0 RV0 tidal
Proj=$1
SIM_TYPE=$2 # [tidal, tidal_20vc, slowdi, deepbr]
Img1=$3
Img2=$4

for SUBJ_DIR in $(ls -d ${Proj}_*/)
do
  if [ -d "${SUBJ_DIR}CFD1D/${Img1}_${Img2}_${SIM_TYPE}/data_plt_nd" ]
  then
    cd ${SUBJ_DIR}CFD1D/${Img1}_${Img2}_${SIM_TYPE}
    cp -p /data1/inqlee0704/CFD1D/dat2csv.py .
    echo 
    echo convert dat to csv:
    echo -------------------
    echo $(pwd)
    echo 
    for STEP in $(ls data_plt_nd/*.dat)
    do
      echo $STEP
    
    done
    cd ../../..
    break
  else
    echo "File Not Found: "
    echo ----------------
    echo ${SUBJ_DIR}CFD1D/${Img1}_${Img2}_${SIM_TYPE}/data_plt_nd 
    echo 
  fi
done
