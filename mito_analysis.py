import numpy as np
import pandas as pd
import glob 
import os
import analysis_tools as tools
import seaborn as sns
import plotters as plot
import matplotlib.pyplot as plt


def raw_data():
    fnames = glob.glob('/Users/mmaes/Documents/Python_scripts/raw_data/**/*.csv')
    fnames = [f for f in fnames if not f.endswith('Overall.csv')]
    data1 = tools.get_stat2_files(fnames)
    data2 = tools.get_loc_files('/Users/mmaes/Documents/Python_scripts/raw_data/*.csv')
    df= tools.get_raw_data(data1, data2)  
    df.to_csv('/Users/mmaes/Documents/Python_scripts/Database/compiled_raw_data.csv')

def mitos():
    df = pd.read_csv('/Users/mmaes/Documents/Python_scripts/Database/compiled_raw_data.csv', low_memory=False).fillna(0)
    # old verison: conditions = {'naive': ['gcl', 'ipl', 'opl'], 'os': ['gcl', 'ipl', 'opl'], 'od': ['gcl', 'ipl', 'opl'], 'rd': ['gcl', 'ipl', 'opl'], 'wt': ['gcl', 'ipl', 'opl']}
    conditions = {'naive': ['ipl', 'opl'], 'os': ['ipl', 'opl'], 'od': ['ipl', 'opl'],'d14os': ['ipl', 'opl'], 'd14od': ['ipl', 'opl'], 'd35os': ['ipl', 'opl'], 'd35od': ['ipl', 'opl'], 'rd': ['gcl', 'ipl', 'opl'], 'wt': ['gcl', 'ipl', 'opl']}

    #Distance
    # dist = df[df.Variable == 'distance']
    # dist_mito = dist[dist.surface_type == 'mitoloc']
    # dist_mito = dist_mito[['sex', 'condition', 'retinal_layer', 'Value', 'mod_sex', 'mod_cond', 'mod_retinal_layer']]
    # dist_mito_grps = tools.get_groups(dist_mito, conditions)
    # # mdist= df[(df.Variable == 'distance') & (df.surface_type == 'mitoloc')]
    # # mdist1 = mdist.groupby(['sex', 'condition', 'retinal_layer','mod_sex', 'mod_cond', 'mod_retinal_layer']).median()['Value']
    # # mdist1 = mdist1.reset_index()
    # # plot.plot_volume(mdist1, 'Mitochondria Distance from Nucleus', 'Distance (um)', 0, 60)


    # dist_cd68 = dist[dist.surface_type == 'cd68loc']
    # dist_cd68_grps = tools.get_groups(dist_cd68, conditions) # this equals a dict containing all curated dataframe for plotting
    # plot.plot_dist(dist_cd68_grps, conditions, 'Cd68 Distance from Nucleus')

    # # # #Mitochondria Volume
    # df_mitovol = df[(df.Variable == 'Volume') & (df.surface_type == 'mito')]
    # df_mitovol= df_mitovol[(df_mitovol.Value >= 0.01)]
    # # df_mitovol = df_mitovol[(df_mitovol['mod_cond'] != 'rd')& (df_mitovol['mod_cond'] != 'wt')] 
    # cell = df_mitovol.groupby(['sex', 'condition', 'retinal_layer','mod_sex', 'mod_cond', 'mod_retinal_layer']).mean()['Value']
    # cell = cell.to_frame().reset_index()
    # # print(len(df_mitovol['Value']))
    # cell.to_csv('/Users/mmaes/Documents/Python_scripts/Output/mitovol.csv')
    # plot.plot_volume(cell, 'Avg organelle volume per cell', 'Volume (um^3)', 0, 6)

    ### ##Mitochondria number
    # df_mitovol = df[(df.Variable == 'Volume') & (df.surface_type == 'mito')]
    # df_mitovol= df_mitovol[(df_mitovol.Value >= 0.01)]
    # df_mitonum = df_mitovol.groupby(['sex', 'condition', 'retinal_layer','mod_sex', 'mod_cond', 'mod_retinal_layer']).count()
    # df_mitonum= df_mitonum.reset_index()
    # plot.plot_volume(df_mitonum, 'Mitochondria Number', 'Number per cell', 0, 125)

    
    # # # %volume cd68 per volume microglia
    df_pcnt = df[df.Variable == 'Volume']  
    # # # df_pcnt = df_pcnt[(df_pcnt['mod_cond'] != 'rd')& (df_pcnt['mod_cond'] != 'wt')] 
    df_pcnt = df_pcnt.groupby(['surface_type', 'sex','condition', 'retinal_layer', 'mod_sex', 'mod_cond','new_cond', 'mod_retinal_layer']).sum()['Value']
    df_pcnt_cd = (df_pcnt.loc['cd68'] / df_pcnt.loc['mg'])*100      #total cd68 vol/ total mg volume per each cell
    df_pcnt_cd = df_pcnt_cd.reset_index()
    df_pcnt_cd['surface_type'] = 'pcnt_cd68_volume'    
    df_pcnt_cd.to_csv('/Users/mmaes/Documents/Python_scripts/Output/cd68_pcnt.csv')
    plot.plot_volume(df_pcnt_cd, 'CD68 percentage of Volume', 'Percent (%)', 0, 30)
    
    ### volume mito per vol mg
    # df_pcnt_mito = (df_pcnt.loc['mito'] / df_pcnt.loc['mg'])*100      #total mito vol/ total mg volume per each cell
    # df_pcnt_mito = df_pcnt_mito.reset_index()
    # df_pcnt_mito['surface_type'] = 'pcnt_mito_volume'    
    # plot.plot_volume(df_pcnt_mito, 'Mito percentage of Volume', 'Percent (%)', 0, 25)
    # total = df_pcnt.loc['mito']
    # total = total.reset_index()
    # plot.plot_volume(total, 'Mito percentage of Volume', 'Percent (%)', 0, 25)

   #sholl analysis
    # df_sh = df[(df.surface_type == 'scholl') & (df.Variable == 'Filament No. Sholl Intersections')]
    # df_sh = df_sh[['sex', 'condition', 'retinal_layer', 'Radius', 'Value', 'mod_sex', 'mod_cond', 'mod_retinal_layer']]
    # dict_sh = tools.get_groups(df_sh, conditions)
    # plot.plot_sholl(dict_sh, 'Radius', conditions, 'Sholl Intersections')

    # # #Surf-Surf Contact Area Mito-lyso
    # mitolyso = df[df.surface_type == 'mitolyso']
    # mitolyso = mitolyso.groupby(['Variable', 'sex','condition', 'retinal_layer', 'mod_sex', 'mod_cond', 'mod_retinal_layer']).sum()['Value']
    # mito_area = df[(df.surface_type == 'mito') & (df.Variable == 'Area')]
    # mito_area = mito_area.groupby(['Variable', 'sex','condition', 'retinal_layer', 'mod_sex', 'mod_cond', 'mod_retinal_layer']).sum()['Value']
    

    # pcnt_mito = ((mitolyso.loc['Contact surface area'] / mito_area.loc['Area'])*100)
    # pcnt_mito = pcnt_mito.reset_index()
    # pcnt_mito= pcnt_mito[(pcnt_mito.Value <= 100)]  #remove weird outlier
    # # pcnt_mito = pcnt_mito[(pcnt_mito['mod_cond'] != 'rd')& (pcnt_mito['mod_cond'] != 'wt')& (pcnt_mito['mod_retinal_layer'] != 'gcl')] 

    # pcnt_mito['surface_type'] = ' pcnt mito contact Cd68'
    # plot.plot_volume(pcnt_mito, '% Mito SA in contact with CD68', 'Percent (%)', 0, 75)


    
def cumulative_plot(): 
    data1 = tools.get_stat2_files('/Users/mmaes/Documents/Python_scripts/raw_data/**/*.csv', 2)
    data2 = tools.get_loc_files('/Users/mmaes/Documents/Python_scripts/raw_data/*.csv')
    
    df= tools.get_raw_data(data1,data2)
    conditions = {'os': ['gcl', 'ipl', 'opl'], 'od': ['gcl', 'ipl', 'opl']}
    dist = df[df.Variable == 'distance']
    dist_mito = dist[dist.surface_type == 'mitoloc']
    dist_mito_grps = tools.get_groups(dist_mito, conditions)
    
    dist_cd68 = dist[dist.surface_type == 'cd68loc']
    # dist_cd68_grps = tools.get_groups(dist_cd68, conditions) 

    # sns.distplot(dist_mito_grps['os']['Value'], color='green', hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='os', cumulative=True))
    # sns.distplot(dist_mito_grps['od']['Value'], color='black', hist_kws=dict(color='white', cumulative=True), kde_kws=dict(label='od',cumulative=True))
    # plt.legend()
    # plt.show()
    
    # sns.distplot(dist_mito_grps['osgcl']['Value'], color='blue', hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='osgcl', cumulative=True))
    # sns.distplot(dist_mito_grps['osipl']['Value'], color='red', hist_kws=dict(color='white', cumulative=True), kde_kws=dict(label='osipl',cumulative=True))
    # sns.distplot(dist_mito_grps['osopl']['Value'], color='magenta', hist_kws=dict(color='white', cumulative=True), kde_kws=dict(label='osopl',cumulative=True))
    # plt.legend()
    # plt.show()

    # sns.distplot(dist_mito_grps['odgcl']['Value'], color='blue', hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='odgcl', cumulative=True))
    # sns.distplot(dist_mito_grps['odipl']['Value'], color='red', hist_kws=dict(color='white', cumulative=True), kde_kws=dict(label='odipl',cumulative=True))
    # sns.distplot(dist_mito_grps['odopl']['Value'], color='magenta', hist_kws=dict(color='white', cumulative=True), kde_kws=dict(label='odopl',cumulative=True))
    # plt.legend()
    # plt.show()
 
    dataset= df.groupby(['mod_sex', 'mod_cond', 'mod_retinal_layer'])['mod_retinal_layer'].nunique()
    dataset=dataset.to_frame()
    print(dataset)
    # dataset.to_csv('dataset.csv')

if __name__ == "__main__":
    raw_data()




