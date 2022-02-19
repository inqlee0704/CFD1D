#!/bin/bash
# ==============================================================================
# Usage: batch_CFD1D_ini_v0a.sh PRONE_ProjSubjList.in
# Run in Proj directory
# ==============================================================================
# ----------------------------------------------------------------
# Path1=/data1/jiwchoi/IR
# Apollo2IR=${Path1}/Batches_SABD/Apollo2IR_SABD_2.sh
# Apollo2IR=${Path1}/Batches_SABD/Apollo2IR_CBNCT_3.sh
# ----------------------------------------------------------------
  nImg=2
# ----------------------------------------------------------------

  declare -a Proj
  declare -a Subj
  declare -a Img
  declare -a ImgDir
  declare -a SrcDir

# Link filedescriptor 10 with stdin
  exec 10<&0

# stdin replaced with a file supplied as a first argument
  exec < $1
  let ii=0
  printf "\n"

# ------------------------------------------------------------------------------------
# read Col1 Col2 Col3 Col4 Col5   # Deactivate if there is no header for variable names.
  read Col1 Col2 Col3 Col4        # Deactivate if there is no header for variable names.
# ------------------------------------------------------------------------------------
  while IFS=$'\t' read -r Proj[ii] Subj[ii] Img1 VidaDir ; do 
# while IFS=$'\t' read -r Proj[ii] Subj[ii] PID[ii] ImgDir[1] ImgDir[2] ; do 
# while IFS=$'\t' read -r Proj[ii] Subj[ii] PID[ii] ImgDir[2] ImgDir[1] ; do 
# while IFS=$'\t' read -r Proj[ii] Subj[ii] PID[ii] ; do 
# ------------------------------------------------------------------------------------

#   Proj[ii]="${Proj[ii]##*( )}"; Proj[ii]="${Proj[ii]%%*( )}"
#   Subj[ii]="${Subj[ii]##*( )}"; Subj[ii]="${Subj[ii]%%*( )}"
#   PID[ii]="${PID[ii]##*( )}"; PID[ii]="${PID[ii]%%*( )}"
#   ImgDir[1]="${ImgDir[1]##*( )}"; ImgDir[1]="${ImgDir[1]%%*( )}"
#   ImgDir[2]="${ImgDir[2]##*( )}"; ImgDir[2]="${ImgDir[2]%%*( )}"
#   SrcDir="${SrcDir##*( )}"; SrcDir="${SrcDir%%*( )}"
#   Img1="${Img1##*( )}"; Img1="${Img1%%*( )}"

#   Img[ii]="${Img[ii]##*( )}"; Img[ii]="${Img[ii]%%*( )}"

#   SubjDir=${Proj[ii]}_${Subj[ii]}

#   printf " ${Proj[ii]} ${Subj[ii]} ${Img[ii]} ${ScrDir[ii]} \n"
    printf " ${SubjDir}\n"

#   mkdir -p ${SubjDir}
    cd ${SubjDir}/CFD1D
    mkdir ${Img1}_${Img2}_${pattern} 

    printf " ${Proj[ii]} ${Subj[ii]} ${Img1} ${VidaDir} \n"
#   +++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ${Apollo2IR} ${Proj[ii]} ${Subj[ii]} ${Img1} ${VidaDir}
#   +++++++++++++++++++++++++++++++++++++++++++++++++++++++

    cd ../
    ((ii++))

  done # < "myfile"
  printf "${ii}/$nImg Subjects Done! ${nImg} images each. \n"

# Recover stdin
  exec 0<&10 10<&-
# ################################################################ END OF SCRIPT
