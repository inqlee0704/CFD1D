# ##############################################################################
# batch_CFD1D_post2_v0.sh {Proj}
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
    for (( j=1; j<=${nFlowPhase}; j++ )); do
      cat CFD1D_all.0 >${Proj}_CFD1D_${CaseType[i]}_${FlowPhase[j]}_all.csv
      sed -s 1d ${Proj}_*/CFD1D/${CaseType[i]}/${Proj}_*_CFD1D_${CaseType[i]}_${FlowPhase[j]}.csv \
      >> ${Proj}_CFD1D_${CaseType[i]}_${FlowPhase[j]}_all.csv
    done
  done

#   cat SABD_5*/CFD1D/TLC0_RV0_tidal/SABD_5*_TLC0_RV0_PIFR_CFD1D.csv > SABD_all_TLC0_RV0_PIFR_CFD1D_36subjs.csv
#   cat SABD_5*/CFD1D/TLC0_RV0_tidal/SABD_5*_TLC0_RV0_PEFR_CFD1D.csv > SABD_all_TLC0_RV0_PEFR_CFD1D_36subjs.csv
#   cat SABD_5*/CFD1D/TLC1_RV1_tidal/SABD_5*_TLC1_RV1_PIFR_CFD1D.csv > SABD_all_TLC1_RV1_PIFR_CFD1D_36subjs.csv
#   cat SABD_5*/CFD1D/TLC1_RV1_tidal/SABD_5*_TLC1_RV1_PEFR_CFD1D.csv > SABD_all_TLC1_RV1_PEFR_CFD1D_36subjs.csv
