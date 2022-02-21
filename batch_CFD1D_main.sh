#!/bin/bash
# ./batch_CFD_main.sh SABD_demo.csv SABD TLC0 RV0 tidal
Proj=$1
SIM_TYPE=$2 # [tidal, tidal_20vc, slowdi, deepbr]
Img1=$3
Img2=$4
DEMO_FILE=$5
DEMO_PATH=$(pwd)/${DEMO_FILE}
for SUBJ_DIR in $(ls -d ${Proj}_*/)
do
  if [ -d "${SUBJ_DIR}CFD1D/${Img1}_${Img2}_${SIM_TYPE}" ]
  then
    IFS='_' read -ra TEMP <<< ${SUBJ_DIR}  
    Subj=${TEMP[1]:0:-1}
    if grep -q ${Subj} ${DEMO_PATH}
    then 
      cd ${SUBJ_DIR}CFD1D/${Img1}_${Img2}_${SIM_TYPE}
      echo 
      echo Run 1D CFD:
      echo -----------
      echo $(pwd)
      echo 
      DEMO_STR=$(grep ${Subj} ${DEMO_PATH})
      IFS=',' read -ra DEMO_ARR <<< ${DEMO_STR}
      AGE=${DEMO_ARR[2]} 
      GENDER=${DEMO_ARR[3]} 
      HEIGHT_m=${DEMO_ARR[4]} 
      WEIGHT_kg=${DEMO_ARR[5]//} 
      V_tidal=$(echo $WEIGHT_kg*6*10^-6 | bc -l)
      HEIGHT_cm=$(echo $HEIGHT_m*100 | bc -l)
      ./pres_flow_lung_batch.sh ${Subj} ${Img1} ${Img2} ${V_tidal} ${HEIGHT_cm} ${AGE} ${GENDER} &>monit_pres_flow_lung.out &
      cd ../../..
    else 
      echo "Demo Not Found:" ${Subj}
    fi
  else
    echo "File Not Found: "
    echo ----------------
    echo ${SUBJ_DIR}CFD1D/${Img1}_${Img2}_${SIM_TYPE} 
    echo 
  fi
done
