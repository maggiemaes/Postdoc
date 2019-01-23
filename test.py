import numpy as np
import pandas as pd
import glob 
import os


# def test():
# #read in files
# #df = pd.concat([pd.read_csv(f, na_values = ' ', header = 2, error_bad_lines = False).fillna(0) for f in glob.glob('/Users/mmaes/Documents/Siegert_Lab/Shared_Drive_local/Python_scripts/raw_data/**/*.csv')], ignore_index = True)
# file1 =pd.read_csv('/Users/mmaes/Documents/Siegert_Lab/Shared_Drive_local/Python_scripts/raw_data/20180614_male1_od2_ipl_mitolyso_Detailed.csv', na_values = " ", delimiter = ',', quotechar = '|', header = 2, error_bad_lines = False).fillna(0)
# #file2 =pd.read_csv('/Users/mmaes/Documents/Siegert_Lab/Shared_Drive_local/Python_scripts/raw_data/20180614_male1_od1_gclipl_cd68_Statistics/20180614_male1_od1_gclipl_cd68_Detailed.csv', na_values = "0", header = 2)
# #print(df)
# for f in glob.glob('/Users/mmaes/Documents/Siegert_Lab/Shared_Drive_local/Python_scripts/raw_data/**/*.csv'): 
#   data = pd.read_csv(f, na_values = ' ', header = 2).fillna(0)
#   print(f, data)


def de_genes():
    f = pd.read_csv('/Users/mmaes/Documents/Python_scripts/AAV_genes/Gosselin_tableS4.csv', na_values = "", delimiter = ',', quotechar = '|', header = 1, error_bad_lines = False).fillna(0)
    f['mean_exvivo'] = f.iloc[:, [14,15,16,17,18]].mean(axis =1)
    f['mean_6h'] = f.iloc[:, [4,5]].mean(axis=1)  
    f['mean_24h'] = f.iloc[:, [1,2,3]].mean(axis=1)
    f['mean_7d'] = f.iloc[:, [7,8,9,10,11]].mean(axis=1)
    f['6h_diff'] = f['mean_6h'] / f['mean_exvivo']
    f['24h_diff'] = f['mean_24h'] / f['mean_exvivo']
    f['7d_diff'] = f['mean_7d'] / f['mean_exvivo']
    f.sort_values(by=['7d_diff', '24h_diff'], axis = 0, ascending = False, inplace = True)
    print(f.loc[15:].head())
    writer = pd.ExcelWriter('de_genes.xlsx', engine='xlsxwriter')
    f.to_excel(writer, sheet_name='Sheet1')

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

if __name__ == "__main__":
  de_genes()

  ## dont really want to do the error bad lines thing. Need to find a different work around. 