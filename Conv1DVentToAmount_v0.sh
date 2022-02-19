#!/bin/bash
# ##############################################################################
# Conv1DVentToAmount_v0.sh Subj Img1 Img2
# Conv1DVentToAmount_v0.sh H16192 TLC FRC
# ##############################################################################
  Subj=$1
  Img1=$2
  Img2=$3
# -----------------------------------------------------------------
  OutputVentWholeDat=Output_${Subj}_${Img1}_${Img2}_Vent_whole.dat
  OutputAmountWholeDat=Output_${Subj}_Amount_whole.dat
# -----------------------------------------------------------------

  
  exec < $OutputVentWholeDat

  read Line1
  printf "%8s%8s%15s%15s%15s%15s%15s%15s%15s%15s%5s%6s%4s%5s%5s%6s%14s%15s%15s\n" ID PareID Length Diameter x_start y_start z_start x_end y_end z_end Gene Horsf Str Flag Lobe RefID rV Vol1 Vol0 > $OutputAmountWholeDat

# while IFS=$'\t' read -r 
  while read -r ID PareID Length Diameter x_start y_start z_start x_end y_end z_end Gene Horsf Str Flag Lobe RefID rV Vol0 Vol1 Vol2 ; do
    printf "%8s%8s %15s%15s%15s%15s%15s%15s%15s%15s %5s%5s%5s%5s%5s%5s %15s%15s%15s\n" $ID $PareID $Length $Diameter $x_start $y_start $z_start $x_end $y_end $z_end $Gene $Horsf $Str $Flag $Lobe $RefID $rV $Vol1 $Vol0 >> $OutputAmountWholeDat
#   ((ii++))
    if [ $(echo "${ID}%100" |bc ) = 0 ]; then
      printf "%15s\n" $ID
    fi
  done

  exec <&0

# ################################################################ END OF SCRIPT
