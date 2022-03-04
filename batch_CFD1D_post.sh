#!/bin/bash
# ./batch_CFD_post.sh SABD TLC0 RV0 tidal
Proj=$1
CASE_TYPE=$2 # [tidal, tidal_20vc, slowdi, deepbr]
Img1=$3
Img2=$4

for SUBJ_DIR in $(ls -d ${Proj}_*/)
do
  if [ -f "${SUBJ_DIR}CFD1D/${Img1}_${Img2}_${CASE_TYPE}/data_plt_nd/plt_nd_000025.dat" ]
  then
    IFS='_' read -ra TEMP <<< ${SUBJ_DIR}
    Subj=${TEMP[1]:0:-1}
    cd ${SUBJ_DIR}CFD1D/${Img1}_${Img2}_${CASE_TYPE}
    cp -p /data1/inqlee0704/CFD1D/dat2csv.py .
    cp -p /data1/inqlee0704/CFD1D/extract_CFD1D.py .
    cp -p /data1/inqlee0704/CFD1D/extract_CFD1D_PI_PE.py .
    echo Extract CFD1D from:
    echo -------------------
    echo $(pwd)
    echo 
    mkdir -p data_plt_nd_csv
    python dat2csv.py plt_nd_000025.dat
    # python extract_CFD1D.py plt_nd_000025.csv ${Proj} ${Subj} ${Img1} ${Img2} tidal PI
    python dat2csv.py plt_nd_000075.dat
    # python extract_CFD1D.py plt_nd_000075.csv ${Proj} ${Subj} ${Img1} ${Img2} tidal PE
    python extract_CFD1D_PI_PE.py plt_nd_000025.csv plt_nd_000075.csv ${Proj} ${Subj} ${Img1} ${Img2} tidal


    
    cd ../../..
  else
    echo "File Not Found: "
    echo ----------------
    echo ${SUBJ_DIR}CFD1D/${Img1}_${Img2}_${CASE_TYPE}/data_plt_nd/plt_nd_000025.dat 
    echo 
  fi
done
