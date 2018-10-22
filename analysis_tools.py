
import glob as glob
import pandas as pd
import numpy as np 
import os


   ##Get simplified file name for specfic cell. Prefix is path name.
def get_cellname(filepath):
      cellname = os.path.basename(filepath)
      return cellname[:-4]

#import imaris surface file from folders
def get_stat_files(filepath, header):
    dfs = []
    for filename in glob.glob(filepath):
        cellname = os.path.basename(filename)[0:-4]
        print(cellname.split('_')[0:5])
        print(filename)
        df = pd.read_csv(filename, na_values = ' ', header = header, error_bad_lines = False).fillna(0)
        df = df.drop(df.columns[df.columns.str.contains('Unnamed')], axis=1)
        df['Date'], df['sex'], df['condition'], df['retinal_layer'], df['surface_type'] = cellname.split('_')[0:5]
        dfs.append(df)
    return pd.concat(dfs, sort=True)

#import localization data files
def get_loc_files(filepath):
    data_loc = []
    for filename in glob.glob(filepath):
        cellname = os.path.basename(filename)
        df2 = pd.read_csv(filename, na_values = ' ', header=0).fillna(0)
        df2 = pd.melt(df2).rename(columns = {'variable' : 'Variable', 'value' : 'Value'})
        df2['Unit'], df2['Category'], df2['Collection'], df2['Time'], df2['ID'] = ['um', 'dist_nucleus', '0', '0', '']
        df2['Date'], df2['sex'], df2['condition'], df2['retinal_layer'] = cellname.split('_')[0:4]
        df2['surface_type'] = cellname.split('_')[-1][:-4]
        data_loc.append(df2)

    data2 = pd.concat(data_loc, sort=True)
    data2 = data2[data2.Value > 0]
    ids = []
    for i,v in data2.Variable.items(): 
      id = v.split(' ')[1]
      ids.append(id)
    data2['ID'] = ids
    data2['Variable'] = 'distance'
    return data2    

#combine data imports to compile all raw data
def get_raw_data(data1, data2):
    df_all = pd.concat([data1, data2], sort=True)
    df_all = df_all.drop(columns=['Collection', 'Channel', 'Depth','Image', 'Level', 'Distance', 'FilamentID', 'Surpass Object'])
    df_all['mod_cond'] = df_all['condition'].str[:2]
    df_all['mod_retinal_layer'] = df_all['retinal_layer'].str[:3]
    df_all['mod_sex'] = df_all['sex'].str[:-1]
    return df_all


def get_groups(df, groupings, key_col='mod_cond', val_col='mod_retinal_layer'):
    ret = {}
    for key in groupings.keys():
        ret[key] = df[df[key_col] == key]
    for key, values in groupings.items():
        for value in values:
            kdf = ret[key]
            ret[key+value] = kdf[kdf[val_col] == value]
    return ret








