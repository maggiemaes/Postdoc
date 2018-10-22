import numpy as np
import pandas as pd
import glob 
import os
import analysis_tools as tools
import seaborn as sns
import plotters as plot
import matplotlib.pyplot as plt



def mitos():
    data1 = tools.get_stat_files('/Users/mmaes/Documents/Python_scripts/raw_data/**/*.csv', 2)
    data2 = tools.get_loc_files('/Users/mmaes/Documents/Python_scripts/raw_data/*.csv')
    
    df= tools.get_raw_data(data1,data2)
    conditions = {'na': ['gcl', 'ipl', 'opl'], 'os': ['gcl', 'ipl', 'opl'], 'od': ['gcl', 'ipl', 'opl']}
    
    #Distance
    # dist = df[df.Variable == 'distance']
    # dist_mito = dist[dist.surface_type == 'mitoloc']
    # # dist_mito = dist_mito[['sex', 'condition', 'retinal_layer', 'Value', 'mod_sex', 'mod_cond', 'mod_retinal_layer']]
    # dist_mito_grps = tools.get_groups(dist_mito, conditions)
    
    # dist_cd68 = dist[dist.surface_type == 'cd68loc']
    # dist_cd68_grps = tools.get_groups(dist_cd68, conditions) # this equals a dict containing all curated dataframe for plotting
    # plot.plot_dist(dist_mito_grps, conditions, 'Mitochondria Distance from Nucleus')
    # plot.plot_dist(dist_cd68_grps, conditions, 'Cd68 Distance from Nucleus')

    # # #Mitochondria Volume
    # df_mitovol = df[(df.Variable == 'Volume') & (df.surface_type == 'mito')]
    # cell = df_mitovol.groupby(['sex', 'condition', 'retinal_layer','mod_sex', 'mod_cond', 'mod_retinal_layer']).mean()['Value']
    # cell = cell.to_frame().reset_index()
    # plot.plot_volume(cell, 'Avg Mitochondria Volume', -1, 5)

    
    # # %volume cd68 per volume microglia
    # df_pcnt = df[df.Variable == 'Volume']
    # df_pcnt = df_pcnt.groupby(['surface_type', 'sex','condition', 'retinal_layer', 'mod_sex', 'mod_cond', 'mod_retinal_layer']).sum()['Value']
    # df_pcnt = (df_pcnt.loc['cd68'] / df_pcnt.loc['mg'])*100      #total cd68 vol/ total mg volume per each cell
    # df_pcnt = df_pcnt.reset_index()
    # df_pcnt['surface_type'] = 'pcnt_cd68_volume'    
    # plot.plot_volume(df_pcnt, 'CD68 percentage of Volume', -10, 30)


   #sholl analysis
    # df_sh = df[(df.surface_type == 'scholl') & (df.Variable == 'Filament No. Sholl Intersections')]
    # df_sh = df_sh[['sex', 'condition', 'retinal_layer', 'Radius', 'Value', 'mod_sex', 'mod_cond', 'mod_retinal_layer']]
    # dict_sh = tools.get_groups(df_sh, conditions)
    # plot.plot_sholl(dict_sh, 'Radius', conditions, 'Sholl Intersections')

    # #Surf-Surf Contact Area Mito-lyso
    mitolyso = df[df.surface_type == 'mitolyso']
    mitolyso = mitolyso.groupby(['Variable', 'sex','condition', 'retinal_layer', 'mod_sex', 'mod_cond', 'mod_retinal_layer']).sum()['Value']
    
    mito_area = df[(df.surface_type == 'mito') & (df.Variable == 'Area')]
    mito_area = mito_area.groupby(['Variable', 'sex','condition', 'retinal_layer', 'mod_sex', 'mod_cond', 'mod_retinal_layer']).sum()['Value']
    
    pcnt_mito = (mitolyso.loc['Contact surface area'] / mito_area.loc['Area'])*100
    pcnt_mito = pcnt_mito.reset_index()
    pcnt_mito['surface_type'] = ' pcnt mito contact Cd68'
    plot.plot_volume(pcnt_mito, 'Mito Contacts', -50, 200)

    # sns.boxplot(x='mod_cond', y = 'Value', hue='mod_sex', data=pcnt_mito, order=['na', 'od', 'os'])
    # plt.ylim(0,65)
    # plt.title('Percent of Mito Surfaces in contact with CD68 Surfaces')
    # plt.show()
    # sns.violinplot(x='mod_retinal_layer', y='Value', hue='mod_sex', data=pcnt_mito, order=['gcl', 'ipl', 'opl'], inner="stick", split=True)
    # plt.show()
    # sns.swarmplot(x='mod_cond', y='Value', hue='mod_retinal_layer', data=pcnt_mito, order=['na', 'od', 'os'])
    # plt.show() 
    
def cumulative_plot(): 
    data1 = tools.get_stat_files('/Users/mmaes/Documents/Python_scripts/raw_data/**/*.csv', 2)
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
 
    dataset= df.groupby(['mod_sex', 'mod_cond', 'mod_retinal_layer'])['retinal_layer'].nunique()
    dataset=dataset.to_frame()
    # dataset.to_csv('dataset.csv')

if __name__ == "__main__":
    mitos()