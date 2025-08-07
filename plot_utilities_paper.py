#!/usr/bin/env python3
#------------------------------------------------------------
# Programmer(s):  Daniel R. Reynolds @ SMU
#------------------------------------------------------------
# Copyright (c) 2025, Southern Methodist University.
# All rights reserved.
# For details, see the LICENSE file.
#------------------------------------------------------------

# imports
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

# Set plot defaults: increase default font size, increase plot width, enable LaTeX rendering
plt.rc('font', size=15)
plt.rcParams['figure.figsize'] = [4.8, 7.2]
plt.rcParams['text.usetex'] = True
plt.rcParams['figure.constrained_layout.use'] = True

# flags to turn on/off certain plots
Generate_PDF = True
Generate_PNG = False

# legend locations
accuracy_figsize = (8,7)
accuracy_bbox = (0.55, 0.97)
work_figsize = (9,10)
work_bbox = (0.57, 0.97)
efficiency_figsize = (7,5)
efficiency_bbox = (0.725, 0.775)

# vertical axis limits
#verification_accuracy_ylim = [1e-1, 1e7]
#verification_work_slow_ylim = [1e2, 1e6]
#verification_work_fast_ylim = [1e3, 1e7]
#verification_failrate_ylim = [0, 0.5]

#comparison_accuracy_ylim = [1e-1, 1e9]
#comparison_work_slow_ylim = [1e1, 1e6]
#comparison_work_fast_ylim = [1e2, 1e8]
#comparison_failrate_ylim = [0, 0.5]

# controllers to include in verification plots


usecontrol= {'MRICC':True,
             'MRIDec-H0211':True,
             'MRIDec-H0321':True,
             'MRIDec-H211':True,
             'MRIDec-H312':True,
             'MRIDec-I':True,
             'MRIHTol-H0211':True,
             'MRIHTol-H0321':True,
             'MRIHTol-H211':True,
             'MRIHTol-H312':True,
             'MRIHTol-I':True,
             'MRILL':True,
             'MRIPI':True,
             'MRIPID':True}
method_order = {'ARKODE_MRI_GARK_RALSTON2': 2,
               'ARKODE_MRI_GARK_ERK22a': 2,
               'ARKODE_MRI_GARK_ERK22b': 2,
               'ARKODE_MERK21': 2,
               'ARKODE_MRI_GARK_IRK21a': 2,
               'ARKODE_IMEX_MRI_SR21': 2,
               'ARKODE_MRI_GARK_ERK33a': 3,
               'ARKODE_MERK32': 3,
               'ARKODE_MRI_GARK_ESDIRK34a': 3,
               'ARKODE_IMEX_MRI_SR32': 3,
               'ARKODE_MRI_GARK_ERK45a': 4,
               'ARKODE_MERK43': 4,
               'ARKODE_MRI_GARK_ESDIRK46a': 4,
               'ARKODE_IMEX_MRI_SR43': 4,
               'ARKODE_MERK54': 5,}

cmap10 = plt.get_cmap('tab10')
cmap20 = plt.get_cmap('tab20')

controlcolor= {'MRICC': cmap10(0),
             'MRIDec-H0211': cmap10(1),
             'MRIDec-H0321': cmap10(2),
             'MRIDec-H211': cmap10(3),
             'MRIDec-H312': cmap10(4),
             'MRIDec-I': cmap10(5),
             'MRIHTol-H0211': cmap10(6),
             'MRIHTol-H0321': cmap10(7),
             'MRIHTol-H211': cmap10(8),
             'MRIHTol-H312': cmap10(9),
             'MRIHTol-I': cmap10(10),
             'MRILL': cmap10(11),
             'MRIPI': cmap10(12),
             'MRIPID': cmap10(13),}

controlsymbol = {'MRICC': '.',
                'MRILL': ",",
                'MRIPI': "o",
                'MRIPID': "v",
                'MRIDec-H0211': "s",
                'MRIDec-H0321': "*",
                'MRIDec-H211': "D",
                'MRIDec-I': "p",
                'MRIDec-H312': "<",
                'MRIHTol-H0211': "P",
                'MRIHTol-H0321': "x",
                'MRIHTol-H211': "d",
                'MRIHTol-I': "1",
                'MRIHTol-H312':"$f$",}

methodcolor = {'ARKODE_MRI_GARK_RALSTON2': cmap10(0),
               'ARKODE_MRI_GARK_ERK22a': cmap10(1),
               'ARKODE_MRI_GARK_ERK22b': cmap10(2),
               'ARKODE_MERK21': cmap10(3),
               'ARKODE_MRI_GARK_IRK21a': cmap10(4),
               'ARKODE_IMEX_MRI_SR21': cmap10(5),
               'ARKODE_MRI_GARK_ERK33a': cmap10(0),
               'ARKODE_MERK32': cmap10(1),
               'ARKODE_MRI_GARK_ESDIRK34a': cmap10(2),
               'ARKODE_IMEX_MRI_SR32': cmap10(3),
               'ARKODE_MRI_GARK_ERK45a': cmap10(4),
               'ARKODE_MERK43': cmap10(5),
               'ARKODE_MRI_GARK_ESDIRK46a': cmap10(6),
               'ARKODE_IMEX_MRI_SR43': cmap10(7),
               'ARKODE_MERK54': cmap10(8),}

methodsymbol = {'ARKODE_MRI_GARK_RALSTON2': '.',
               'ARKODE_MRI_GARK_ERK22a': ",",
               'ARKODE_MRI_GARK_ERK22b': "o",
               'ARKODE_MERK21': "v",
               'ARKODE_MRI_GARK_IRK21a': "1",
               'ARKODE_IMEX_MRI_SR21': "s",
               'ARKODE_MRI_GARK_ERK33a': "P",
               'ARKODE_MERK32': "*",
               'ARKODE_MRI_GARK_ESDIRK34a': "x",
               'ARKODE_IMEX_MRI_SR32': "D",
               'ARKODE_MRI_GARK_ERK45a': "d",
               'ARKODE_MERK43': "p",
               'ARKODE_MRI_GARK_ESDIRK46a': "|",
               'ARKODE_IMEX_MRI_SR43': "$f$",
               'ARKODE_MERK54': "<",}

methods_lo = ['ARKODE_MRI_GARK_RALSTON2', 'ARKODE_MRI_GARK_ERK22a', 'ARKODE_MRI_GARK_ERK22b', 'ARKODE_MERK21',
              'ARKODE_MRI_GARK_IRK21a', 'ARKODE_IMEX_MRI_SR21']
methods_mid=['ARKODE_MRI_GARK_ERK33a', 'ARKODE_MERK32', 'ARKODE_MRI_GARK_ESDIRK34a', 'ARKODE_IMEX_MRI_SR32']
methods_hi = [ 'ARKODE_MRI_GARK_ERK45a','ARKODE_MERK43', 'ARKODE_MRI_GARK_ESDIRK46a', 'ARKODE_IMEX_MRI_SR43', 'ARKODE_MERK54']

controltext = {'MRICC': 'Hh-CC',
               'MRILL': 'Hh-LL',
               'MRIPI': 'Hh-PI',
               'MRIPID': 'Hh-PID',
               'MRIHTol-I': 'HT-I',
               'MRIHTol-H0211': 'HT-H0211',
               'MRIHTol-H0321': 'HT-H0321',
               'MRIHTol-H211': 'HT-H211',
               'MRIHTol-H312': 'HT-H312',
               'MRIDec-I': 'D-I',
               'MRIDec-H0211': 'D-H0211',
               'MRIDec-H0321': 'D-H0321',
               'MRIDec-H211': 'D-H211',
               'MRIDec-H312': 'D-H312',}

Hh_controllers={'MRICC',
              'MRILL',
              'MRIPI',
              'MRIPID'}
Htol_controllers={'MRIHTol-H0211',
                'MRIHTol-H0321',
                'MRIHTol-H211',
                'MRIHTol-I',
                'MRIHTol-H312'}
Decoupled_controllers={'MRIDec-H0211',
                'MRIDec-H0321',
                'MRIDec-H211',
                'MRIDec-I',
                'MRIDec-H312',}
con = [("H-h", Hh_controllers),
    ("Htol", Htol_controllers),
    ("Decoupled", Decoupled_controllers)]

# utility functions
def mname(method):
    """
    Splits the method name based on underscores, removes the strings 'ARKODE' and 'GARK' ,
    and joins the results back together with spaces to separate.
    """
    msplit = method.split('_')
    pruned = [s for s in msplit if s != 'ARKODE']
    pruned2 = [s for s in pruned if s != 'GARK']
    pruned3 = [s for s in pruned2 if s != 'MRI']
    return "".join(pruned3)


def print_failed_tests(fname, prefix):
    data = pd.read_excel(fname)
    failed = data[data.ReturnCode != 0]
    print(prefix + ' failed ' + str(len(failed)) + ' tests')
    if (len(failed) > 0):
        print(failed)

def check(control, mri_method,removed_pairs,reverse=0):
    for i in removed_pairs:
        if i==(control,mri_method):
            return (True-reverse)
    return (False+reverse)

def filter_data(fname):
    data=pd.read_excel(fname)
    bad_combos = data.loc[data['ReturnCode'] == 1, ['control', 'mri_method']]
    merged = data.merge(bad_combos.drop_duplicates(), on=['control', 'mri_method'], how='left', indicator=True)
    clean = merged[merged['_merge'] == 'left_only'].drop(columns=['_merge'])
    return clean
def combine():
    probs = ['kpr', 'bruss']
    methods = ['lo.xlsx', 'mid.xlsx', 'hi.xlsx']
    import pandas as pd
    import os
    dfs = []
    for prob in probs:
        for method in methods:
            filename = f"ranks_stats_{prob}-{method}"
            df = pd.read_excel(filename)
            dfs.append(df)
            if os.path.exists(filename) and os.path.exists(prob+'-'+method):
                os.remove(filename)
                os.remove(prob+'-'+method)

            else:
                print("The file does not exist")

    combined = pd.concat(dfs, ignore_index=True)
    combined.to_excel("rank_stats.xlsx", index=False)

def get_work(errorarr, workarr, errorval):
    """
    Given input arrays errorarr = [err0, err1, ..., errN] and workarr = [work0, work1, ..., workN],
    and a value errorval in [min(errorarr), max(errorarr)], this interpolates to estimate the
    corresponding workval.

    If errorval is below min(errorarr), this just returns a huge work number (since this means
    that the method was unable to attain the requested error).
    """
    # check for valid inputs
    if (len(errorarr) != len(workarr)):
        raise ValueError("inputs for errorarr and workarr have differing numbers of entries")
    if (errorval < np.min(errorarr)):
        return 1e20

    return 10**(np.interp(np.log10(errorval), np.log10(errorarr[::-1]), np.log10(workarr[::-1])))



def compare_efficiency(data,param,metric, errorwindow=[1e-6,1e-2], nerr=20):
    """
    Given a list of dictionaries:
       data = [{'method': x1, 'works' : work_array1, 'errors': error_array1},
               {'method': x2, 'works' : work_array2, 'errors': error_array2},
               ... ]
    an optional window of errors to use, and an optional the number of error lines
    (logarithmically-spaced) to test, this routine ranks each method according to
    its overall computational efficiency, returning only the method names, ranked
    from most-to-least efficient.

    If errorwindow is not provided, then this will set the error window to be
      [max_{all methods}(min_{each method}(error)), min_{all methods}(max_{each method}(error))],
    i.e., the range of error values that all methods were able to achieve.

    For each errortest in np.logspace(errorwindow[0], errorwindow[1], nerr), we rank the methods
    according to which one achieves the target error with the minimum amount of work.  These
    rankings are then averaged over all nerr values, and the methods are then ranked according
    to their average rank.

    We return the ranked list of methods as a Pandas dataframe, sorted by
    the average rank.  The fields in the dataframe are: 'MRIMethod', 'Controller',
    'AvgRank'.
    """

    # check for valid inputs
    if (errorwindow is not None):
        if (errorwindow[0] > errorwindow[1]):
            raise ValueError("errorwindow extents are out of order")
    if (nerr < 1):
        raise ValueError("nerr must be at least 1")

    # if needed, automatically create error window
    if (errorwindow is None):
        errorwindow = [0, 0]
        win_min = []
        win_max = []
        for X in data:
            win_min.append(np.min(X['errors']))
            win_max.append(np.max(X['errors']))
        errorwindow[0] = 1.05*np.max(win_min)
        errorwindow[1] = 0.95*np.min(win_max)

    # create array of error test values
    errortests = np.logspace(np.log10(errorwindow[0]), np.log10(errorwindow[1]), nerr)

    # initialize a dictionary of rank sums for each method
    workranks = {}
    for X in data:
        workranks[X['method']] = 0

    # loop over error test values
    for errortest in errortests:

        # get work estimate for each method to attain this error value
        workdict = []
        for X in data:
            workdict.append({'method': X['method'], 'work': get_work(X['errors'], X['works'], errortest)})

        # sort by 'work' values
        sorted_work = sorted(workdict, key=lambda x: x['work'])

        # accumulate ranks for each method, dividing by the number of error test values to build running average
        for i in range(len(sorted_work)):
            s = sorted_work[i]
            workranks[s['method']] += (i+1.0)/nerr

    # sort the method names by their rank sums
    method_ranks = dict(sorted(workranks.items(), key=lambda item: item[1]))

    # create ranked list of dictionaries for return
    ranked_dict = []
    for key, value in method_ranks.items():
        msplit = key.split(' + ')
        MRIMethod = msplit[0]
        Controller = msplit[1]
        AvgRank = value
        ranked_dict.append({'MRIMethod': MRIMethod, 'Controller': Controller,
                            'AvgRank': AvgRank,'order':method_order[MRIMethod],'Param':param, 'metric':metric} )
    ranking_df = pd.DataFrame.from_records(ranked_dict)
    return ranking_df


def make_accuracy_comparison_plot(data, mratekey, mratevals, mratetxt,mri_methods, picname,removed_pairs):
    color={"H-h":'red',
       "Htol":'blue',
       "Decoupled":'green'}
    fig = plt.figure(figsize=accuracy_figsize)
    gs = GridSpec(2, 2, figure=fig)
    ax1 = fig.add_subplot(gs[0,0])  # top-left
    ax2 = fig.add_subplot(gs[1,0])  # middle-left
    Master_data=data
    for group, controllers in con:
        accuracy_max1=np.array([-1e10] * 5)
        accuracy_min1=np.array([1e10] * 5)
        accuracy_max2=np.array([-1e10] * 5)
        accuracy_min2=np.array([1e10] * 5)
        for control in controllers:
            data=Master_data[Master_data['control'] == control]
            for mri_method in mri_methods:
                # skip over failed tests
                if check(control,mri_method,removed_pairs):
                    continue

                # first multirate value
                mrate = mratevals[0]
                rtol = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['rtol'].array
                accuracy = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['Accuracy'].array
                accuracy_min1=np.minimum(accuracy_min1,accuracy)
                accuracy_max1=np.maximum(accuracy_max1,accuracy)
                # this plots the lines within the bands
                #ax1.loglog(rtol, accuracy, marker=msymbol, color=mcolor, ls='-', markersize=10)
                ax1.loglog()

                # second multirate value
                mrate = mratevals[1]
                rtol = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['rtol'].array
                accuracy = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['Accuracy'].array
                accuracy_min2=np.minimum(accuracy_min2,accuracy)
                accuracy_max2=np.maximum(accuracy_max2,accuracy)

                #ax2.loglog(rtol, accuracy, marker=msymbol, color=mcolor, ls='-', markersize=10)
                ax2.loglog()
        ax1.fill_between(rtol, accuracy_min1, accuracy_max1, color=color[group], alpha=0.25,label=group)
        ax2.fill_between(rtol, accuracy_min2, accuracy_max2, color=color[group], alpha=0.25,label=group)
    handles, labels = ax1.get_legend_handles_labels()
    ax1.set_xlabel(r'reltol')
    ax1.set_ylabel(r'accuracy '+ mratetxt + ' = ' + str(mratevals[0]))
    ax2.set_xlabel(r'reltol')
    ax2.set_ylabel(r'accuracy '+ mratetxt + ' = ' + str(mratevals[1]))
    ax1.grid(linestyle='--', linewidth=0.5)
    ax2.grid(linestyle='--', linewidth=0.5)
    fig.legend(handles, labels, title='Family', loc='upper left', bbox_to_anchor=accuracy_bbox)
    if (Generate_PNG):
        plt.savefig(picname+" filled in" + '.png')
    if (Generate_PDF):
        plt.savefig(picname + " filled in"+'.pdf')

def make_efficiency_comparison_plot(data, mratekey, mratevals, controllers, mri_methods, titletxt,rank_name):

    comparison_data_slow1 = []
    comparison_data_fast1 = []
    comparison_data_slow2 = []
    comparison_data_fast2 = []
    Master_data=data
    cut_off_rank=12
    for control in controllers:
        data=Master_data[Master_data['control'] == control]
        for mri_method in mri_methods:

            # first multirate value
            mrate = mratevals[0]
            rtol = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['rtol']
            accuracy = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['Accuracy']
            error = accuracy*rtol
            slowsteps = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['SlowSteps'].array
            slowfails = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['SlowFails'].array
            faststeps = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['FastSteps'].array
            fastfails = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['FastFails'].array
            comparison_data_slow1.append({'method': mri_method+' + '+control, 'works': slowsteps+slowfails, 'errors': error})
            comparison_data_fast1.append({'method': mri_method+' + '+control, 'works': faststeps+fastfails, 'errors': error})

            # second multirate value
            mrate = mratevals[1]
            rtol = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['rtol']
            accuracy = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['Accuracy']
            error = accuracy*rtol
            slowsteps = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['SlowSteps'].array
            slowfails = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['SlowFails'].array
            faststeps = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['FastSteps'].array
            fastfails = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['FastFails'].array
            comparison_data_slow2.append({'method': mri_method+' + '+control, 'works': slowsteps+slowfails, 'errors': error})
            comparison_data_fast2.append({'method': mri_method+' + '+control, 'works': faststeps+fastfails, 'errors': error})

    # output efficiency comparisons for both multirate values and for both slow/fast work
    ranks_slow1 = compare_efficiency(comparison_data_slow1,mratevals[0],'slow')
    ranks_slow1_loc=ranks_slow1.loc[ranks_slow1['AvgRank'] <= cut_off_rank, ['Controller', 'MRIMethod']]

    print('For ', titletxt, ' and mrateval = ', mratevals[0], ' the slow efficiency method ranks are:')
    print(ranks_slow1)

    ranks_fast1 = compare_efficiency(comparison_data_fast1,mratevals[0],'fast')
    ranks_fast1_loc=ranks_fast1.loc[ranks_fast1['AvgRank'] <= cut_off_rank, ['Controller', 'MRIMethod']]

    print('For ', titletxt, ' and mrateval = ', mratevals[0], ' the fast efficiency method ranks are:')
    print(ranks_fast1)

    ranks_slow2 = compare_efficiency(comparison_data_slow2,mratevals[1],'slow')
    ranks_slow2_loc=ranks_slow2.loc[ranks_slow2['AvgRank'] <= cut_off_rank, ['Controller', 'MRIMethod']]

    print('For ', titletxt, ' and mrateval = ', mratevals[1], ' the slow efficiency method ranks are:')
    print(ranks_slow2)

    ranks_fast2 = compare_efficiency(comparison_data_fast2,mratevals[1],'fast')
    ranks_fast2_loc=ranks_fast2.loc[ranks_fast2['AvgRank'] <= cut_off_rank, ['Controller', 'MRIMethod']]

    print('For ', titletxt, ' and mrateval = ', mratevals[1], ' the fast efficiency method ranks are:')
    print(ranks_fast2)

    # keeps all pairs who attains a low rank for both mrate values
    rankslow= pd.merge(ranks_slow1_loc,ranks_slow2_loc, on=['Controller', 'MRIMethod'], how='inner')
    rankfast= pd.merge(ranks_fast1_loc,ranks_fast2_loc, on=['Controller', 'MRIMethod'], how='inner')
    #ranks=pd.concat([rankslow,rankfast]).drop_duplicates()


    # keeps all pairs who attains a low rank any any mrate values
    #ranks=pd.concat([ranks_slow1_loc,ranks_fast1_loc,ranks_slow2_loc,ranks_fast2_loc]).drop_duplicates()

    rankslow.to_excel(rank_name+'slow.xlsx',index=False)
    rankfast.to_excel(rank_name+'fast.xlsx',index=False)

    # output statistic dataframe
    ranks_stats_df=pd.concat([ranks_slow1,ranks_fast1,ranks_slow2,ranks_fast2])
    ranks_stats_df.to_excel('ranks_stats_'+rank_name+'.xlsx',index=False)

def best_efficiencies_comparison_plot(data, mratekey, mratevals, mratetxt, controllers, mri_methods,rank_names,xlim1,xlim2,xlim3,xlim4):


    fig = plt.figure(figsize=efficiency_figsize)
    fig2 = plt.figure(figsize=efficiency_figsize)
    gs = GridSpec(1, 3, figure=fig)
    gs2 = GridSpec(1, 3, figure=fig2)
    ax1 = fig.add_subplot(gs[0,0])  # top-left
    ax2 = fig2.add_subplot(gs2[0,0])  # top-middle
    ax3 = fig.add_subplot(gs[0,1])  # bottom-left
    ax4 = fig2.add_subplot(gs2[0,1])  # bottom-middle

    retained_pairs=pd.read_excel(rank_names+'slow.xlsx')
    retained_pairs=list(retained_pairs.itertuples(index=False, name=None))
    comparison_data_slow1 = []
    comparison_data_fast1 = []
    comparison_data_slow2 = []
    comparison_data_fast2 = []
    Master_data=data
    for control in controllers:
        data=Master_data[Master_data['control'] == control]
        for mri_method in mri_methods:
            if check(control,mri_method,retained_pairs,reverse=1):
                continue
            ltext = mname(mri_method)+'+'+controltext[control]
            mcolor = methodcolor[mri_method]
            msymbol = controlsymbol[control]

            # first multirate value
            mrate = mratevals[0]
            rtol = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['rtol']
            accuracy = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['Accuracy']
            error = accuracy*rtol
            slowsteps = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['SlowSteps'].array
            slowfails = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['SlowFails'].array
            faststeps = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['FastSteps'].array
            fastfails = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['FastFails'].array
            ax1.loglog(slowsteps+slowfails, error, marker=msymbol, color=mcolor, ls='-', label=ltext, markersize=10)
            #ax2.loglog(faststeps+fastfails, error, marker=msymbol, color=mcolor, ls='-', label=ltext, markersize=10)
            comparison_data_slow1.append({'method': mri_method+' + '+control, 'works': slowsteps+slowfails, 'errors': error})
            #comparison_data_fast1.append({'method': mri_method+' + '+control, 'works': faststeps+fastfails, 'errors': error})

            # second multirate value
            mrate = mratevals[1]
            rtol = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['rtol']
            accuracy = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['Accuracy']
            error = accuracy*rtol
            slowsteps = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['SlowSteps'].array
            slowfails = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['SlowFails'].array
            faststeps = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['FastSteps'].array
            fastfails = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['FastFails'].array
            ax3.loglog(slowsteps+slowfails, error, marker=msymbol, color=mcolor, ls='-', label=ltext, markersize=10)
            #ax4.loglog(faststeps+fastfails, error, marker=msymbol, color=mcolor, ls='-', label=ltext, markersize=10)
            comparison_data_slow2.append({'method': mri_method+' + '+control, 'works': slowsteps+slowfails, 'errors': error})
            #comparison_data_fast2.append({'method': mri_method+' + '+control, 'works': faststeps+fastfails, 'errors': error})

    retained_pairs=pd.read_excel(rank_names+'fast.xlsx')
    retained_pairs=list(retained_pairs.itertuples(index=False, name=None))
    for control in controllers:
        data=Master_data[Master_data['control'] == control]
        for mri_method in mri_methods:
            if check(control,mri_method,retained_pairs,reverse=1):
                continue
            ltext = mname(mri_method)+'+'+controltext[control]
            mcolor = methodcolor[mri_method]
            msymbol = controlsymbol[control]

            # first multirate value
            mrate = mratevals[0]
            rtol = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['rtol']
            accuracy = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['Accuracy']
            error = accuracy*rtol
            slowsteps = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['SlowSteps'].array
            slowfails = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['SlowFails'].array
            faststeps = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['FastSteps'].array
            fastfails = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['FastFails'].array
            #ax1.loglog(slowsteps+slowfails, error, marker=msymbol, color=mcolor, ls='-', label=ltext, markersize=10)
            ax2.loglog(faststeps+fastfails, error, marker=msymbol, color=mcolor, ls='-', label=ltext, markersize=10)
            #comparison_data_slow1.append({'method': mri_method+' + '+control, 'works': slowsteps+slowfails, 'errors': error})
            comparison_data_fast1.append({'method': mri_method+' + '+control, 'works': faststeps+fastfails, 'errors': error})

            # second multirate value
            mrate = mratevals[1]
            rtol = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['rtol']
            accuracy = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['Accuracy']
            error = accuracy*rtol
            slowsteps = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['SlowSteps'].array
            slowfails = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['SlowFails'].array
            faststeps = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['FastSteps'].array
            fastfails = (data.groupby([mratekey,'mri_method']).get_group((mrate,mri_method)))['FastFails'].array
            #ax3.loglog(slowsteps+slowfails, error, marker=msymbol, color=mcolor, ls='-', label=ltext, markersize=10)
            ax4.loglog(faststeps+fastfails, error, marker=msymbol, color=mcolor, ls='-', label=ltext, markersize=10)
            #comparison_data_slow2.append({'method': mri_method+' + '+control, 'works': slowsteps+slowfails, 'errors': error})
            comparison_data_fast2.append({'method': mri_method+' + '+control, 'works': faststeps+fastfails, 'errors': error})
    handles, labels = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
   # fig.suptitle('top pairs' +rank_names+ ' efficiency')
    ax1.set_xlabel(r'slow work')
    ax2.set_xlabel(r'fast work')
    ax3.set_xlabel(r'slow work')
    ax4.set_xlabel(r'fast work')
    ax1.set_ylabel(r'error, ' + mratetxt + ' = ' + str(mratevals[0]))
    ax2.set_ylabel(r'error, ' + mratetxt + ' = ' + str(mratevals[1]))

    ax1.set_xlim(xlim1)
    ax2.set_xlim(xlim2)
    ax3.set_xlim(xlim3)
    ax4.set_xlim(xlim4)

    ax1.grid(linestyle='--', linewidth=0.5)
    ax2.grid(linestyle='--', linewidth=0.5)
    ax3.grid(linestyle='--', linewidth=0.5)
    ax4.grid(linestyle='--', linewidth=0.5)




    fig.legend(handles, labels, title='Method + Controller', loc='upper left', bbox_to_anchor=efficiency_bbox,fontsize=10)
    fig2.legend(handles2, labels2, title='Method + Controller', loc='upper left', bbox_to_anchor=efficiency_bbox,fontsize=10)
    if (Generate_PNG):
        plt.savefig('top_pairs'+rank_names + '.png')
    if (Generate_PDF):
        plt.savefig('paper-top_pairs_efficencies_'+rank_names + '.pdf')

def do_comparison_plots(fname, mratekey, mratevals, mratetxt,controllers, titletxt, picname,removed_pairs,rank_name,xlimlo,xlimmid,xlimhi):

    """
    Given a saved Pandas dataframe file with results, and strings containing the base
    title and base output file name (without suffix), this does the following:
    1. Loads the data file
    2. Constructs a plot of the reported "accuracy" of each 2nd order MRI method for
       each multirate value, and saves to disk
    3. Constructs a plot of the reported "accuracy" of each 3rd order MRI method for
       each multirate value, and saves to disk
    4. Constructs a plot of the reported "accuracy" of each 4th/5th order MRI method
       for each multirate value, and saves to disk
    5. Constructs a plot of the reported "work" of each 2nd order MRI method at both
       slow and fast time scales for each multirate value, and saves to disk
    6. Constructs a plot of the reported "work" of each 3rd order MRI method at
       both slow and fast time scales for each multirate value, and saves to disk
    7. Constructs a plot of the reported "work" of each 4th/5th order MRI method at
       both slow and fast time scales for each multirate value, and saves to disk
    8. Constructs plots of the "computational efficieny" at both the slow and fast
       time scales for each 2nd order MRI method at each multirate value, and saves to disk
    9. Constructs plots of the "computational efficieny" at both the slow and fast
       time scales for each 3rd order MRI method at each multirate value, and saves to disk
   10. Constructs plots of the "computational efficieny" at both the slow and fast
       time scales for each 4th/5th order MRI method at each multirate value, and saves to disk
    """
    data = pd.read_excel(fname)
    #data = filter_data(fname)
    # verify that there are only 2 mrate values
    if (len(mratevals) != 2):
        raise ValueError('Error: this function can only be run with 2 multirate values')

    # accuracy plots
    make_accuracy_comparison_plot(data, mratekey, mratevals, mratetxt, methods_lo, picname+'-accuracy-lo',removed_pairs)
    make_accuracy_comparison_plot(data, mratekey, mratevals, mratetxt, methods_mid, picname+'-accuracy-mid',removed_pairs)
    make_accuracy_comparison_plot(data, mratekey, mratevals, mratetxt, methods_hi, picname+'-accuracy-hi',removed_pairs)

    # efficiency plots
    make_efficiency_comparison_plot(data, mratekey, mratevals, controllers, methods_lo,  titletxt, rank_name+'-lo')
    make_efficiency_comparison_plot(data, mratekey, mratevals, controllers, methods_mid, titletxt, rank_name+'-mid')
    make_efficiency_comparison_plot(data, mratekey, mratevals, controllers, methods_hi,  titletxt,rank_name+'-hi')

    best_efficiencies_comparison_plot(data, mratekey, mratevals, mratetxt,controllers, methods_lo, rank_name+'-lo',xlimlo[0],xlimlo[1],xlimlo[2],xlimlo[3])
    best_efficiencies_comparison_plot(data, mratekey, mratevals, mratetxt,controllers, methods_mid,rank_name+'-mid',xlimmid[0],xlimmid[1],xlimmid[2],xlimmid[3])
    best_efficiencies_comparison_plot(data, mratekey, mratevals, mratetxt, controllers, methods_hi,rank_name+'-hi',xlimhi[0],xlimhi[1],xlimhi[2],xlimhi[3])
