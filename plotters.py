import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns



def plot_dist(df_dict, conditions, title):
#plots histograms and cumulative plots for several condition combinations
    
    sns.distplot(df_dict['odgcl']['Value'], label='od_gcl', color='blue', kde=True, norm_hist=True)
    sns.distplot(df_dict['odipl']['Value'], label='od_ipl', color = 'red', kde=True, norm_hist=True)
    sns.distplot(df_dict['odopl']['Value'], label='od_opl', color = 'magenta', kde=True, norm_hist=True)
    plt.xlabel('Distance (um)')
    plt.legend()
    plt.xlim(-10,225)
    plt.ylim(0,0.08)
    plt.title(title + ' OD')
    plt.show()
    
    sns.distplot(df_dict['osgcl']['Value'], label='os_gcl', color='blue')
    sns.distplot(df_dict['osipl']['Value'], label='os_ipl', color = 'red')
    sns.distplot(df_dict['osopl']['Value'], label='os_opl', color = 'magenta')
    plt.xlabel('Distance (um)')
    plt.legend()
    plt.xlim(-10,225)
    plt.ylim(0, 0.08)
    plt.title(title + ' OS')
    plt.show()
    
    sns.distplot(df_dict['na']['Value'], label='naive', color='orange')
    sns.distplot(df_dict['os']['Value'], label='os', color = 'black') #kde=False
    sns.distplot(df_dict['od']['Value'], label='od', color = 'green')
    plt.xlabel('Distance (um)')
    plt.legend()
    plt.xlim(-10,225)
    plt.ylim(0, 0.08)
    plt.title(title + ' All Cond')
    plt.show()

    sns.distplot(df_dict['nagcl']['Value'], label='Naive GCL', color = 'orange')
    sns.distplot(df_dict['odgcl']['Value'], label='OD GCL', color = 'green')
    sns.distplot(df_dict['osgcl']['Value'], label='OS GCL', color = 'black')
    plt.xlabel('Distance (um)')
    plt.legend()
    plt.xlim(-10,225)
    plt.ylim(0, 0.08)
    plt.title(title + ' GCL')
    plt.show()

    # sns.distplot(df_dict['naipl']['Value'], label='Naive IPL', color = 'orange')
    sns.distplot(df_dict['osipl']['Value'], label='OS IPL', color = 'black')
    sns.distplot(df_dict['odipl']['Value'], label='OD IPL', color = 'green')
    plt.xlabel('Distance (um)')
    plt.legend()
    plt.xlim(-10,225)
    plt.ylim(0, 0.08)
    plt.title(title + ' IPL')
    plt.show()

    # sns.distplot(df_dict['naopl']['Value'], label='Naive OPL', color = 'orange')
    sns.distplot(df_dict['osopl']['Value'], label='OS OPL', color = 'black')
    sns.distplot(df_dict['odopl']['Value'], label='OD OPL', color = 'green')
    plt.xlabel('Distance (um)')
    plt.legend()
    plt.xlim(-10,225)
    plt.ylim(0, 0.08)
    plt.title(title + ' OPL')
    plt.show()

    sns.distplot(df_dict['na']['Value'], color='orange', hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='Naive', cumulative=True))
    sns.distplot(df_dict['os']['Value'], color='green', hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='OS', cumulative=True))
    sns.distplot(df_dict['od']['Value'], color='black', hist_kws=dict(color='white', cumulative=True), kde_kws=dict(label='OD',cumulative=True))
    plt.legend()
    plt.xlim(-10,100)
    plt.ylim(0, 1.1)
    plt.title(title + ' All Cond')
    plt.show()
    
    sns.distplot(df_dict['osgcl']['Value'], color='blue', hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='OS GCL', cumulative=True))
    sns.distplot(df_dict['osipl']['Value'], color='red', hist_kws=dict(color='white', cumulative=True), kde_kws=dict(label='OS IPL',cumulative=True))
    sns.distplot(df_dict['osopl']['Value'], color='magenta', hist_kws=dict(color='white', cumulative=True), kde_kws=dict(label='OS OPL',cumulative=True))
    plt.legend()
    plt.xlim(-10,100)
    plt.ylim(0,1.1)
    plt.title(title + ' OS')
    plt.show()

    sns.distplot(df_dict['odgcl']['Value'], color='blue', hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='OD GCL', cumulative=True))
    sns.distplot(df_dict['odipl']['Value'], color='red', hist_kws=dict(color='white', cumulative=True), kde_kws=dict(label='OD IPL',cumulative=True))
    sns.distplot(df_dict['odopl']['Value'], color='magenta', hist_kws=dict(color='white', cumulative=True), kde_kws=dict(label='OD OPL',cumulative=True))
    plt.legend()
    plt.xlim(-10,100)
    plt.ylim(0,1.1)
    plt.title(title + ' OD')
    plt.show()

    sns.distplot(df_dict['nagcl']['Value'], color = 'orange', hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='Naive GCL', cumulative=True))
    sns.distplot(df_dict['odgcl']['Value'], color = 'green', hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='OD GCL', cumulative=True))
    sns.distplot(df_dict['osgcl']['Value'], color = 'black', hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='OS GCL', cumulative=True))
    plt.xlabel('Distance (um)')
    plt.legend()
    plt.xlim(-10,100)
    plt.ylim(0, 1.1)
    plt.title(title + ' GCL')
    plt.show()

    # sns.distplot(df_dict['naipl']['Value'],  color = 'orange',hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='Naive IPL', cumulative=True))
    sns.distplot(df_dict['osipl']['Value'], color = 'black', hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='OS IPL', cumulative=True))
    sns.distplot(df_dict['odipl']['Value'], color = 'green',hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='OD IPL', cumulative=True))
    plt.xlabel('Distance (um)')
    plt.legend()
    plt.xlim(-10,100)
    plt.ylim(0, 1.1)
    plt.title(title + ' IPL')
    plt.show()

    # sns.distplot(df_dict['naopl']['Value'], color = 'orange',hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='Naive OPL', cumulative=True))
    sns.distplot(df_dict['osopl']['Value'], color = 'black', hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='OS OPL', cumulative=True))
    sns.distplot(df_dict['odopl']['Value'], color = 'green', hist_kws=dict(cumulative=True, color='white'), kde_kws=dict(label='OD OPL', cumulative=True))
    plt.xlabel('Distance (um)')
    plt.legend()
    plt.xlim(-10,100)
    plt.ylim(0, 1.1)
    plt.title(title + ' OPL')
    plt.show()

def plot_sholl(df_dict, group, conditions, title):	
    
    

    df_dict['na'].groupby(group).median()['Value'].plot(kind='line', color='orange', xlim=(0,125), ylim=(0,25), label='Naive', legend=True)
    df_dict['od'].groupby(group).median()['Value'].plot(kind='line', color='green', xlim=(0,125), ylim=(0,25), label='OD', legend=True)
    df_dict['os'].groupby(group).median()['Value'].plot(kind='line', color='black', xlim=(0,125), ylim=(0,25), label='OS', legend=True)
    df_dict['rd'].groupby(group).median()['Value'].plot(kind='line', color='yellow', xlim=(0,125), ylim=(0,25), label='RD', legend=True)
    df_dict['wt'].groupby(group).median()['Value'].plot(kind='line', color='pink', xlim=(0,125), ylim=(0,25), label='WT', legend=True)
    plt.legend()
    plt.title(title + ' per Condition')
    plt.show()

    df_dict['odgcl'].groupby(group).median()['Value'].plot(kind='line', color='blue', xlim=(0,125), ylim=(0,25), label='OD GCL', legend=True)
    df_dict['odipl'].groupby(group).median()['Value'].plot(kind='line', color='red', xlim=(0,125), ylim=(0,25), label='OD IPL', legend=True)
    df_dict['odopl'].groupby(group).median()['Value'].plot(kind='line', color='magenta', xlim=(0,125), ylim=(0,25), label='OD OPL', legend=True)
    plt.legend()
    plt.title(title + ' OD')
    plt.show()

    df_dict['osgcl'].groupby(group).median()['Value'].plot(kind='line', color='blue', xlim=(0,125), ylim=(0,25), label='OS GCL', legend=True)
    df_dict['osipl'].groupby(group).median()['Value'].plot(kind='line', color='red', xlim=(0,125), ylim=(0,25), label='OS IPL', legend=True)
    df_dict['osopl'].groupby(group).median()['Value'].plot(kind='line', color='magenta', xlim=(0,125), ylim=(0,25), label='OS OPL', legend=True)
    plt.legend()
    plt.title(title + ' OS')
    plt.show()

    df_dict['nagcl'].groupby(group).median()['Value'].plot(kind='line', color='orange', xlim=(0,125), ylim=(0,25), label='Naive GCL', legend=True)
    df_dict['odgcl'].groupby(group).median()['Value'].plot(kind='line', color='green', xlim=(0,125), ylim=(0,25), label='OD GCL', legend=True)
    df_dict['osgcl'].groupby(group).median()['Value'].plot(kind='line', color='black', xlim=(0,125), ylim=(0,25), label='OS GCL', legend=True)
    plt.legend()
    plt.title(title + ' GCL')
    plt.show()

    # df_dict['naipl'].groupby(group).median()['Value'].plot(kind='line', color='orange', xlim=(0,125), ylim=(0,25), label='Naive IPL', legend=True)
    df_dict['odipl'].groupby(group).median()['Value'].plot(kind='line', color='green', xlim=(0,125), ylim=(0,25), label='OD IPL', legend=True)
    df_dict['osipl'].groupby(group).median()['Value'].plot(kind='line', color='black', xlim=(0,125), ylim=(0,25), label='OS IPL', legend=True)
    plt.legend()
    plt.title(title +' IPL')
    plt.show()

    # df_dict['naopl'].groupby(group).median()['Value'].plot(kind='line', color='orange', xlim=(0,125), ylim=(0,25), label='Naive OPL', legend=True)
    df_dict['odopl'].groupby(group).median()['Value'].plot(kind='line', color='green', ylim=(0,25), label='OD OPL', legend=True)
    df_dict['osopl'].groupby(group).median()['Value'].plot(kind='line', color='black', ylim=(0,25), label='OS OPL', legend=True)
    plt.legend()
    plt.title(title +' OPL')
    plt.show()

def plot_volume(df, title, ylabel, ymin, ylimit):
    df_od = df[df.mod_cond == 'od']
    df_os = df[df.mod_cond == 'os']
    df_naive = df[df.mod_cond == 'naive']

    rd = df[df.mod_cond == 'rd']
    wt = df[df.mod_cond == 'wt']
    array = ['os', 'od']
    array2 = ['rd', 'wt']

    df_f = df[df.mod_sex == 'fem']
    dff=df_f.loc[df_f['mod_cond'].isin(array)]
    rdwt_f = df_f.loc[df_f['mod_cond'].isin(array2)]
  
    df_m = df[df.mod_sex == 'male']
    dfm=df_m.loc[df_m['mod_cond'].isin(array)]
    rdwt_m = df_m.loc[df_m['mod_cond'].isin(array2)]
    
    ipl = df[df.mod_retinal_layer == 'ipl']
    opl = df[df.mod_retinal_layer ==  'opl']
    layers = [ipl, opl]
    conditions = [df_od, df_os, df_naive]
    colors = sns.color_palette('Set2')#['turquoise', 'tomato','magenta', 'blue']
    hues = ['naive', 'd5', 'd14', 'd35']

    for x in range(len(layers)):
        sns.stripplot(x='timepoint', y='Value', hue='mod_cond', data = layers[x], order=hues, palette=colors, jitter=True, dodge=True)    
        ax = sns.boxplot(x='timepoint', y='Value',  hue='mod_cond', data= layers[x], order=hues, palette=colors)
        handles, labels = ax.get_legend_handles_labels()
        for patch in ax.artists:
            r, g, b, a = patch.get_facecolor()
            patch.set_facecolor((r, g, b, .1))
        layer = str(layers[x].mod_retinal_layer.unique())

        plt.title(title + layer +' per condition') 
        plt.legend(handles[0:4], labels[0:4])
        plt.ylim(ymin,ylimit)
        plt.ylabel(ylabel)
        plt.savefig(title + layer + '.pdf')
        plt.show()

    # for i in range(len(conditions)): 
    #     colors = ['c', 'mediumvioletred']
    #     sns.boxplot(x='timepoint', y='Value', hue='mod_cond', data = conditions[i], order=['wt', 'rd'], palette=colors)#['naive', 'd5', 'd14', 'd35']hue='mod_cond',
    #     sns.stripplot(x='timepoint', y='Value', hue='mod_cond', data = conditions[i], order=['wt', 'rd'], palette=colors, jitter=True, dodge=True)    
    #     ax = sns.boxplot(x='timepoint', y='Value',  hue='mod_cond', data=conditions[i], order=['wt', 'rd'], palette='Set2')
    #     handles, labels = ax.get_legend_handles_labels()
    #     for patch in ax.artists:
    #       r, g, b, a = patch.get_facecolor()
    #       patch.set_facecolor((r, g, b, .3))
    #     layer = str(conditions[i].mod_retinal_layer.unique())

    #     plt.title(title + layer + ' per condition') 
    #     plt.legend(handles[0:2], labels[0:2])
    #     plt.ylim(ymin,ylimit)
    #     plt.ylabel(ylabel)
    #     plt.xlabel('Experimental Condition')
    #     plt.show()
    #     # plt.savefig('title.eps', dpi=300)

    #   ###plot for posters   
    # for i in range(len(conditions)): 
    #     colors = sns.color_palette('Set2') #['turquoise', 'tomato','magenta', 'blue']
    #     hues = ['naive', 'd5', 'd14', 'd35']
    #     order = ['ipl','opl']

    #     sns.stripplot(x='mod_retinal_layer', y='Value', hue='timepoint', data = conditions[i], hue_order=hues,  palette=colors, jitter=True, dodge=True)    
    #     ax = sns.boxplot(x='mod_retinal_layer', y='Value',  hue='timepoint', data=conditions[i], hue_order=hues,  palette=colors)
    #     handles, labels = ax.get_legend_handles_labels()
    #     for patch in ax.artists:
    #       r, g, b, a = patch.get_facecolor()
    #       patch.set_facecolor((r, g, b, .2))
    #     layer = str(conditions[i].mod_retinal_layer.unique())

    #     plt.title(title + layer + ' per condition') 
    #     plt.legend(handles[0:4], labels[0:4])
    #     plt.ylim(ymin,ylimit)
    #     plt.ylabel(ylabel)
    #     plt.xlabel('Experimental Condition')
    #     plt.savefig(title + layer + '.pdf')
    #     plt.show()
    #     plt.close()

 # ##
    # sns.stripplot(x='mod_retinal_layer', y= 'Value', hue='condition',data = df, hue_order= ['naiveos', 'naiveod', 'd5od', 'd5os', 'd14od', 'd14os', 'd35od', 'd35os', 'wtod', 'wtos', 'rdod', 'rdos'],order=['ipl', 'opl'] ,palette='deep', jitter=True, dodge=True)
    # sns.boxplot(x='mod_retinal_layer', y= 'Value', hue='condition',data = df, hue_order= ['naiveos', 'naiveod', 'd5od', 'd5os', 'd14od', 'd14os', 'd35od', 'd35os', 'wtod', 'wtos', 'rdod', 'rdos'],order=['ipl', 'opl'], palette='deep')
    # ax = sns.boxplot(x='mod_retinal_layer', y= 'Value', hue = 'condition', data = df, hue_order=['naiveos', 'naiveod', 'd5od', 'd5os', 'd14od', 'd14os', 'd35od', 'd35os', 'wtod', 'wtos', 'rdod', 'rdos'], order=['ipl', 'opl'],palette='deep')
    # handles, labels = ax.get_legend_handles_labels()
    # for patch in ax.artists:
    #   r, g, b, a = patch.get_facecolor()
    #   patch.set_facecolor((r, g, b, .3))

    # plt.legend(handles[0:12], labels[0:12])
    # plt.title(title)
    # plt.ylim(0,ylimit)
    # plt.ylabel(ylabel)
    # plt.xlabel('Retinal Layer')
    # plt.show()   
    

    
    # sns.stripplot(x='mod_retinal_layer', y= 'Value', hue = 'mod_cond', data = df, hue_order=[ 'wt', 'rd'], order=['ipl', 'opl'], palette='deep', dodge=True, jitter=True)
    # sns.boxplot(x='mod_retinal_layer', y= 'Value', hue = 'mod_cond', data = df, hue_order=[ 'wt', 'rd'], order=['ipl', 'opl'], palette='deep')
    # ax = sns.boxplot(x='mod_retinal_layer', y= 'Value', hue = 'mod_cond', data = df, hue_order=[ 'wt', 'rd'], order=['ipl', 'opl'], palette='deep')
    # handles, labels = ax.get_legend_handles_labels()
    # for patch in ax.artists:
    #   r, g, b, a = patch.get_facecolor()
    #   patch.set_facecolor((r, g, b, .3))

    # plt.legend(handles[0:2], labels[0:2])
    # plt.title(title)
    # plt.ylim(0,ylimit)
    # plt.ylabel(ylabel)
    # plt.xlabel('Retinal Layer')
    # plt.show()

    # sns.stripplot(x='mod_retinal_layer', y= 'Value', hue='mod_cond',data = df, hue_order= ['wt', 'rd'],order=['opl'], palette='deep', jitter=True, dodge=True)
    # sns.boxplot(x='mod_retinal_layer', y= 'Value', hue='mod_cond',data = df, hue_order= ['wt', 'rd'],order=['opl'], palette='deep')
    # ax = sns.boxplot(x='mod_retinal_layer', y= 'Value', hue = 'mod_cond', data = df, hue_order=['wt', 'od'], order=['opl'], palette='deep')
    # handles, labels = ax.get_legend_handles_labels()
    # for patch in ax.artists:
    #   r, g, b, a = patch.get_facecolor()
    #   patch.set_facecolor((r, g, b, .3))

    # plt.legend(handles[0:2],labels[0:2])
    # plt.title(title)
    # plt.ylim(0,ylimit)
    # plt.ylabel(ylabel)
    # plt.xlabel('Retinal Layer')
    # plt.show()   
    






