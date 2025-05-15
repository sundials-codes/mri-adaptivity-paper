#!/usr/bin/env python3
#------------------------------------------------------------
# Programmer(s):  Daniel R. Reynolds @ SMU
#------------------------------------------------------------
# Copyright (c) 2024, Southern Methodist University.
# All rights reserved.
# For details, see the LICENSE file.
#------------------------------------------------------------

# imports
import pickle
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

# Set plot defaults: increase default font size, increase plot width, enable LaTeX rendering
plt.rc('font', size=15)
#plt.rcParams['figure.figsize'] = [8, 4]
plt.rcParams['text.usetex'] = True
plt.rcParams['figure.constrained_layout.use'] = True

# flags to turn on/off certain plots
Generate_PDF = True
Generate_PNG = False
NPlotSlow = 200
NPlotFast = 1000

# utility functions
cmap = plt.get_cmap('tab10')
controlcolor = {'MRIHTol-I': cmap(0),
                'MRIHTol-H0211': cmap(1),
                'MRIHTol-H0321': cmap(2),
                'MRIHTol-H211': cmap(3),
                'MRIHTol-H312': cmap(4),
                'MRIDec-I': cmap(5),
                'MRIDec-H0211': cmap(6),
                'MRIDec-H0321': cmap(7),
                'MRIDec-H211': cmap(8),
                'MRIDec-H312': cmap(9),
                'MRICC': cmap(0),
                'MRILL': cmap(1),
                'MRIPI': cmap(2),
                'MRIPID': cmap(3)}

def do_test_plots(fname, titletxt, picname, slowstride=None, faststride=None):
    """
    fname = filename with pickled data
    titletxt = string for plot title
    picname = string for output file name (without suffix)
    slowstride = sampling frequency for slow time scale plot
    faststride = sampling frequency for fast time scale plot
    """
    if (slowstride != None):
        sstride = slowstride
    if (faststride != None):
        fstride = faststride
    with open(fname, 'rb') as file:
        data = pickle.load(file)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12,6))
    for i in range(len(data)):
        runstats = data[i]
        control = runstats['control']
        pcolor = controlcolor[control]
        Nslow = len(np.array(runstats['H']))
        Nfast = len(np.array(runstats['h']))
        accuracy = runstats['Accuracy']

        arr = np.array(runstats['H'])
        if (slowstride == None):
            sstride = len(arr)//NPlotSlow
        Hvals = np.mean(arr[:len(arr) - (len(arr) % sstride)].reshape(-1, sstride), axis=1)
        Tvals = (np.array(runstats['T'])[::sstride])[:len(Hvals)]
        ltext = control + '\n steps: ' + str(Nslow) + ', ' + str(Nfast) + '\n accuracy: ' + f"{accuracy:.1f}"
        ax1.semilogy(Tvals, Hvals, color=pcolor, marker='.', ls='none', label=ltext)

        arr = np.array(runstats['h'])
        if (faststride == None):
            fstride = len(arr)//NPlotFast
        hvals = np.mean(arr[:len(arr) - (len(arr) % fstride)].reshape(-1, fstride), axis=1)
        tvals = (np.array(runstats['t'])[::fstride])[:len(hvals)]
        ax2.semilogy(tvals, hvals, color=pcolor, marker='.', ls='none', label=ltext)

    handles, labels = ax1.get_legend_handles_labels()
    ax1.set_ylabel('$H$')
    ax1.grid(linestyle='--', linewidth=0.5)
    ax2.set_xlabel('$t$')
    ax2.set_ylabel('$h$')
    ax2.grid(linestyle='--', linewidth=0.5)
    ax1.set_title(titletxt + ' step size history')
    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    box = ax2.get_position()
    ax2.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    lgtitle = 'Controller'
    ax1.legend(loc='upper left', title=lgtitle, bbox_to_anchor=(1.01, 1), borderaxespad=0)
    if (Generate_PNG):
        plt.savefig(picname + '.png')
    if (Generate_PDF):
        plt.savefig(picname + '.pdf')


# generate plots
#slowstride = 1
#faststride = 10
slowstride = None
faststride = None
do_test_plots('kpr_adapt_comparison_results.pkl', 'KPR', 'kpr-history', slowstride, faststride)

#slowstride = 5
#faststride = 50
slowstride = None
faststride = None
do_test_plots('brusselator_adapt_comparison_results.pkl', 'Stiff Brusselator', 'bruss-history', slowstride, faststride)

# display plots
plt.show()
