import sys
import pandas as pd

df_QCT_path = str(sys.argv[1])
df_CFD_path = str(sys.argv[2])
save_path = str(sys.argv[3])

df_QCT = pd.read_csv(df_QCT_path)
df_CFD = pd.read_csv(df_CFD_path)

combined_df = df_QCT.merge(df_CFD, how='left', on=['Proj','Subj'])
combined_df.to_csv(save_path, index=False)