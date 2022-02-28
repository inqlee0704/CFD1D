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
    plt_PI_df = pd.read_csv(plt_nd_PI_path)
    plt_PE_df = pd.read_csv(plt_nd_PE_path)

    df = pd.DataFrame(
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
    df[f"Palv_LUL_PI"] = df_PI_lu[df_PI_lu.i_ho == 1].p.mean()
    df[f"Palv_LLL_PI"] = df_PI_ll[df_PI_ll.i_ho == 1].p.mean()
    df[f"Palv_RUL_PI"] = df_PI_ru[df_PI_ru.i_ho == 1].p.mean()
    df[f"Palv_RML_PI"] = df_PI_rm[df_PI_rm.i_ho == 1].p.mean()
    df[f"Palv_RLL_PI"] = df_PI_rl[df_PI_rl.i_ho == 1].p.mean()
    df[f"Palv_All_PI"] = df_PI_all[df_PI_all.i_ho == 1].p.mean()

    # Mean transpulmonary pressure at the terminal bronchioles
    df[f"Ptp_LUL_PI"] = df_PI_lu[df_PI_lu.i_ho == 1].p_tp.mean()
    df[f"Ptp_LLL_PI"] = df_PI_ll[df_PI_ll.i_ho == 1].p_tp.mean()
    df[f"Ptp_RUL_PI"] = df_PI_ru[df_PI_ru.i_ho == 1].p_tp.mean()
    df[f"Ptp_RML_PI"] = df_PI_rm[df_PI_rm.i_ho == 1].p_tp.mean()
    df[f"Ptp_RLL_PI"] = df_PI_rl[df_PI_rl.i_ho == 1].p_tp.mean()
    df[f"Ptp_All_PI"] = df_PI_all[df_PI_all.i_ho == 1].p_tp.mean()

    # Mean Flow rate factions
    df[f"FF_LUL_PI"] = df_PI_lu[df_PI_lu.i_ho == 1].flow_fr.mean()
    df[f"FF_LLL_PI"] = df_PI_ll[df_PI_ll.i_ho == 1].flow_fr.mean()
    df[f"FF_RUL_PI"] = df_PI_ru[df_PI_ru.i_ho == 1].flow_fr.mean()
    df[f"FF_RML_PI"] = df_PI_rm[df_PI_rm.i_ho == 1].flow_fr.mean()
    df[f"FF_RLL_PI"] = df_PI_rl[df_PI_rl.i_ho == 1].flow_fr.mean()
    df[f"FF_ALL_PI"] = df_PI_all[df_PI_all.i_ho == 1].flow_fr.mean()

    # flow rate
    df[f"FR_LUL_PI"] = df_PI_lu[df_PI_lu.i_ho == 1].flowrate.sum()
    df[f"FR_LLL_PI"] = df_PI_ll[df_PI_ll.i_ho == 1].flowrate.sum()
    df[f"FR_RUL_PI"] = df_PI_ru[df_PI_ru.i_ho == 1].flowrate.sum()
    df[f"FR_RML_PI"] = df_PI_rm[df_PI_rm.i_ho == 1].flowrate.sum()
    df[f"FR_RLL_PI"] = df_PI_rl[df_PI_rl.i_ho == 1].flowrate.sum()
    df[f"FR_ALL_PI"] = df_PI_all[df_PI_all.i_ho == 1].flowrate.sum()

    # airway resistance = pressure /flow_rate
    df[f"R_LUL_PI"] = np.abs(
        df[f"Palv_LUL_PI"] / df[f"FF_LUL_PI"]
    )
    df[f"R_LLL_PI"] = np.abs(
        df[f"Palv_LLL_PI"] / df[f"FF_LLL_PI"]
    )
    df[f"R_RUL_PI"] = np.abs(
        df[f"Palv_RUL_PI"] / df[f"FF_RUL_PI"]
    )
    df[f"R_RML_PI"] = np.abs(
        df[f"Palv_RML_PI"] / df[f"FF_RML_PI"]
    )
    df[f"R_RLL_PI"] = np.abs(
        df[f"Palv_RLL_PI"] / df[f"FF_RLL_PI"]
    )
    df[f"R_ALL_PI"] = np.abs(
        df[f"Palv_All_PI"] / df[f"FF_ALL_PI"]
    )

    # PE
    df_PE_lu = plt_PE_df[plt_PE_df.i_lobe == 1]
    df_PE_ll = plt_PE_df[plt_PE_df.i_lobe == 2]
    df_PE_ru = plt_PE_df[plt_PE_df.i_lobe == 3]
    df_PE_rm = plt_PE_df[plt_PE_df.i_lobe == 4]
    df_PE_rl = plt_PE_df[plt_PE_df.i_lobe == 5]
    df_PE_all = plt_PE_df[plt_PE_df.i_lobe != 0]

    # Mean pressure at the terminal bronchioles
    df[f"Palv_LUL_PE"] = df_PE_lu[df_PE_lu.i_ho == 1].p.mean()
    df[f"Palv_LLL_PE"] = df_PE_ll[df_PE_ll.i_ho == 1].p.mean()
    df[f"Palv_RUL_PE"] = df_PE_ru[df_PE_ru.i_ho == 1].p.mean()
    df[f"Palv_RML_PE"] = df_PE_rm[df_PE_rm.i_ho == 1].p.mean()
    df[f"Palv_RLL_PE"] = df_PE_rl[df_PE_rl.i_ho == 1].p.mean()
    df[f"Palv_All_PE"] = df_PE_all[df_PE_all.i_ho == 1].p.mean()

    # Mean transpulmonary pressure at the terminal bronchioles
    df[f"Ptp_LUL_PE"] = df_PE_lu[df_PE_lu.i_ho == 1].p_tp.mean()
    df[f"Ptp_LLL_PE"] = df_PE_ll[df_PE_ll.i_ho == 1].p_tp.mean()
    df[f"Ptp_RUL_PE"] = df_PE_ru[df_PE_ru.i_ho == 1].p_tp.mean()
    df[f"Ptp_RML_PE"] = df_PE_rm[df_PE_rm.i_ho == 1].p_tp.mean()
    df[f"Ptp_RLL_PE"] = df_PE_rl[df_PE_rl.i_ho == 1].p_tp.mean()
    df[f"Ptp_All_PE"] = df_PE_all[df_PE_all.i_ho == 1].p_tp.mean()

    # Mean Flow rate factions
    df[f"FF_LUL_PE"] = df_PE_lu[df_PE_lu.i_ho == 1].flow_fr.mean()
    df[f"FF_LLL_PE"] = df_PE_ll[df_PE_ll.i_ho == 1].flow_fr.mean()
    df[f"FF_RUL_PE"] = df_PE_ru[df_PE_ru.i_ho == 1].flow_fr.mean()
    df[f"FF_RML_PE"] = df_PE_rm[df_PE_rm.i_ho == 1].flow_fr.mean()
    df[f"FF_RLL_PE"] = df_PE_rl[df_PE_rl.i_ho == 1].flow_fr.mean()
    df[f"FF_ALL_PE"] = df_PE_all[df_PE_all.i_ho == 1].flow_fr.mean()

    # flow rate
    df[f"FR_LUL_PE"] = df_PE_lu[df_PE_lu.i_ho == 1].flowrate.sum()
    df[f"FR_LLL_PE"] = df_PE_ll[df_PE_ll.i_ho == 1].flowrate.sum()
    df[f"FR_RUL_PE"] = df_PE_ru[df_PE_ru.i_ho == 1].flowrate.sum()
    df[f"FR_RML_PE"] = df_PE_rm[df_PE_rm.i_ho == 1].flowrate.sum()
    df[f"FR_RLL_PE"] = df_PE_rl[df_PE_rl.i_ho == 1].flowrate.sum()
    df[f"FR_ALL_PE"] = df_PE_all[df_PE_all.i_ho == 1].flowrate.sum()

    # airway resistance = pressure /flow_rate
    df[f"R_LUL_PE"] = np.abs(
        df[f"Palv_LUL_PE"] / df[f"FF_LUL_PE"]
    )
    df[f"R_LLL_PE"] = np.abs(
        df[f"Palv_LLL_PE"] / df[f"FF_LLL_PE"]
    )
    df[f"R_RUL_PE"] = np.abs(
        df[f"Palv_RUL_PE"] / df[f"FF_RUL_PE"]
    )
    df[f"R_RML_PE"] = np.abs(
        df[f"Palv_RML_PE"] / df[f"FF_RML_PE"]
    )
    df[f"R_RLL_PE"] = np.abs(
        df[f"Palv_RLL_PE"] / df[f"FF_RLL_PE"]
    )
    df[f"R_ALL_PE"] = np.abs(
        df[f"Palv_All_PE"] / df[f"FF_ALL_PE"]
    )

    # Save the result
    df.to_csv(save_path, index=False)


if __name__ == "__main__":
    main()
