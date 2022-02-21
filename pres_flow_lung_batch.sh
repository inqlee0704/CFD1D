#!/bin/bash

#******************************************************************************
# Solve 1-D pulmonary airflow model for pressure and flow rate distribution. 
# -----------------------------------------------------------------------------
# 02/17/2022, In Kyu Lee
#  - [Update] Run pres_flow_lung as a batch
# -----------------------------------------------------------------------------
# 01/31/2022, In Kyu Lee
#  - [FIX] PRES_SH is converted to pres_flow_lung_v1b.sh
# -----------------------------------------------------------------------------
# 12/8/2017, Jiwoong Choi
#  - Added some dahsed lines for convenience
# Version 2 (Shinjiro Miyawaki, 7/20/2016)
# Original version (Sanghun Choi?)
#******************************************************************************

# Paths
# -----
CODE_DIR=$HOME/mbin/Shin_Codes/fluid1d/exes
PREP_EXE=prep_pres_flow_lung.exe
PRES_EXE=pres_flow_lung.exe
PRES_SH=pres_flow_lung_batch.sh
INP_DIR=data_input
OUTP_DIR=data_output
MESH1D_DIR=data_mesh1D
PLT_ND_DIR=data_plt_nd
XFLX_DIR=data_xflx

# Arguments
# ---------
Subj=$1
Img1=$2
Img2=$3
V_tidal=$4
Height=$5
Age=$6
Gender=$7

# Set up the job
# --------------
# Global
  get_stats=0     # Get stats. of diameter ratio (1:yes, 0:no)
  hetero_All=0    # Heterogeneity applied to 0:no, 1:'E'-'T', 2:all branches
  lobar_hetero=1  # Heterogeneity applied 0:globally, 1:lobe by lobe
  BCond=1         # read(*,*) i_p_type 1,inQ & outP, 2, inP & outQ

# 1D mesh
# -------
# --------------------------------------
# file=Output_H17293_Amount_whole_as.dat  # 1D mesh
# file=Output_50052_TLC0_RV0_Amount_whole.dat  # 1D mesh
  file=Output_${Subj}_${Img1}_${Img2}_Amount_whole.dat  # 1D mesh
# --------------------------------------
# 1D mesh for <get_stats> = 1
  fileStatApollo=Output_MSM4D-013_Amount_Ap_Opt0_whole.dat  # Not used
  scale=0.001  # Scaling factor
# -----------
  igen_lim=30  # Highest generation number
# -----------

# Gas properties
# --------------
  rhog=1.2      # Fluid density (kg/m^3)
  visg=1.5d-05  # Kinematic viscosity (m^2/s)

# Simulation parameters
# ---------------------
# -----------
  i_max=400    # Total number of time steps
  idump=4      # Number of time steps between output files
  i_solver=2   # Matrix solver (1:BCG, 2:GMRES)
  i_kinetic=1  # Kinetic energy effect (0:off, 1:on)
# -----------

# Breathing pattern
# -----------------
  tperiod=4.80       # Breathing period (s)  # only for <i_wform>=1
# -----------------
  v_tidal=${V_tidal}  # Tidal volume (m^3)
# -----------------
  i_wform=1          # 1:sin, 2:Longest breathing waveform
  time_ein=2.4       # Time to end insp. for <i_wform> = 2
  xtime_pin=0.25     # Fraction of time to peak insp. for <i_wform> = 2
# --------------

# Clinical information. For <hetero_All> = 1 and get_stats> = 1
# ---------------------
# ------------
  gender=${Gender} # Gender (0:male, 1:female) for <get_stats> = 1
  age=${Age}    # Age (yr) for <get_stats> = 1
  height=${Height} # Height (cm) for <get_stats> = 1
# ------------

# Before the job
# --------------
# Copy *.exe files
cp -p $CODE_DIR/$PREP_EXE $CODE_DIR/$PRES_EXE ./

# Copy input files and codes to $INP_DIR
mkdir -p ./$INP_DIR
cp $PRES_SH ./$INP_DIR  # W/o time stamp to record start time
cp -p $PREP_EXE $PRES_EXE $file ./$INP_DIR

# Get input files
./$PREP_EXE $file $scale $BCond $get_stats \
	$gender $age $height $fileStatApollo

# Run the job
# -----------
./$PRES_EXE $rhog $visg $tperiod $v_tidal $i_max $idump \
	$scale $BCond $igen_lim $i_solver $i_kinetic \
	$hetero_All $lobar_hetero $i_wform $time_ein $xtime_pin

# After the job
# -------------
mkdir -p ./$OUTP_DIR ./$MESH1D_DIR ./$PLT_ND_DIR ./$XFLX_DIR

# Files from $PREP_EXE
mv flag_summary.dat single_001.dat kind_ne000001.dat \
	tec_whole.dat ./$OUTP_DIR/
if [ $get_stats -eq 1 ]; then
	mv Apollo_Statistics.dat ./$OUTP_DIR/
fi

# Files from $PRES_EXE
mv timehis.dat Nodal_Distance_from_Trachea.dat ./$OUTP_DIR/
mv mesh1D_******.dat ./$MESH1D_DIR/
mv plt_nd_******.dat ./$PLT_ND_DIR/
mv xflx_******.dat ./$XFLX_DIR/
if [ $hetero_All -gt 0 ]; then
	mv Diameter_Heterogeneity.dat ./$OUTP_DIR/
fi
