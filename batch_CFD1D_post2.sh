# ##############################################################################
# batch_CFD1D_post2.sh {Proj} {CASE_TYPE} {Img1} {Img2}
# ##############################################################################
# 20220227, In Kyu Lee
# - combine PI and PE as one row
# ##############################################################################

# ------------
  Proj=$1 
  CaseType=$2
  Img1=$3
  Img2=$4
# ------------
  nCaseType=1
  nFlowPhase=2
# --------------------------
  CaseType[1]=${Img1}_${Img2}_${CaseType}
#  CaseType[2]=TLC1_RV1_tidal
# --------------------------
  FlowPhase[1]=PI
  FlowPhase[2]=PE
# ---------------

  for (( i=1; i<=${nCaseType}; i++ )); do
    cat CFD1D_all_PI_PE.0 >${Proj}_CFD1D_${CaseType[i]}_${FlowPhase[1]}_${FlowPhase[2]}_all.csv
    sed -s 1d ${Proj}_*/CFD1D/${CaseType[i]}/${Proj}_*_CFD1D_${CaseType[i]}_${FlowPhase[1]}_${FlowPhase[2]}.csv \
    >> ${Proj}_CFD1D_${CaseType[i]}_${FlowPhase[1]}_${FlowPhase[2]}_all.csv

    cat CFD1D_all_PI_PE_std.0 >${Proj}_CFD1D_${CaseType[i]}_${FlowPhase[1]}_${FlowPhase[2]}_all_std.csv
    sed -s 1d ${Proj}_*/CFD1D/${CaseType[i]}/${Proj}_*_CFD1D_${CaseType[i]}_${FlowPhase[1]}_${FlowPhase[2]}_std.csv \
    >> ${Proj}_CFD1D_${CaseType[i]}_${FlowPhase[1]}_${FlowPhase[2]}_all_std.csv

    cat CFD1D_all_PI_PE_n.0 >${Proj}_CFD1D_${CaseType[i]}_${FlowPhase[1]}_${FlowPhase[2]}_all_n.csv
    sed -s 1d ${Proj}_*/CFD1D/${CaseType[i]}/${Proj}_*_CFD1D_${CaseType[i]}_${FlowPhase[1]}_${FlowPhase[2]}_n.csv \
    >> ${Proj}_CFD1D_${CaseType[i]}_${FlowPhase[1]}_${FlowPhase[2]}_all_n.csv
  done
