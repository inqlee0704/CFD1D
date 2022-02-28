import os
import sys
import pandas as pd
import numpy as np


class CFG:
    plt_nd_file = str(sys.argv[1])
    Proj = str(sys.argv[2])
    Subj = str(sys.argv[3])
    Img1 = str(sys.argv[4])  # TLC0
    Img2 = str(sys.argv[5])  # RV0
    CaseType = str(sys.argv[6])  # tidal
    Flow = str(sys.argv[7])  # [PI, PE]


def main():
    Config = CFG()
    Proj = Config.Proj
    Subj = Config.Subj
    Img1 = Config.Img1
    Img2 = Config.Img2
    CaseType = Config.CaseType
    Flow = Config.Flow
    plt_nd_path = os.path.join("./data_plt_nd_csv", Config.plt_nd_file)
    save_path = f"{Proj}_{Subj}_CFD1D_{Img1}_{Img2}_{CaseType}_{Flow}.csv"
    plt_df = pd.read_csv(plt_nd_path)
    df = pd.DataFrame(
        {
            "Proj": [Proj],
            "Subj": [Subj],
            "CaseType": [f"{Img1}_{Img2}_{CaseType}"],
            "FlowPhase": [Flow]
        }
    )

    df_lu = plt_df[plt_df.i_lobe == 1]
    df_ll = plt_df[plt_df.i_lobe == 2]
    df_ru = plt_df[plt_df.i_lobe == 3]
    df_rm = plt_df[plt_df.i_lobe == 4]
    df_rl = plt_df[plt_df.i_lobe == 5]
    df_all = plt_df[plt_df.i_lobe != 0]

    # Mean pressure at the terminal bronchioles
    df[f"Palv_LUL"] = df_lu[df_lu.i_ho == 1].p.mean()
    df[f"Palv_LLL"] = df_ll[df_ll.i_ho == 1].p.mean()
    df[f"Palv_RUL"] = df_ru[df_ru.i_ho == 1].p.mean()
    df[f"Palv_RML"] = df_rm[df_rm.i_ho == 1].p.mean()
    df[f"Palv_RLL"] = df_rl[df_rl.i_ho == 1].p.mean()
    df[f"Palv_All"] = df_all[df_all.i_ho == 1].p.mean()

    # Mean transpulmonary pressure at the terminal bronchioles
    df[f"Ptp_LUL"] = df_lu[df_lu.i_ho == 1].p_tp.mean()
    df[f"Ptp_LLL"] = df_ll[df_ll.i_ho == 1].p_tp.mean()
    df[f"Ptp_RUL"] = df_ru[df_ru.i_ho == 1].p_tp.mean()
    df[f"Ptp_RML"] = df_rm[df_rm.i_ho == 1].p_tp.mean()
    df[f"Ptp_RLL"] = df_rl[df_rl.i_ho == 1].p_tp.mean()
    df[f"Ptp_All"] = df_all[df_all.i_ho == 1].p_tp.mean()

    # Mean Flow rate factions
    df[f"FF_LUL"] = df_lu[df_lu.i_ho == 1].flow_fr.mean()
    df[f"FF_LLL"] = df_ll[df_ll.i_ho == 1].flow_fr.mean()
    df[f"FF_RUL"] = df_ru[df_ru.i_ho == 1].flow_fr.mean()
    df[f"FF_RML"] = df_rm[df_rm.i_ho == 1].flow_fr.mean()
    df[f"FF_RLL"] = df_rl[df_rl.i_ho == 1].flow_fr.mean()
    df[f"FF_ALL"] = df_all[df_all.i_ho == 1].flow_fr.mean()

    # flow rate
    df[f"FR_LUL"] = df_lu[df_lu.i_ho == 1].flowrate.sum()
    df[f"FR_LLL"] = df_ll[df_ll.i_ho == 1].flowrate.sum()
    df[f"FR_RUL"] = df_ru[df_ru.i_ho == 1].flowrate.sum()
    df[f"FR_RML"] = df_rm[df_rm.i_ho == 1].flowrate.sum()
    df[f"FR_RLL"] = df_rl[df_rl.i_ho == 1].flowrate.sum()
    df[f"FR_ALL"] = df_all[df_all.i_ho == 1].flowrate.sum()

    # airway resistance = pressure /flow_rate
    df[f"R_LUL"] = np.abs(
        df[f"Palv_LUL"] / df[f"FF_LUL"]
    )
    df[f"R_LLL"] = np.abs(
        df[f"Palv_LLL"] / df[f"FF_LLL"]
    )
    df[f"R_RUL"] = np.abs(
        df[f"Palv_RUL"] / df[f"FF_RUL"]
    )
    df[f"R_RML"] = np.abs(
        df[f"Palv_RML"] / df[f"FF_RML"]
    )
    df[f"R_RLL"] = np.abs(
        df[f"Palv_RLL"] / df[f"FF_RLL"]
    )
    df[f"R_ALL"] = np.abs(
        df[f"Palv_All"] / df[f"FF_ALL"]
    )

    # Save it
    df.to_csv(save_path, index=False)


if __name__ == "__main__":
    main()
