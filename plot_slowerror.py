#!/usr/bin/env python3
#------------------------------------------------------------
# Programmer(s):  Daniel R. Reynolds @ SMU
#------------------------------------------------------------
# Copyright (c) 2024, Southern Methodist University.
# All rights reserved.
# For details, see the LICENSE file.
#------------------------------------------------------------

# imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set plot defaults: increase default font size, increase plot width, enable LaTeX rendering
plt.rc('font', size=15)
plt.rcParams['figure.figsize'] = [7.2, 4.8]
plt.rcParams['text.usetex'] = True

# flags to turn on/off certain plots
Generate_detailed_plots = False
Generate_stats_plots = True
Generate_PDF = True
Generate_PNG = False

# set a floor for dsm and dsm_est values
dsm_floor = 1.e-7

# utility functions
def mname(method):
    """
    Splits the method name based on underscores, removes the strings 'ARKODE' and 'GARK' ,
    and joins the results back together.
    """
    msplit = method.split('_')
    pruned = [s for s in msplit if s != 'ARKODE']
    pruned2 = [s for s in pruned if s != 'GARK']
    return " ".join(pruned2)

def get_row_fixedstep(line):
    """
    This routine processes a fixed step run line
    """
    txt = line.split()
    H = float(txt[1])
    method = txt[3]
    time = float(txt[5])
    dsm = float(txt[7])
    dsm_est = float(txt[9])
    if (dsm_est < dsm_floor or dsm < dsm_floor):
        ratio = np.nan
    else:
        ratio = dsm/dsm_est
    data = [{'H': H, 'method': method, 't': time, 'ratio': ratio}]
    return pd.DataFrame.from_records(data)

def load_file(fname):
    """
    Creates time-step level dataframes from a file.
    """
    df = pd.DataFrame({'H': [], 'method': [], 't': [], 'dsm': [], 'dsm_est': []})
    f = open(fname)
    for line in f:
        txt = line.split()
        if ('dsm_est' in txt):
            new_row = get_row_fixedstep(line)
            df = pd.concat([df, new_row])
    f.close()
    return df

def compile_stats(df):
    """
    Creates "statistics" dataframes from time-step level dataframes.
    """
    from scipy import stats
    Hs = []
    methods = []
    mins = []
    maxs = []
    gmeans = []
    for method in df['method'].sort_values().unique():
        for H in (df.groupby(['method']).get_group((method)))['H'].sort_values().unique():
            ratio = (df.groupby(['H','method']).get_group((H,method)))['ratio']
            Hs.append(H)
            methods.append(method)
            mins.append(np.min(ratio))
            maxs.append(np.max(ratio))
            gmeans.append(stats.mstats.gmean(ratio))
    stats = pd.DataFrame({'H': Hs, 'method': methods, 'min': mins, 'max': maxs, 'gmean': gmeans})
    return stats

def do_plots(fname, problem, picname):
    """
    Given a filename with results, and strings containing the problem name (for plot titles) and
    output file name (without suffix), this does the following:
    1. Loads the data file
    2. Conditionally constructs a detailed plot of the data, and saves to disk
    3. Conditionally constructs a plot of the statistics of the data, and saves to disk
    """
    data = load_file(fname)

    if (Generate_detailed_plots):
        t = data['t'].sort_values().unique()
        plt.figure()
        for method in data['method'].sort_values().unique():
            for H in (data.groupby(['method']).get_group((method)))['H'].sort_values().unique():
                ratio = (data.groupby(['H','method']).get_group((H,method)))['ratio']
                labeltxt = mname(method) + ' H {0:.1e}'.format(H)
                plt.semilogy(t[:len(ratio)], ratio, label=labeltxt)

        plt.xlabel(r'$t$')
        plt.ylabel(r'$\varepsilon^s_{ref}/\varepsilon^s_{approx}$')
        plt.title('Slow error estimation -- ' + problem)
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        #plt.tight_layout()
        plt.grid(linestyle='--', linewidth=0.5)
        if (Generate_PNG):
            plt.savefig(picname + '.png')
        if (Generate_PDF):
            plt.savefig(picname + '.pdf')

    if (Generate_stats_plots):
        stats = compile_stats(data)
        plt.figure()
        for method in stats['method'].sort_values().unique():
            Hs = (stats.groupby(['method']).get_group((method)))['H']
            gmeans = (stats.groupby(['method']).get_group((method)))['gmean']
            plt.loglog(Hs, gmeans, 'o', label=mname(method))

        plt.xlabel('step size')
        plt.ylabel(r'$\varepsilon^s_{ref}/\varepsilon^s_{approx}$ (geom. mean)')
        plt.title('Slow error estimation -- ' + problem)
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()
        plt.grid(linestyle='--', linewidth=0.5)
        if (Generate_PNG):
            plt.savefig(picname + '-stats.png')
        if (Generate_PDF):
            plt.savefig(picname + '-stats.pdf')

# KPR: low order vs high order methods
do_plots('slowerror_kpr_results_lo.txt', 'KPR', 'kpr-ratio-lo')
do_plots('slowerror_kpr_results_hi.txt', 'KPR', 'kpr-ratio-hi')

# Brusselator: low order vs high order methods
do_plots('slowerror_brusselator_results_lo.txt', 'Brusselator', 'bruss-ratio-lo')
do_plots('slowerror_brusselator_results_hi.txt', 'Brusselator', 'bruss-ratio-hi')


## display plots
#plt.show()
