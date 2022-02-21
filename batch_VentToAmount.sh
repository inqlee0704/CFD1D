#!/bin/bash

Proj=SABD
Script=Conv1DVentToAmount_v0a.sh
for SUBJ_FOLDER in $(ls -d ${Proj}_*/)
do
  cd $SUBJ_FOLDER/CFD1D
  echo $(pwd)
  cp -p /data1/inqlee0704/CFD1D/${Script} .
  for IMG in $(ls Output_*_Vent_whole.dat)
  do
    IFS='_' read -ra STR_ARRAY <<< ${IMG}
    Subj=${STR_ARRAY[1]}
    Img1=${STR_ARRAY[2]}
    Img2=${STR_ARRAY[3]}

    ./${Script} ${Subj} ${Img1} ${Img2} 

  done
  cd ../..
done
