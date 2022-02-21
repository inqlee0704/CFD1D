#!/bin/bash

SCR_PATH=/data1/inqlee0704/CFD1D/pres_flow_lung_batch.sh 
# Proj=SABD
# SIM_TYPE=tidal # [tidal, tidal_20vc, slowdi, deepbr]
Proj=$1
SIM_TYPE=$2 # [tidal, tidal_20vc, slowdi, deepbr]
for SUBJ in $(ls -d ${Proj}_*/)
do
  cd $SUBJ/CFD1D
  echo $(pwd)
  for IMG in $(ls Output_*_Amount_whole.dat)
  do
    echo ${IMG}
    IFS='_' read -ra STR_ARRAY <<< ${IMG}
    Subj=${STR_ARRAY[1]}
    Img1=${STR_ARRAY[2]}
    Img2=${STR_ARRAY[3]}
    mkdir -p ${Img1}_${Img2}_${SIM_TYPE}
    cp -p ${IMG} ${Img1}_${Img2}_${SIM_TYPE}
    cp -p ${SCR_PATH} ${Img1}_${Img2}_${SIM_TYPE}
    cp -p ${Subj}_${Img1}_Central_1D_withDiameter.dat ${Img1}_${Img2}_${SIM_TYPE}
    
  done
  cd ../..
done
