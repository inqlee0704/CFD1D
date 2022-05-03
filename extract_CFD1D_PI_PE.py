import os
import sys
import pandas as pd
import numpy as np


class CFG:
    plt_nd_PI_file = str(sys.argv[1])
    plt_nd_PE_file = str(sys.argv[2])
    Proj = str(sys.argv[3])
    Subj = str(sys.argv[4])
    Img1 = str(sys.argv[5])  # TLC0
    Img2 = str(sys.argv[6])  # RV0
    CaseType = str(sys.argv[7])  # tidal
    # Flow = str(sys.argv[7])  # [PI, PE]

def main():
    Config = CFG()
    Proj = Config.Proj
    Subj = Config.Subj
    Img1 = Config.Img1
    Img2 = Config.Img2
    CaseType = Config.CaseType
    plt_nd_PI_path = os.path.join("./data_plt_nd_csv", Config.plt_nd_PI_file)
    plt_nd_PE_path = os.path.join("./data_plt_nd_csv", Config.plt_nd_PE_file)
    save_path = f"{Proj}_{Subj}_CFD1D_{Img1}_{Img2}_{CaseType}_PI_PE.csv"
    save_std_path = f"{Proj}_{Subj}_CFD1D_{Img1}_{Img2}_{CaseType}_PI_PE_std.csv"
    save_n_path = f"{Proj}_{Subj}_CFD1D_{Img1}_{Img2}_{CaseType}_PI_PE_n.csv"

    plt_PI_df = pd.read_csv(plt_nd_PI_path)
    plt_PE_df = pd.read_csv(plt_nd_PE_path)

    df = pd.DataFrame(
        {
            "Proj": [Proj],
            "Subj": [Subj],
            "CaseType": [f"{Img1}_{Img2}_{CaseType}"],
        }
    )

    df_std = pd.DataFrame(
        {
            "Proj": [Proj],
            "Subj": [Subj],
            "CaseType": [f"{Img1}_{Img2}_{CaseType}"],
        }
    )

    df_n = pd.DataFrame(
        {
            "Proj": [Proj],
            "Subj": [Subj],
            "CaseType": [f"{Img1}_{Img2}_{CaseType}"],
        }
    )

    # PI
    df_PI_lu = plt_PI_df[plt_PI_df.i_lobe == 1]
    df_PI_ll = plt_PI_df[plt_PI_df.i_lobe == 2]
    df_PI_ru = plt_PI_df[plt_PI_df.i_lobe == 3]
    df_PI_rm = plt_PI_df[plt_PI_df.i_lobe == 4]
    df_PI_rl = plt_PI_df[plt_PI_df.i_lobe == 5]
    df_PI_all = plt_PI_df[plt_PI_df.i_lobe != 0]

    # Mean pressure at the terminal bronchioles
    Palv_LUL_PI = df_PI_lu[df_PI_lu.i_ho == 1].p
    Palv_LLL_PI = df_PI_ll[df_PI_ll.i_ho == 1].p
    Palv_RUL_PI = df_PI_ru[df_PI_ru.i_ho == 1].p
    Palv_RML_PI = df_PI_rm[df_PI_rm.i_ho == 1].p
    Palv_RLL_PI = df_PI_rl[df_PI_rl.i_ho == 1].p
    Palv_All_PI = df_PI_all[df_PI_all.i_ho == 1].p
    # mean
    df[f"Palv_LUL_PI"] = Palv_LUL_PI.mean()
    df[f"Palv_LLL_PI"] = Palv_LLL_PI.mean()
    df[f"Palv_RUL_PI"] = Palv_RUL_PI.mean()
    df[f"Palv_RML_PI"] = Palv_RML_PI.mean()
    df[f"Palv_RLL_PI"] = Palv_RLL_PI.mean()
    df[f"Palv_All_PI"] = Palv_All_PI.mean()
    # std
    df_std[f"Palv_LUL_PI_sd"] = Palv_LUL_PI.std()
    df_std[f"Palv_LLL_PI_sd"] = Palv_LLL_PI.std()
    df_std[f"Palv_RUL_PI_sd"] = Palv_RUL_PI.std()
    df_std[f"Palv_RML_PI_sd"] = Palv_RML_PI.std()
    df_std[f"Palv_RLL_PI_sd"] = Palv_RLL_PI.std()
    df_std[f"Palv_All_PI_sd"] = Palv_All_PI.std()
    # n
    df_n[f"Palv_LUL_PI_n"] = Palv_LUL_PI.count()
    df_n[f"Palv_LLL_PI_n"] = Palv_LLL_PI.count()
    df_n[f"Palv_RUL_PI_n"] = Palv_RUL_PI.count()
    df_n[f"Palv_RML_PI_n"] = Palv_RML_PI.count()
    df_n[f"Palv_RLL_PI_n"] = Palv_RLL_PI.count()
    df_n[f"Palv_All_PI_n"] = Palv_All_PI.count()

    # Mean transpulmonary pressure at the terminal bronchioles
    Ptp_LUL_PI = df_PI_lu[df_PI_lu.i_ho == 1].p_tp
    Ptp_LLL_PI = df_PI_ll[df_PI_ll.i_ho == 1].p_tp
    Ptp_RUL_PI = df_PI_ru[df_PI_ru.i_ho == 1].p_tp
    Ptp_RML_PI = df_PI_rm[df_PI_rm.i_ho == 1].p_tp
    Ptp_RLL_PI = df_PI_rl[df_PI_rl.i_ho == 1].p_tp
    Ptp_All_PI = df_PI_all[df_PI_all.i_ho == 1].p_tp
    # mean
    df[f"Ptp_LUL_PI"] = Ptp_LUL_PI.mean()
    df[f"Ptp_LLL_PI"] = Ptp_LLL_PI.mean()
    df[f"Ptp_RUL_PI"] = Ptp_RUL_PI.mean()
    df[f"Ptp_RML_PI"] = Ptp_RML_PI.mean()
    df[f"Ptp_RLL_PI"] = Ptp_RLL_PI.mean()
    df[f"Ptp_All_PI"] = Ptp_All_PI.mean()
    # std
    df_std[f"Ptp_LUL_PI_sd"] = Ptp_LUL_PI.std()
    df_std[f"Ptp_LLL_PI_sd"] = Ptp_LLL_PI.std()
    df_std[f"Ptp_RUL_PI_sd"] = Ptp_RUL_PI.std()
    df_std[f"Ptp_RML_PI_sd"] = Ptp_RML_PI.std()
    df_std[f"Ptp_RLL_PI_sd"] = Ptp_RLL_PI.std()
    df_std[f"Ptp_All_PI_sd"] = Ptp_All_PI.std()
    # n
    df_n[f"Ptp_LUL_PI_n"] = Ptp_LUL_PI.count()
    df_n[f"Ptp_LLL_PI_n"] = Ptp_LLL_PI.count()
    df_n[f"Ptp_RUL_PI_n"] = Ptp_RUL_PI.count()
    df_n[f"Ptp_RML_PI_n"] = Ptp_RML_PI.count()
    df_n[f"Ptp_RLL_PI_n"] = Ptp_RLL_PI.count()
    df_n[f"Ptp_All_PI_n"] = Ptp_All_PI.count()

    # Mean Flow rate factions
    FF_LUL_PI = df_PI_lu[df_PI_lu.i_ho == 1].flow_fr
    FF_LLL_PI = df_PI_ll[df_PI_ll.i_ho == 1].flow_fr
    FF_RUL_PI = df_PI_ru[df_PI_ru.i_ho == 1].flow_fr
    FF_RML_PI = df_PI_rm[df_PI_rm.i_ho == 1].flow_fr
    FF_RLL_PI = df_PI_rl[df_PI_rl.i_ho == 1].flow_fr
    FF_All_PI = df_PI_all[df_PI_all.i_ho == 1].flow_fr
    # mean
    df[f"FF_LUL_PI"] = FF_LUL_PI.mean()
    df[f"FF_LLL_PI"] = FF_LLL_PI.mean()
    df[f"FF_RUL_PI"] = FF_RUL_PI.mean()
    df[f"FF_RML_PI"] = FF_RML_PI.mean()
    df[f"FF_RLL_PI"] = FF_RLL_PI.mean()
    df[f"FF_All_PI"] = FF_All_PI.mean()
    # std
    df_std[f"FF_LUL_PI_sd"] = FF_LUL_PI.std()
    df_std[f"FF_LLL_PI_sd"] = FF_LLL_PI.std()
    df_std[f"FF_RUL_PI_sd"] = FF_RUL_PI.std()
    df_std[f"FF_RML_PI_sd"] = FF_RML_PI.std()
    df_std[f"FF_RLL_PI_sd"] = FF_RLL_PI.std()
    df_std[f"FF_All_PI_sd"] = FF_All_PI.std()
    # n
    df_n[f"FF_LUL_PI_n"] = FF_LUL_PI.count()
    df_n[f"FF_LLL_PI_n"] = FF_LLL_PI.count()
    df_n[f"FF_RUL_PI_n"] = FF_RUL_PI.count()
    df_n[f"FF_RML_PI_n"] = FF_RML_PI.count()
    df_n[f"FF_RLL_PI_n"] = FF_RLL_PI.count()
    df_n[f"FF_All_PI_n"] = FF_All_PI.count()

    # flow rate
    FR_LUL_PI = df_PI_lu[df_PI_lu.i_ho == 1].flowrate
    FR_LLL_PI = df_PI_ll[df_PI_ll.i_ho == 1].flowrate
    FR_RUL_PI = df_PI_ru[df_PI_ru.i_ho == 1].flowrate
    FR_RML_PI = df_PI_rm[df_PI_rm.i_ho == 1].flowrate
    FR_RLL_PI = df_PI_rl[df_PI_rl.i_ho == 1].flowrate
    FR_All_PI = df_PI_all[df_PI_all.i_ho == 1].flowrate
    # sum
    df[f"FR_LUL_PI"] = FR_LUL_PI.sum()
    df[f"FR_LLL_PI"] = FR_LLL_PI.sum()
    df[f"FR_RUL_PI"] = FR_RUL_PI.sum()
    df[f"FR_RML_PI"] = FR_RML_PI.sum()
    df[f"FR_RLL_PI"] = FR_RLL_PI.sum()
    df[f"FR_All_PI"] = FR_All_PI.sum()
    # std
    df_std[f"FR_LUL_PI_sd"] = FR_LUL_PI.std()
    df_std[f"FR_LLL_PI_sd"] = FR_LLL_PI.std()
    df_std[f"FR_RUL_PI_sd"] = FR_RUL_PI.std()
    df_std[f"FR_RML_PI_sd"] = FR_RML_PI.std()
    df_std[f"FR_RLL_PI_sd"] = FR_RLL_PI.std()
    df_std[f"FR_All_PI_sd"] = FR_All_PI.std()
    # sum
    df_n[f"FR_LUL_PI_n"] = FR_LUL_PI.count()
    df_n[f"FR_LLL_PI_n"] = FR_LLL_PI.count()
    df_n[f"FR_RUL_PI_n"] = FR_RUL_PI.count()
    df_n[f"FR_RML_PI_n"] = FR_RML_PI.count()
    df_n[f"FR_RLL_PI_n"] = FR_RLL_PI.count()
    df_n[f"FR_All_PI_n"] = FR_All_PI.count()

    # airway resistance = pressure /flow_rate
    AR_LUL_PI = np.abs(Palv_LUL_PI / FR_LUL_PI)
    AR_LLL_PI = np.abs(Palv_LLL_PI / FR_LLL_PI)
    AR_RUL_PI = np.abs(Palv_RUL_PI / FR_RUL_PI)
    AR_RML_PI = np.abs(Palv_RML_PI / FR_RML_PI)
    AR_RLL_PI = np.abs(Palv_RLL_PI / FR_RLL_PI)
    AR_All_PI = np.abs(Palv_All_PI / FR_All_PI)
    # mean
    df[f"R_LUL_PI"] = AR_LUL_PI.mean()
    df[f"R_LLL_PI"] = AR_LLL_PI.mean()
    df[f"R_RUL_PI"] = AR_RUL_PI.mean()
    df[f"R_RML_PI"] = AR_RML_PI.mean()
    df[f"R_RLL_PI"] = AR_RLL_PI.mean()
    df[f"R_All_PI"] = AR_All_PI.mean()
    # std
    df_std[f"R_LUL_PI_sd"] = AR_LUL_PI.std()
    df_std[f"R_LLL_PI_sd"] = AR_LLL_PI.std()
    df_std[f"R_RUL_PI_sd"] = AR_RUL_PI.std()
    df_std[f"R_RML_PI_sd"] = AR_RML_PI.std()
    df_std[f"R_RLL_PI_sd"] = AR_RLL_PI.std()
    df_std[f"R_All_PI_sd"] = AR_All_PI.std()
    # mean
    df_n[f"R_LUL_PI_n"] = AR_LUL_PI.count()
    df_n[f"R_LLL_PI_n"] = AR_LLL_PI.count()
    df_n[f"R_RUL_PI_n"] = AR_RUL_PI.count()
    df_n[f"R_RML_PI_n"] = AR_RML_PI.count()
    df_n[f"R_RLL_PI_n"] = AR_RLL_PI.count()
    df_n[f"R_All_PI_n"] = AR_All_PI.count()

    # Pressure work = Palv * FR PalvFR
    PQ_LUL_PI = Palv_LUL_PI * FR_LUL_PI
    PQ_LLL_PI = Palv_LLL_PI * FR_LLL_PI
    PQ_RUL_PI = Palv_RUL_PI * FR_RUL_PI
    PQ_RML_PI = Palv_RML_PI * FR_RML_PI
    PQ_RLL_PI = Palv_RLL_PI * FR_RLL_PI
    PQ_All_PI = Palv_All_PI * FR_All_PI
    # mean
    df[f"PalvFR_LUL_PI"] = PQ_LUL_PI.mean()
    df[f"PalvFR_LLL_PI"] = PQ_LLL_PI.mean()
    df[f"PalvFR_RUL_PI"] = PQ_RUL_PI.mean()
    df[f"PalvFR_RML_PI"] = PQ_RML_PI.mean()
    df[f"PalvFR_RLL_PI"] = PQ_RLL_PI.mean()
    df[f"PalvFR_All_PI"] = PQ_All_PI.mean()
    # std
    df_std[f"PalvFR_LUL_PI_sd"] = PQ_LUL_PI.std()
    df_std[f"PalvFR_LLL_PI_sd"] = PQ_LLL_PI.std()
    df_std[f"PalvFR_RUL_PI_sd"] = PQ_RUL_PI.std()
    df_std[f"PalvFR_RML_PI_sd"] = PQ_RML_PI.std()
    df_std[f"PalvFR_RLL_PI_sd"] = PQ_RLL_PI.std()
    df_std[f"PalvFR_All_PI_sd"] = PQ_All_PI.std()
    # n
    df_n[f"PalvFR_LUL_PI_n"] = PQ_LUL_PI.count()
    df_n[f"PalvFR_LLL_PI_n"] = PQ_LLL_PI.count()
    df_n[f"PalvFR_RUL_PI_n"] = PQ_RUL_PI.count()
    df_n[f"PalvFR_RML_PI_n"] = PQ_RML_PI.count()
    df_n[f"PalvFR_RLL_PI_n"] = PQ_RLL_PI.count()
    df_n[f"PalvFR_All_PI_n"] = PQ_All_PI.count()


    # PE
    df_PE_lu = plt_PE_df[plt_PE_df.i_lobe == 1]
    df_PE_ll = plt_PE_df[plt_PE_df.i_lobe == 2]
    df_PE_ru = plt_PE_df[plt_PE_df.i_lobe == 3]
    df_PE_rm = plt_PE_df[plt_PE_df.i_lobe == 4]
    df_PE_rl = plt_PE_df[plt_PE_df.i_lobe == 5]
    df_PE_all = plt_PE_df[plt_PE_df.i_lobe != 0]

    # Mean pressure at the terminal bronchioles
    Palv_LUL_PE = df_PE_lu[df_PE_lu.i_ho == 1].p
    Palv_LLL_PE = df_PE_ll[df_PE_ll.i_ho == 1].p
    Palv_RUL_PE = df_PE_ru[df_PE_ru.i_ho == 1].p
    Palv_RML_PE = df_PE_rm[df_PE_rm.i_ho == 1].p
    Palv_RLL_PE = df_PE_rl[df_PE_rl.i_ho == 1].p
    Palv_All_PE = df_PE_all[df_PE_all.i_ho == 1].p
    # mean
    df[f"Palv_LUL_PE"] = Palv_LUL_PE.mean()
    df[f"Palv_LLL_PE"] = Palv_LLL_PE.mean()
    df[f"Palv_RUL_PE"] = Palv_RUL_PE.mean()
    df[f"Palv_RML_PE"] = Palv_RML_PE.mean()
    df[f"Palv_RLL_PE"] = Palv_RLL_PE.mean()
    df[f"Palv_All_PE"] = Palv_All_PE.mean()
    # std
    df_std[f"Palv_LUL_PE_sd"] = Palv_LUL_PE.std()
    df_std[f"Palv_LLL_PE_sd"] = Palv_LLL_PE.std()
    df_std[f"Palv_RUL_PE_sd"] = Palv_RUL_PE.std()
    df_std[f"Palv_RML_PE_sd"] = Palv_RML_PE.std()
    df_std[f"Palv_RLL_PE_sd"] = Palv_RLL_PE.std()
    df_std[f"Palv_All_PE_sd"] = Palv_All_PE.std()
    # n
    df_n[f"Palv_LUL_PE_n"] = Palv_LUL_PE.count()
    df_n[f"Palv_LLL_PE_n"] = Palv_LLL_PE.count()
    df_n[f"Palv_RUL_PE_n"] = Palv_RUL_PE.count()
    df_n[f"Palv_RML_PE_n"] = Palv_RML_PE.count()
    df_n[f"Palv_RLL_PE_n"] = Palv_RLL_PE.count()
    df_n[f"Palv_All_PE_n"] = Palv_All_PE.count()

    # Mean transpulmonary pressure at the terminal bronchioles
    Ptp_LUL_PE = df_PE_lu[df_PE_lu.i_ho == 1].p_tp
    Ptp_LLL_PE = df_PE_ll[df_PE_ll.i_ho == 1].p_tp
    Ptp_RUL_PE = df_PE_ru[df_PE_ru.i_ho == 1].p_tp
    Ptp_RML_PE = df_PE_rm[df_PE_rm.i_ho == 1].p_tp
    Ptp_RLL_PE = df_PE_rl[df_PE_rl.i_ho == 1].p_tp
    Ptp_All_PE = df_PE_all[df_PE_all.i_ho == 1].p_tp
    # mean
    df[f"Ptp_LUL_PE"] = Ptp_LUL_PE.mean()
    df[f"Ptp_LLL_PE"] = Ptp_LLL_PE.mean()
    df[f"Ptp_RUL_PE"] = Ptp_RUL_PE.mean()
    df[f"Ptp_RML_PE"] = Ptp_RML_PE.mean()
    df[f"Ptp_RLL_PE"] = Ptp_RLL_PE.mean()
    df[f"Ptp_All_PE"] = Ptp_All_PE.mean()
    # std
    df_std[f"Ptp_LUL_PE_sd"] = Ptp_LUL_PE.std()
    df_std[f"Ptp_LLL_PE_sd"] = Ptp_LLL_PE.std()
    df_std[f"Ptp_RUL_PE_sd"] = Ptp_RUL_PE.std()
    df_std[f"Ptp_RML_PE_sd"] = Ptp_RML_PE.std()
    df_std[f"Ptp_RLL_PE_sd"] = Ptp_RLL_PE.std()
    df_std[f"Ptp_All_PE_sd"] = Ptp_All_PE.std()
    # n
    df_n[f"Ptp_LUL_PE_n"] = Ptp_LUL_PE.count()
    df_n[f"Ptp_LLL_PE_n"] = Ptp_LLL_PE.count()
    df_n[f"Ptp_RUL_PE_n"] = Ptp_RUL_PE.count()
    df_n[f"Ptp_RML_PE_n"] = Ptp_RML_PE.count()
    df_n[f"Ptp_RLL_PE_n"] = Ptp_RLL_PE.count()
    df_n[f"Ptp_All_PE_n"] = Ptp_All_PE.count()

    # Mean Flow rate factions
    FF_LUL_PE = df_PE_lu[df_PE_lu.i_ho == 1].flow_fr
    FF_LLL_PE = df_PE_ll[df_PE_ll.i_ho == 1].flow_fr
    FF_RUL_PE = df_PE_ru[df_PE_ru.i_ho == 1].flow_fr
    FF_RML_PE = df_PE_rm[df_PE_rm.i_ho == 1].flow_fr
    FF_RLL_PE = df_PE_rl[df_PE_rl.i_ho == 1].flow_fr
    FF_All_PE = df_PE_all[df_PE_all.i_ho == 1].flow_fr
    # mean
    df[f"FF_LUL_PE"] = FF_LUL_PE.mean()
    df[f"FF_LLL_PE"] = FF_LLL_PE.mean()
    df[f"FF_RUL_PE"] = FF_RUL_PE.mean()
    df[f"FF_RML_PE"] = FF_RML_PE.mean()
    df[f"FF_RLL_PE"] = FF_RLL_PE.mean()
    df[f"FF_All_PE"] = FF_All_PE.mean()
    # std
    df_std[f"FF_LUL_PE_sd"] = FF_LUL_PE.std()
    df_std[f"FF_LLL_PE_sd"] = FF_LLL_PE.std()
    df_std[f"FF_RUL_PE_sd"] = FF_RUL_PE.std()
    df_std[f"FF_RML_PE_sd"] = FF_RML_PE.std()
    df_std[f"FF_RLL_PE_sd"] = FF_RLL_PE.std()
    df_std[f"FF_All_PE_sd"] = FF_All_PE.std()
    # n
    df_n[f"FF_LUL_PE_n"] = FF_LUL_PE.count()
    df_n[f"FF_LLL_PE_n"] = FF_LLL_PE.count()
    df_n[f"FF_RUL_PE_n"] = FF_RUL_PE.count()
    df_n[f"FF_RML_PE_n"] = FF_RML_PE.count()
    df_n[f"FF_RLL_PE_n"] = FF_RLL_PE.count()
    df_n[f"FF_All_PE_n"] = FF_All_PE.count()

    # flow rate
    FR_LUL_PE = df_PE_lu[df_PE_lu.i_ho == 1].flowrate
    FR_LLL_PE = df_PE_ll[df_PE_ll.i_ho == 1].flowrate
    FR_RUL_PE = df_PE_ru[df_PE_ru.i_ho == 1].flowrate
    FR_RML_PE = df_PE_rm[df_PE_rm.i_ho == 1].flowrate
    FR_RLL_PE = df_PE_rl[df_PE_rl.i_ho == 1].flowrate
    FR_All_PE = df_PE_all[df_PE_all.i_ho == 1].flowrate
    # sum
    df[f"FR_LUL_PE"] = FR_LUL_PE.sum()
    df[f"FR_LLL_PE"] = FR_LLL_PE.sum()
    df[f"FR_RUL_PE"] = FR_RUL_PE.sum()
    df[f"FR_RML_PE"] = FR_RML_PE.sum()
    df[f"FR_RLL_PE"] = FR_RLL_PE.sum()
    df[f"FR_All_PE"] = FR_All_PE.sum()
    # std
    df_std[f"FR_LUL_PE_sd"] = FR_LUL_PE.std()
    df_std[f"FR_LLL_PE_sd"] = FR_LLL_PE.std()
    df_std[f"FR_RUL_PE_sd"] = FR_RUL_PE.std()
    df_std[f"FR_RML_PE_sd"] = FR_RML_PE.std()
    df_std[f"FR_RLL_PE_sd"] = FR_RLL_PE.std()
    df_std[f"FR_All_PE_sd"] = FR_All_PE.std()
    # sum
    df_n[f"FR_LUL_PE_n"] = FR_LUL_PE.count()
    df_n[f"FR_LLL_PE_n"] = FR_LLL_PE.count()
    df_n[f"FR_RUL_PE_n"] = FR_RUL_PE.count()
    df_n[f"FR_RML_PE_n"] = FR_RML_PE.count()
    df_n[f"FR_RLL_PE_n"] = FR_RLL_PE.count()
    df_n[f"FR_All_PE_n"] = FR_All_PE.count()

    # airway resistance = pressure /flow_rate
    AR_LUL_PE = np.abs(Palv_LUL_PE / FR_LUL_PE)
    AR_LLL_PE = np.abs(Palv_LLL_PE / FR_LLL_PE)
    AR_RUL_PE = np.abs(Palv_RUL_PE / FR_RUL_PE)
    AR_RML_PE = np.abs(Palv_RML_PE / FR_RML_PE)
    AR_RLL_PE = np.abs(Palv_RLL_PE / FR_RLL_PE)
    AR_All_PE = np.abs(Palv_All_PE / FR_All_PE)
    # mean
    df[f"R_LUL_PE"] = AR_LUL_PE.mean()
    df[f"R_LLL_PE"] = AR_LLL_PE.mean()
    df[f"R_RUL_PE"] = AR_RUL_PE.mean()
    df[f"R_RML_PE"] = AR_RML_PE.mean()
    df[f"R_RLL_PE"] = AR_RLL_PE.mean()
    df[f"R_All_PE"] = AR_All_PE.mean()
    # std
    df_std[f"R_LUL_PE_sd"] = AR_LUL_PE.std()
    df_std[f"R_LLL_PE_sd"] = AR_LLL_PE.std()
    df_std[f"R_RUL_PE_sd"] = AR_RUL_PE.std()
    df_std[f"R_RML_PE_sd"] = AR_RML_PE.std()
    df_std[f"R_RLL_PE_sd"] = AR_RLL_PE.std()
    df_std[f"R_All_PE_sd"] = AR_All_PE.std()
    # mean
    df_n[f"R_LUL_PE_n"] = AR_LUL_PE.count()
    df_n[f"R_LLL_PE_n"] = AR_LLL_PE.count()
    df_n[f"R_RUL_PE_n"] = AR_RUL_PE.count()
    df_n[f"R_RML_PE_n"] = AR_RML_PE.count()
    df_n[f"R_RLL_PE_n"] = AR_RLL_PE.count()
    df_n[f"R_All_PE_n"] = AR_All_PE.count()

    # Pressure work = Palv * FR PalvFR
    PQ_LUL_PE = Palv_LUL_PE * FR_LUL_PE
    PQ_LLL_PE = Palv_LLL_PE * FR_LLL_PE
    PQ_RUL_PE = Palv_RUL_PE * FR_RUL_PE
    PQ_RML_PE = Palv_RML_PE * FR_RML_PE
    PQ_RLL_PE = Palv_RLL_PE * FR_RLL_PE
    PQ_All_PE = Palv_All_PE * FR_All_PE
    # mean
    df[f"PalvFR_LUL_PE"] = PQ_LUL_PE.mean()
    df[f"PalvFR_LLL_PE"] = PQ_LLL_PE.mean()
    df[f"PalvFR_RUL_PE"] = PQ_RUL_PE.mean()
    df[f"PalvFR_RML_PE"] = PQ_RML_PE.mean()
    df[f"PalvFR_RLL_PE"] = PQ_RLL_PE.mean()
    df[f"PalvFR_All_PE"] = PQ_All_PE.mean()
    # std
    df_std[f"PalvFR_LUL_PE_sd"] = PQ_LUL_PE.std()
    df_std[f"PalvFR_LLL_PE_sd"] = PQ_LLL_PE.std()
    df_std[f"PalvFR_RUL_PE_sd"] = PQ_RUL_PE.std()
    df_std[f"PalvFR_RML_PE_sd"] = PQ_RML_PE.std()
    df_std[f"PalvFR_RLL_PE_sd"] = PQ_RLL_PE.std()
    df_std[f"PalvFR_All_PE_sd"] = PQ_All_PE.std()
    # n
    df_n[f"PalvFR_LUL_PE_n"] = PQ_LUL_PE.count()
    df_n[f"PalvFR_LLL_PE_n"] = PQ_LLL_PE.count()
    df_n[f"PalvFR_RUL_PE_n"] = PQ_RUL_PE.count()
    df_n[f"PalvFR_RML_PE_n"] = PQ_RML_PE.count()
    df_n[f"PalvFR_RLL_PE_n"] = PQ_RLL_PE.count()
    df_n[f"PalvFR_All_PE_n"] = PQ_All_PE.count()

    # Save the result
    df.to_csv(save_path, index=False)
    df_std.to_csv(save_std_path, index=False)
    df_n.to_csv(save_n_path, index=False)


if __name__ == "__main__":
    main()
