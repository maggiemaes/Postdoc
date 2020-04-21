
import glob as glob
import pandas as pd
import numpy as np 
import os
import string

###### DATA IMPORT TOOLS #########

   ##Get simplified file name for specfic cell. Prefix is path name.
def get_cellname(filepath):
      cellname = os.path.basename(filepath)
      return cellname[:-4]

#import imaris surface file from folders 
#antiquated version
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

#
# Reading utilities for "stat" files 
#

def read_v9_1(fname):
    cellname = os.path.basename(fname)[:-len('.csv')]
    df = pd.read_csv(fname, na_values=' ', header=2, error_bad_lines=False).fillna(0)
    
    if 'Variable' not in df.columns:
        msg = '{} (v9_1) has no variable column'
        raise ValueError(msg.format(fname))
    
    df = df.drop(df.columns[df.columns.str.contains('Unnamed')], axis=1)
    df['Date'], df['sex'], df['condition'], df['retinal_layer'], df['surface_type'] = cellname.split('_')[0:5]
    return df

# this is a generic function for both 9.2 and 9.3 files after we discover the cell and variable names
def _read_v9_1_plus(fname, variable, cellname):
    df = pd.read_csv(fname, na_values=' ', header=2, error_bad_lines=False).fillna(0)
    df = df.drop(df.columns[df.columns.str.contains('Unnamed')], axis=1)

    # sometimes position values have multiple data columns, melt into one observation per row
    var_cols = df.columns[df.columns.str.startswith(variable)]
    if len(var_cols) >1:
        value_vars = var_cols
        id_vars = set(df.columns) - set(value_vars)
        df = df.melt(value_vars=value_vars, id_vars=id_vars, 
                     value_name=variable, var_name='Variable')
    elif len(var_cols) == 1:
        df['Variable'] = variable
    else:
        msg = '{} not in columns for V9_3 file {}, need to update the function read_v9_3 in order to handle this'
        raise ValueError(msg.format(variable, fname))

    # get additional column names/data correct
    df = df.rename(columns={variable: 'Value'})
    df['Date'], df['sex'], df['condition'], df['retinal_layer'], df['surface_type'] = cellname.split('_')[0:5]
    return df

def varname_v9_2(fname):
    parts = os.path.basename(fname).split('_')[5:]
    if '=' not in ' '.join(parts):
        return ' '.join(parts)[:-len('.csv')].strip()
    
    # otherwise, theres some magic here, find everything up to first = and only join that
    for i, part in enumerate(parts):
        if '=' in part:
            idx = i
            break
    return ' '.join(parts[:idx]).strip()

### is there a problem here with the space in join functions??
def read_v9_2(fname):
    cellname = ' _'.join(os.path.basename(fname).split('_')[0:5])
    variable = varname_v9_2(fname)
    return _read_v9_1_plus(fname, variable, cellname)

def varname_v9_3(fname):
    basename = os.path.basename(fname)
    if '=' in basename:
        variable = ' '.join(basename.split('=')[0].split('_')[:-1])
    else:
        variable = ' '.join(basename[:-len('.csv')].split('_'))
    return variable.strip()

def read_v9_3(fname):
    cellname = os.path.basename(os.path.dirname(fname))
    variable = varname_v9_3(fname)
    return _read_v9_1_plus(fname, variable, cellname)


def determine_version(fname):
    basename = os.path.basename(fname)
    dirname = os.path.basename(os.path.dirname(fname))
    # 9.1 always looks like 2018_xx_yy/Detailed_xx_yy.csv
    if 'Detailed' in fname:
        version = '9_1'
    # 9.2 looks like 2018_xx_yy/2018_xx_yy.csv
    elif basename.split('_')[0] == dirname.split('_')[0]:
        version = '9_2'
    else:
        version = '9_3'
    return version


def get_stat2_files(fnames):
    read_funcs = {
        '9_1': read_v9_1,
        '9_2': read_v9_2,
        '9_3': read_v9_3,
    }
    dfs = []
    len_count = 0
    for fname in fnames:
        version = determine_version(fname)
        df = read_funcs[version](fname)
        if set(['Value', 'Variable']) - set(df.columns):
            raise ValueError('Fname: {} Version: {} is missing value or variable columns: {}'.format(fname, version, df.columns))
        if df.Value.isnull().any():
            raise ValueError('Fname: {} Version: {} has NaN values in Value Column'.format(fname, version))
        if df.Variable.apply(lambda x: len(x) == 0).any():
            raise ValueError('Fname: {} Version: {} could not discern Variable value'.format(fname, version))
        len_count += len(df)
        dfs.append(df)
    ret = pd.concat(dfs, sort=False)
    assert len_count == len(ret)
    return ret

#combine data imports to compile all raw data
def get_raw_data(data1, data2):
    n = []
    cond = []
    timepoint = []

    df_all = pd.concat([data1, data2], sort=True)
    # condition column has spaces at the end of some strings. Clean here. 
    df_all['condition'] = df_all['condition'].str.strip() 
    # df_all = df_all.drop(columns=['Collection', 'Channel', 'Depth','Image', 'Level', 'Distance', 'FilamentID', 'Surpass Object'])
   
    for x in df_all.sex:
        non_num = x.strip()
        non_num = non_num.rstrip(string.digits)
        n.append(non_num)

    for y in df_all.condition: 
        clean = y.strip()
        cond.append(clean[-2:])
        timepoint.append(clean[0:-2])

    df_all['mod_cond'] = cond
    df_all['timepoint'] = timepoint
    df_all['mod_retinal_layer'] = df_all['retinal_layer'].str[:3]
    df_all['mod_sex'] = n
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


##### EXTRACTING METRICS #####







