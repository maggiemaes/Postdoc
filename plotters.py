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

def plot_volume(df, title, ymin, ylimit):
    df_od = df[df.mod_cond == 'od']
    df_os = df[df.mod_cond == 'os']
    array = ['os', 'od']
    df_f = df[df.mod_sex == 'female']
    df_f=df_f.loc[df_f['mod_cond'].isin(array)]
  
    df_m = df[df.mod_sex == 'male']
    df_m=df_m.loc[df_m['mod_cond'].isin(array)]


    sns.violinplot(x='mod_retinal_layer', y= 'Value', hue='mod_sex',data = df_od, order=['gcl', 'ipl', 'opl'], split=True, inner="stick", palette='deep')
    plt.title(title + ' OD')
    plt.ylim(ymin,ylimit)
    plt.show()
     
    sns.violinplot(x='mod_retinal_layer', y='Value', hue='mod_sex', data=df_os, order=['gcl', 'ipl', 'opl'], split=True, inner="stick", palette='deep')
    plt.title(title + ' OS')
    plt.ylim(ymin,ylimit)
    plt.show()

    sns.violinplot(x='mod_cond', y= 'Value', hue='mod_sex',data = df, split=True, order=['na', 'od', 'os'], inner="stick", palette='deep')
    plt.title(title + ' (per Condition)') 
    plt.ylim(ymin,ylimit)
    plt.show()

 ##
    sns.violinplot(x='mod_retinal_layer', y= 'Value', hue='mod_cond',data = df_m, split=True, order=['gcl', 'ipl', 'opl'], inner="stick")
    plt.title(title + ' Male') 
    plt.ylim(ymin,ylimit)
    plt.show() 

    sns.violinplot(x='mod_retinal_layer', y= 'Value', hue='mod_cond',data = df_f, split=True, order=['gcl', 'ipl', 'opl'], inner="stick")
    plt.title(title + ' Female') 
    plt.ylim(ymin,ylimit)
    plt.show() 

    sns.boxplot(x='mod_cond', y= 'Value', hue = 'mod_retinal_layer', data = df, order=['na', 'od', 'os'])
    plt.title(title)
    plt.ylim(0,ylimit)
    plt.show()

    sns.boxplot(x='mod_cond', y= 'Value', hue = 'mod_sex', data = df, order=['na', 'od', 'os'])
    plt.ylim(0,ylimit)
    plt.title(title)
    plt.show()



