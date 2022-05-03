# ##############################################################################
# batch_CFD1D_post2_v0a.sh {Proj}
# ##############################################################################
# 20220227, In Kyu Lee
# - combine PI and PE as one row
# ##############################################################################

# ------------
  Proj=$1 
# ------------
  nCaseType=2
  nFlowPhase=2
# --------------------------
  CaseType[1]=TLC0_RV0_tidal
  CaseType[2]=TLC1_RV1_tidal
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

#   cat SABD_5*/CFD1D/TLC0_RV0_tidal/SABD_5*_TLC0_RV0_PIFR_CFD1D.csv > SABD_all_TLC0_RV0_PIFR_CFD1D_36subjs.csv
#   cat SABD_5*/CFD1D/TLC0_RV0_tidal/SABD_5*_TLC0_RV0_PEFR_CFD1D.csv > SABD_all_TLC0_RV0_PEFR_CFD1D_36subjs.csv
#   cat SABD_5*/CFD1D/TLC1_RV1_tidal/SABD_5*_TLC1_RV1_PIFR_CFD1D.csv > SABD_all_TLC1_RV1_PIFR_CFD1D_36subjs.csv
#   cat SABD_5*/CFD1D/TLC1_RV1_tidal/SABD_5*_TLC1_RV1_PEFR_CFD1D.csv > SABD_all_TLC1_RV1_PEFR_CFD1D_36subjs.csv
