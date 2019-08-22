
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

## import files from Imaris v9.3, v9.2.1 and older v9.1.1
def get_stat2_files(filepath, header):
    dfs = []
    d= []
    for filename in glob.glob(filepath):
        cellname = os.path.basename(filename)[0:-4]
       ##print(cellname.split('_')[0:6])
        if cellname.split('_')[0:6][-1] == 'Detailed': 
            print(cellname.split('_')[0:6], 'yes')
            df = pd.read_csv(filename, na_values = ' ', header = header, error_bad_lines = False).fillna(0)
            df = df.drop(df.columns[df.columns.str.contains('Unnamed')], axis=1)
            df['Date'], df['sex'], df['condition'], df['retinal_layer'], df['surface_type'] = cellname.split('_')[0:5]
            dfs.append(df)        
        elif cellname.split('_')[0] != filename.split('/')[6][0:8]:
           ### Third formatting change in imaris. File name now no longer contains original file name information
            print("format3" )
            new_name = filename.split('/')[6]
#             print(new_name)
            exclude = ['Ch=', 'Img=']    
            new_df = pd.read_csv(filename, na_values = ' ', header = header, error_bad_lines = False).fillna(0)
            new_df = new_df.drop(new_df.columns[new_df.columns.str.contains('Unnamed')], axis=1)
            new_df = new_df.rename(columns = {cellname[:-4]: 'Value'})
            new_df['Date'], new_df['sex'], new_df['condition'], new_df['retinal_layer'], new_df['surface_type'] = new_name.split('_')[0:5]
            new_df['Variable'] = cellname[:-4]
            new_df.append(new_df)
            # print(new_df.columns)
        else:
            ## New formatted files have Value column labeled as the Variable type, must rename and organize for import
            print(cellname.split('_')[0:6],'new format')
            exclude = ['Ch=', 'Img=']    
            xtra = ' '.join([word for word in cellname.split('_')[5:] if not word.startswith(tuple(exclude))]).strip()       
            df3 = pd.read_csv(filename, na_values = ' ', header = header, error_bad_lines = False).fillna(0)
            if 'Time.1' in df3.columns: 
                df3= df3.drop(columns= 'Time.1')
            ##Overall file has several issues, and data is not needed anyway         
            if cellname.split('_')[0:6][-1] == 'Overall' and cellname.split('_')[0:5][-1] == 'mitolyso': 
                df3 = df3.drop(columns= ['Overall', 'Variable', 'Value', 'Unit', 'Custom', 'Time', 'ID']) #drops columns in overall files
            df3 = df3.drop(df3.columns[df3.columns.str.contains('Unnamed')], axis=1)
            df3 = df3.rename(columns = {xtra: 'Value'})
            df3['Date'], df3['sex'], df3['condition'], df3['retinal_layer'], df3['surface_type'] = cellname.split('_')[0:5]
            df3['Variable'] = xtra
            d.append(df3)    
            
    ver1 = pd.concat(dfs, sort=True)
    ver2 = pd.concat(d, sort=True)
    return pd.concat([ver1, ver2], sort=True)

#combine data imports to compile all raw data
def get_raw_data(data1, data2):
    n = []
    df_all = pd.concat([data1, data2], sort=True)
    # df_all = df_all.drop(columns=['Collection', 'Channel', 'Depth','Image', 'Level', 'Distance', 'FilamentID', 'Surpass Object'])
   
    for x in df_all.condition:
        non_num = x.rstrip('012')
        n.append(non_num)
    df_all['new_cond'] = n
    df_all['mod_cond'] = df_all['new_cond'].str[0:-2]
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








