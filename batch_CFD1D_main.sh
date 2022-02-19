#!/bin/bash

DEMO_PATH=$(pwd)/SABD_demo_subj36_20220217.csv
Proj=SABD
SIM_TYPE=tidal # [tidal, tidal_20vc, slowdi, deepbr]
Img1=TLC0
Img2=RV0
for SUBJ_DIR in $(ls -d ${Proj}_*/)
do
  cd $SUBJ_DIR/CFD1D/${Img1}_${Img2}_${SIM_TYPE}
  echo $(pwd)
  IFS='_' read -ra TEMP <<< ${SUBJ_DIR}  
  Subj=${TEMP[1]:0:-1}
  if grep -q ${Subj} ${DEMO_PATH}
  then 
    DEMO_STR=$(grep ${Subj} ${DEMO_PATH})
    IFS=',' read -ra DEMO_ARR <<< ${DEMO_STR}
    AGE=${DEMO_ARR[2]} 
    GENDER=${DEMO_ARR[3]} 
    HEIGHT=${DEMO_ARR[4]} 
    WEIGHT=${DEMO_ARR[5]} 
    echo ${AGE} ${GENDER} ${HEIGHT} ${WEIGHT}
  else 
    echo "Demo Not Found:" ${Subj}
  fi
  cd ../../..
done
