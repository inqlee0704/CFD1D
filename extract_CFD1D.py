import os
import sys
import pandas as pd
import numpy as np

class CFG:
    plt_nd_file = str(sys.argv[1])
    Proj = str(sys.argv[2])
    Subj = str(sys.argv[3])
    Img1 = str(sys.argv[4])
    Img2 = str(sys.argv[5])
    Flow = str(sys.argv[6])

def main():
    Config = CFG()
    Proj = Config.Proj
    Subj = Config.Subj
    Img1 = Config.Img1
    Img2 = Config.Img2
    Flow = Config.Flow
    plt_nd_path = os.path.join('./data_plt_nd_csv',Config.plt_nd_file)
    # save_path = os.path.join('./data_plt_nd_csv',f"{Proj}_{Subj}_{Img1}_{Img2}_{Flow}_CFD1D.csv")
    save_path = f"{Proj}_{Subj}_{Img1}_{Img2}_{Flow}_CFD1D.csv"
    plt_df = pd.read_csv(plt_nd_path)
    df = pd.DataFrame({"Proj": [Proj], "Subj": [Subj]})

    df_lu = plt_df[plt_df.i_lobe==1]
    df_ll = plt_df[plt_df.i_lobe==2]
    df_ru = plt_df[plt_df.i_lobe==3]
    df_rm = plt_df[plt_df.i_lobe==4]
    df_rl = plt_df[plt_df.i_lobe==5]
    df_all = plt_df[plt_df.i_lobe!=0]
    
    # Mean pressure at the terminal bronchioles
    df[f"P_t_LUL_{Img1}_{Img2}"] = df_lu[df_lu.i_ho==1].p.mean()
    df[f"P_t_LLL_{Img1}_{Img2}"] = df_ll[df_ll.i_ho==1].p.mean()
    df[f"P_t_RUL_{Img1}_{Img2}"] = df_ru[df_ru.i_ho==1].p.mean()
    df[f"P_t_RML_{Img1}_{Img2}"] = df_rm[df_rm.i_ho==1].p.mean()
    df[f"P_t_RLL_{Img1}_{Img2}"] = df_rl[df_rl.i_ho==1].p.mean()
    df[f"P_t_All_{Img1}_{Img2}"] = df_all[df_all.i_ho==1].p.mean()

    # Mean Flow rate factions
    df[f"FF_LUL_{Img1}_{Img2}"] = df_lu[df_lu.i_ho==1].flow_fr.mean()
    df[f"FF_LLL_{Img1}_{Img2}"] = df_ll[df_ll.i_ho==1].flow_fr.mean()
    df[f"FF_RUL_{Img1}_{Img2}"] = df_ru[df_ru.i_ho==1].flow_fr.mean()
    df[f"FF_RML_{Img1}_{Img2}"] = df_rm[df_rm.i_ho==1].flow_fr.mean()
    df[f"FF_RLL_{Img1}_{Img2}"] = df_rl[df_rl.i_ho==1].flow_fr.mean()
    df[f"FF_ALL_{Img1}_{Img2}"] = df_all[df_all.i_ho==1].flow_fr.mean()

    # flow rate
    df[f"FR_LUL_{Img1}_{Img2}"] = df_lu[df_lu.i_ho==1].flowrate.sum()
    df[f"FR_LLL_{Img1}_{Img2}"] = df_ll[df_ll.i_ho==1].flowrate.sum()
    df[f"FR_RUL_{Img1}_{Img2}"] = df_ru[df_ru.i_ho==1].flowrate.sum()
    df[f"FR_RML_{Img1}_{Img2}"] = df_rm[df_rm.i_ho==1].flowrate.sum()
    df[f"FR_RLL_{Img1}_{Img2}"] = df_rl[df_rl.i_ho==1].flowrate.sum()
    df[f"FR_ALL_{Img1}_{Img2}"] = df_all[df_all.i_ho==1].flowrate.sum()

    # airway resistance = pressure /flow_rate
    df[f"AR_LUL_{Img1}_{Img2}"] = np.abs(df[f"P_t_LUL_{Img1}_{Img2}"]/df[f"FF_LUL_{Img1}_{Img2}"])
    df[f"AR_LLL_{Img1}_{Img2}"] = np.abs(df[f"P_t_LLL_{Img1}_{Img2}"]/df[f"FF_LLL_{Img1}_{Img2}"])
    df[f"AR_RUL_{Img1}_{Img2}"] = np.abs(df[f"P_t_RUL_{Img1}_{Img2}"]/df[f"FF_RUL_{Img1}_{Img2}"])
    df[f"AR_RML_{Img1}_{Img2}"] = np.abs(df[f"P_t_RML_{Img1}_{Img2}"]/df[f"FF_RML_{Img1}_{Img2}"])
    df[f"AR_RLL_{Img1}_{Img2}"] = np.abs(df[f"P_t_RLL_{Img1}_{Img2}"]/df[f"FF_RLL_{Img1}_{Img2}"])
    df[f"AR_ALL_{Img1}_{Img2}"] = np.abs(df[f"P_t_All_{Img1}_{Img2}"]/df[f"FF_ALL_{Img1}_{Img2}"])

    # Save it
    df.to_csv(save_path, index=False)

if __name__ == "__main__":
    main()