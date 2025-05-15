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

accsymbol = {'Additive': 'o',
             'Average': 's',
             'Double-Step': '^',
             'Maximum': "P",}
acccolor = {'Additive': 'blue',
            'Average': 'orange',
            'Double-Step': 'green',
            'Maximum': 'red',}
RKlines ={'DIRK' :'--',
          'ERK' : '-'}

# utility functions
def get_row_adaptive(line):
    """
    This routine processes an adaptive run line
    """
    txt = line.split()
    rtol = float(txt[1])
    rk_type = int(txt[3])
    if (rk_type == 0):
        RK = 'DIRK'
    else:
        RK = 'ERK'
    order = int(txt[5])
    acc = int(txt[7])
    if (acc == 1):
        accumulator = 'Maximum'
    elif (acc == 2):
        accumulator = 'Additive'
    elif (acc == 3):
        accumulator = 'Average'
    else:
        accumulator = 'Double-Step'
    time = float(txt[9])
    dsm = float(txt[11])
    dsm_est = float(txt[13])
    nsteps = int(txt[15])
    data = [{'rtol': rtol, 'RK': RK, 'order': order, 'accumulator': accumulator,  't': time, 'dsm': dsm, 'dsm_est': dsm_est, 'nsteps': nsteps}]
    return pd.DataFrame.from_records(data)

def get_row_fixedstep(line):
    """
    This routine processes a fixed step run line
    """
    txt = line.split()
    h = float(txt[1])
    rk_type = int(txt[3])
    if (rk_type == 0):
        RK = 'DIRK'
    else:
        RK = 'ERK'
    order = int(txt[5])
    acc = int(txt[7])
    if (acc == 1):
        accumulator = 'Maximum'
    elif (acc == 2):
        accumulator = 'Additive'
    elif (acc == 3):
        accumulator = 'Average'
    else:
        accumulator = 'Double-Step'
    time = float(txt[9])
    dsm = float(txt[11])
    dsm_est = float(txt[13])
    nsteps = int(txt[15])
    data = [{'h': h, 'RK': RK, 'order': order, 'accumulator': accumulator,  't': time, 'dsm': dsm, 'dsm_est': dsm_est, 'nsteps': nsteps}]
    return pd.DataFrame.from_records(data)

def load_file(fname):
    """
    Creates time-step level dataframes from a file.
    """
    adaptive_df = pd.DataFrame({'rtol': [], 'RK': [], 'order': [], 'accumulator': [], 't': [], 'dsm': [], 'dsm_est': [], 'nsteps': []})
    fixedstep_df = pd.DataFrame({'h': [], 'RK': [], 'order': [], 'accumulator': [], 't': [], 'dsm': [], 'dsm_est': [], 'nsteps': []})
    f = open(fname)
    for line in f:
        txt = line.split()
        if ('rtol' in txt):
            new_row = get_row_adaptive(line)
            adaptive_df = pd.concat([adaptive_df, new_row])
        elif ('h' in txt):
            new_row = get_row_fixedstep(line)
            fixedstep_df = pd.concat([fixedstep_df, new_row])
    f.close()
    return adaptive_df, fixedstep_df

def compile_stats(adaptive_df, fixedstep_df):
    """
    Creates "statistics" dataframes from time-step level dataframes.
    """
    from scipy import stats
    rtols = []
    RKs = []
    orders = []
    accumulators = []
    mins = []
    maxs = []
    gmeans = []
    steps = []
    for acc in adaptive_df['accumulator'].sort_values().unique():
        for RK in adaptive_df['RK'].sort_values().unique():
            for rtol in adaptive_df['rtol'].sort_values().unique():
                for order in (adaptive_df.groupby(['RK']).get_group((RK)))['order'].sort_values().unique():
                    dsm = (adaptive_df.groupby(['rtol','RK','order','accumulator']).get_group((rtol,RK,order,acc)))['dsm']
                    dsm_est = (adaptive_df.groupby(['rtol','RK','order','accumulator']).get_group((rtol,RK,order,acc)))['dsm_est']
                    nsteps = (adaptive_df.groupby(['rtol','RK','order','accumulator']).get_group((rtol,RK,order,acc)))['nsteps']
                    ratio = dsm/dsm_est
                    rtols.append(rtol)
                    RKs.append(RK)
                    orders.append(order)
                    accumulators.append(acc)
                    mins.append(np.min(ratio))
                    maxs.append(np.max(ratio))
                    gmeans.append(stats.mstats.gmean(ratio))
                    steps.append(np.sum(nsteps))
    adaptive_stats = pd.DataFrame({'rtol': rtols, 'RK': RKs, 'order': orders, 'accumulator': accumulators,
                                   'min': mins, 'max': maxs, 'gmean': gmeans, 'nsteps': steps})

    hs = []
    RKs = []
    orders = []
    accumulators = []
    mins = []
    maxs = []
    gmeans = []
    steps = []
    for acc in fixedstep_df['accumulator'].sort_values().unique():
        for RK in fixedstep_df['RK'].sort_values().unique():
            for h in (fixedstep_df.groupby(['RK']).get_group((RK)))['h'].sort_values().unique():
                for order in (fixedstep_df.groupby(['RK']).get_group((RK)))['order'].sort_values().unique():
                    dsm = (fixedstep_df.groupby(['h','RK','order','accumulator']).get_group((h,RK,order,acc)))['dsm']
                    dsm_est = (fixedstep_df.groupby(['h','RK','order','accumulator']).get_group((h,RK,order,acc)))['dsm_est']
                    nsteps = (fixedstep_df.groupby(['h','RK','order','accumulator']).get_group((h,RK,order,acc)))['nsteps']
                    ratio = dsm/dsm_est
                    hs.append(h)
                    RKs.append(RK)
                    orders.append(order)
                    accumulators.append(acc)
                    mins.append(np.min(ratio))
                    maxs.append(np.max(ratio))
                    gmeans.append(stats.mstats.gmean(ratio))
                    steps.append(np.sum(nsteps))
    fixedstep_stats = pd.DataFrame({'h': hs, 'RK': RKs, 'order': orders, 'accumulator': accumulators,
                                    'min': mins, 'max': maxs, 'gmean': gmeans, 'nsteps': steps})

    return adaptive_stats, fixedstep_stats


# load KPR data
kpr_adaptive, kpr_fixedstep = load_file('accumerror_kpr_results.txt')
kpr_adaptive_stats, kpr_fixedstep_stats = compile_stats(kpr_adaptive, kpr_fixedstep)

# load Brusselator data
bruss_adaptive, bruss_fixedstep = load_file('accumerror_brusselator_results.txt')
bruss_adaptive_stats, bruss_fixedstep_stats = compile_stats(bruss_adaptive, bruss_fixedstep)

# KPR plots
if (Generate_detailed_plots):
    t = kpr_adaptive['t'].sort_values().unique()
    for acc in kpr_adaptive['accumulator'].sort_values().unique():
        plt.figure()
        for RK in kpr_adaptive['RK'].sort_values().unique():
            for order in (kpr_adaptive.groupby(['RK']).get_group((RK)))['order'].sort_values().unique():
                for rtol in kpr_adaptive['rtol'].sort_values().unique():
                    dsm = (kpr_adaptive.groupby(['rtol','RK','order','accumulator']).get_group((rtol,RK,order,acc)))['dsm']
                    dsm_est = (kpr_adaptive.groupby(['rtol','RK','order','accumulator']).get_group((rtol,RK,order,acc)))['dsm_est']
                    nsteps = (kpr_adaptive.groupby(['rtol','RK','order','accumulator']).get_group((rtol,RK,order,acc)))['nsteps']
                    ratio = dsm/dsm_est
                    labeltxt = RK + '-{0:d}'.format(int(order)) + ' rtol {0:.1e}'.format(rtol)
                    plt.semilogy(t[:len(ratio)], ratio, label=labeltxt)

        plt.xlabel(r'$t$')
        plt.ylabel(r'$\varepsilon^f_{ref}/\varepsilon^f_{approx}$')
        plt.title(acc + ' Acc. (Adaptive)')
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()
        plt.grid(linestyle='--', linewidth=0.5)
        if (Generate_PNG):
            plt.savefig('kpr-ratio-adaptive-' + acc + '.png')
        if (Generate_PDF):
            plt.savefig('kpr-ratio-adaptive-' + acc + '.pdf')

    t = kpr_fixedstep['t'].sort_values().unique()
    for acc in kpr_fixedstep['accumulator'].sort_values().unique():
        plt.figure()
        for RK in kpr_fixedstep['RK'].sort_values().unique():
            for h in (kpr_fixedstep.groupby(['RK']).get_group((RK)))['h'].sort_values().unique():
                for order in (kpr_fixedstep.groupby(['RK']).get_group((RK)))['order'].sort_values().unique():
                    dsm = (kpr_fixedstep.groupby(['h','RK','order','accumulator']).get_group((h,RK,order,acc)))['dsm']
                    dsm_est = (kpr_fixedstep.groupby(['h','RK','order','accumulator']).get_group((h,RK,order,acc)))['dsm_est']
                    nsteps = (kpr_fixedstep.groupby(['h','RK','order','accumulator']).get_group((h,RK,order,acc)))['nsteps']
                    ratio = dsm/dsm_est
                    labeltxt = RK + '-{0:d}'.format(int(order)) + ' h {0:.1e}'.format(h)
                    plt.semilogy(t[:len(ratio)], ratio, label=labeltxt)

        plt.xlabel(r'$t$')
        plt.ylabel(r'$\varepsilon^f_{ref}/\varepsilon^f_{approx}$')
        plt.title(acc + ' Acc. (Fixed Step)')
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()
        plt.grid(linestyle='--', linewidth=0.5)
        if (Generate_PNG):
            plt.savefig('kpr-ratio-fixedstep-' + acc + '.png')
        if (Generate_PDF):
            plt.savefig('kpr-ratio-fixedstep-' + acc + '.pdf')
# this the one we use!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if (Generate_stats_plots):
    plt.figure()
    for acc in kpr_adaptive_stats['accumulator'].sort_values().unique():
        RK = 'ERK'
        #for RK in kpr_adaptive_stats['RK'].sort_values().unique():
        rtol   = (kpr_adaptive_stats.groupby(['order','RK','accumulator']).get_group((3,RK,acc)))['rtol']
        gmeans = (kpr_adaptive_stats.groupby(['order','RK','accumulator']).get_group((3,RK,acc)))['gmean']
        labeltxt = '{0:1}'.format(acc)
        plt.loglog(rtol, gmeans, label=labeltxt, marker=accsymbol[acc], color=acccolor[acc], linestyle=RKlines[RK])
    plt.xlabel('rtol')
    plt.ylabel(r'$\varepsilon^f_{ref}/\varepsilon^f_{approx}$ (geom. mean)')
    plt.title("Adaptive-step KPR")
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()
    plt.grid(linestyle='--', linewidth=0.5)

    if (Generate_PNG):
        plt.savefig('3rd order kpr-ratio-adaptive-stats.png')
    if (Generate_PDF):
        plt.savefig('3rd order kpr-ratio-adaptive-stats.pdf')

    plt.figure()
    for acc in kpr_fixedstep_stats['accumulator'].sort_values().unique():
        RK = 'ERK'
        #for RK in kpr_fixedstep_stats['RK'].sort_values().unique():
        h      = (kpr_fixedstep_stats.groupby(['order','RK','accumulator']).get_group((3,RK,acc)))['h']
        #orders = (kpr_fixedstep_stats.groupby(['h','RK','accumulator']).get_group((h,RK,acc)))['order']
        gmeans = (kpr_fixedstep_stats.groupby(['order','RK','accumulator']).get_group((3,RK,acc)))['gmean']
        labeltxt = '{0:1}'.format(acc)
        plt.loglog(h, gmeans, label=labeltxt, marker=accsymbol[acc], color=acccolor[acc], linestyle=RKlines[RK])

    plt.xlabel('h')
    plt.ylabel(r'$\varepsilon^f_{ref}/\varepsilon^f_{approx}$ (geom. mean)')
    plt.title("Fixed-step KPR")
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()
    plt.grid(linestyle='--', linewidth=0.5)

    if (Generate_PNG):
        plt.savefig('3rd order kpr-ratio-fixedstep-stats.png')
    if (Generate_PDF):
        plt.savefig('3rd order kpr-ratio-fixedstep-stats.pdf')



# Brusselator plots
if (Generate_detailed_plots):
    #plt.figure()
    t = bruss_adaptive['t'].sort_values().unique()
    for acc in bruss_adaptive['accumulator'].sort_values().unique():
        plt.figure()
        for RK in bruss_adaptive['RK'].sort_values().unique():
            for rtol in bruss_adaptive['rtol'].sort_values().unique():
                for order in (bruss_adaptive.groupby(['RK']).get_group((RK)))['order'].sort_values().unique():
                    dsm = (bruss_adaptive.groupby(['rtol','RK','order','accumulator']).get_group((rtol,RK,order,acc)))['dsm']
                    dsm_est = (bruss_adaptive.groupby(['rtol','RK','order','accumulator']).get_group((rtol,RK,order,acc)))['dsm_est']
                    nsteps = (bruss_adaptive.groupby(['rtol','RK','order','accumulator']).get_group((rtol,RK,order,acc)))['nsteps']
                    ratio = dsm/dsm_est
                    labeltxt = RK + '-{0:d}'.format(int(order)) + ' rtol {0:.1e}'.format(rtol)
                    plt.semilogy(t[:len(ratio)], ratio, label=labeltxt)

        plt.xlabel(r'$t$')
        plt.ylabel(r'$\varepsilon^f_{ref}/\varepsilon^f_{approx}$')
        plt.title(acc + ' Acc. (Adaptive)')
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()
        plt.grid(linestyle='--', linewidth=0.5)
        if (Generate_PNG):
            plt.savefig('bruss-ratio-adaptive-' + acc + '.png')
        if (Generate_PDF):
            plt.savefig('bruss-ratio-adaptive-' + acc + '.pdf')

    t = bruss_fixedstep['t'].sort_values().unique()
    for acc in bruss_fixedstep['accumulator'].sort_values().unique():
        plt.figure()
        for RK in bruss_fixedstep['RK'].sort_values().unique():
            for h in (bruss_fixedstep.groupby(['RK']).get_group((RK)))['h'].sort_values().unique():
                for order in (bruss_fixedstep.groupby(['RK']).get_group((RK)))['order'].sort_values().unique():
                    dsm = (bruss_fixedstep.groupby(['h','RK','order','accumulator']).get_group((h,RK,order,acc)))['dsm']
                    dsm_est = (bruss_fixedstep.groupby(['h','RK','order','accumulator']).get_group((h,RK,order,acc)))['dsm_est']
                    nsteps = (bruss_fixedstep.groupby(['h','RK','order','accumulator']).get_group((h,RK,order,acc)))['nsteps']
                    ratio = dsm/dsm_est
                    labeltxt = RK + '-{0:d}'.format(int(order)) + ' h {0:.1e}'.format(h)
                    plt.semilogy(t[:len(ratio)], ratio, label=labeltxt)

        plt.xlabel(r'$t$')
        plt.ylabel(r'$\varepsilon^f_{ref}/\varepsilon^f_{approx}$')
        plt.title(acc + ' Acc. (Fixed Step)')
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()
        plt.grid(linestyle='--', linewidth=0.5)
        if (Generate_PNG):
            plt.savefig('bruss-ratio-fixedstep-' + acc + '.png')
        if (Generate_PDF):
            plt.savefig('bruss-ratio-fixedstep-' + acc + '.pdf')
# we use this as well

if (Generate_stats_plots):
    plt.figure()
    for acc in bruss_adaptive_stats['accumulator'].sort_values().unique():
        RK = 'ERK'
        #for RK in bruss_adaptive_stats['RK'].sort_values().unique():
        rtol   = (bruss_adaptive_stats.groupby(['order','RK','accumulator']).get_group((3,RK,acc)))['rtol']
        gmeans = (bruss_adaptive_stats.groupby(['order','RK','accumulator']).get_group((3,RK,acc)))['gmean']
        labeltxt = '{0:1}'.format(acc)
        plt.loglog(rtol, gmeans,'o', label=labeltxt, marker=accsymbol[acc], color=acccolor[acc], linestyle=RKlines[RK])

    plt.xlabel('rtol')
    plt.ylabel(r'$\varepsilon^f_{ref}/\varepsilon^f_{approx}$ (geom. mean)')
    plt.title("Adaptive-step Brusselator")
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()
    plt.grid(linestyle='--', linewidth=0.5)

    if (Generate_PNG):
        plt.savefig('3rd order bruss-ratio-adaptive-stats.png')
    if (Generate_PDF):
        plt.savefig('3rd order bruss-ratio-adaptive-stats.pdf')
    plt.figure()
    for acc in bruss_fixedstep_stats['accumulator'].sort_values().unique():
        RK = 'ERK'
        #for RK in bruss_fixedstep_stats['RK'].sort_values().unique():
        h      = (bruss_fixedstep_stats.groupby(['order','RK','accumulator']).get_group((3,RK,acc)))['h']
        #orders = (bruss_fixedstep_stats.groupby(['h','RK','accumulator']).get_group((h,RK,acc)))['order']
        gmeans = (bruss_fixedstep_stats.groupby(['order','RK','accumulator']).get_group((3,RK,acc)))['gmean']
        labeltxt = '{0:1}'.format(acc)
        plt.loglog(h, gmeans, 'o', label=labeltxt, marker=accsymbol[acc], color=acccolor[acc], linestyle=RKlines[RK])

    plt.xlabel('h')
    plt.ylabel(r'$\varepsilon^f_{ref}/\varepsilon^f_{approx}$ (geom. mean)')
    plt.title("Fixed-step Brusselator")
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()
    plt.grid(linestyle='--', linewidth=0.5)
    #plt.figure()
    if (Generate_PNG):
        plt.savefig('bruss-ratio-fixedstep-stats.png')
    if (Generate_PDF):
        plt.savefig('bruss-ratio-fixedstep-stats.pdf')


## display plots
#plt.show()
