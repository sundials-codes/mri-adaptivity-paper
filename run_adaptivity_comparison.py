#!/usr/bin/env python3
#------------------------------------------------------------
# Programmer(s):  Daniel R. Reynolds @ SMU
#------------------------------------------------------------
# Copyright (c) 2024, Southern Methodist University.
# All rights reserved.
# For details, see the LICENSE file.
#------------------------------------------------------------

# imports
import os
import subprocess
import shlex
import sys
import pandas as pd
sys.path.append('sundials-v7.3.0/tools')
from suntools import logs as sunlog

#####################
# utility routines

# controller parameters
def controller(method):
    match method:
        case 'MRICC':
            txt = ' --scontrol 1 --fcontrol 0 --safety 0.85'
        case 'MRILL':
            txt = ' --scontrol 2 --fcontrol 0 --safety 0.85'
        case 'MRIPI':
            txt = ' --scontrol 3 --fcontrol 0 --safety 0.85'
        case 'MRIPID':
            txt = ' --scontrol 4 --fcontrol 0 --safety 0.85'
        case 'MRIHTol-I':
            txt = ' --scontrol 5 --fcontrol 1'
        case 'MRIDec-I':
            txt = ' --scontrol 6 --fcontrol 1'
        case 'MRIHTol-H0211':
            txt = ' --scontrol 17 --fcontrol 7'
        case 'MRIDec-H0211':
            txt = ' --scontrol 18 --fcontrol 7'
        case 'MRIHTol-H0321':
            txt = ' --scontrol 19 --fcontrol 8'
        case 'MRIDec-H0321':
            txt = ' --scontrol 20 --fcontrol 8'
        case 'MRIHTol-H211':
            txt = ' --scontrol 21 --fcontrol 9'
        case 'MRIDec-H211':
            txt = ' --scontrol 22 --fcontrol 9'
        case 'MRIHTol-H312':
            txt = ' --scontrol 23 --fcontrol 10'
        case 'MRIDec-H312':
            txt = ' --scontrol 24 --fcontrol 10'
        case _:
            txt = ' '
    return txt

# utility routine to run a kpr test, storing the run options and solver statistics
def runtest_kpr(exe, e, omega, atol, rtol, mri, order, control, showcommand=True, removelog=False):
    stats = {'e': e, 'omega': omega, 'atol': atol, 'rtol': rtol, 'mri_method': mri, 'fast_order': order, 'control': control, 'ReturnCode': 1, 'T': [], 'H': [], 't': [], 'h': [], 'Accuracy': []}
    runcommand = "%s --e %e --w %e --atol %e --rtol %e --fast_rtol %e --mri_method %s --fast_order %d" % (exe, e, omega, atol, rtol, rtol, mri, order) + controller(control)
    logfile = 'kpr-log-' + control + '.txt'
    env = os.environ.copy()
    env["SUNLOGGER_DEBUG_FILENAME"] = logfile
    result = subprocess.run(shlex.split(runcommand), stdout=subprocess.PIPE, env=env)
    stats['ReturnCode'] = result.returncode
    if (result.returncode != 0):
        print("Run command " + runcommand + " FAILURE: " + str(result.returncode))
        print(result.stderr)
    else:
        if (showcommand):
            print("Run command " + runcommand + " SUCCESS")
        log = sunlog.log_file_to_list(logfile)
        stepidx, times, stepsizes = sunlog.get_history(log, "h", group_by_level=True)
        stats['T'] = times[0]
        stats['H'] = stepsizes[0]
        stats['t'] = times[1]
        stats['h'] = stepsizes[1]
        lines = str(result.stdout).split('\\n')
        for line in lines:
            txt = line.split()
            if ("Relative" in txt):
                stats['Accuracy'] = float(txt[3])
    if (os.path.isfile(logfile) and removelog):
        if (showcommand):
            print("Removing log file")
        os.remove(logfile)
    return stats

def runtest_brusselator(exe, ep, atol, rtol, mri, order, control, showcommand=True, removelog=False):
    stats = {'ep': ep, 'atol': atol, 'rtol': rtol, 'mri_method': mri, 'fast_order': order, 'control': control, 'ReturnCode': 1, 'T': [], 'H': [], 't': [], 'h': [], 'Accuracy': []}
    runcommand = "%s --ep %e --atol %e --rtol %e --fast_rtol %e --mri_method %s --fast_order %d" % (exe, ep, atol, rtol, rtol, mri, order) + controller(control)
    logfile = 'bruss-log-' + control + '.txt'
    env = os.environ.copy()
    env["SUNLOGGER_DEBUG_FILENAME"] = logfile
    result = subprocess.run(shlex.split(runcommand), stdout=subprocess.PIPE, env=env)
    stats['ReturnCode'] = result.returncode
    if (result.returncode != 0):
        print("Run command " + runcommand + " FAILURE: " + str(result.returncode))
        print(result.stderr)
    else:
        if (showcommand):
            print("Run command " + runcommand + " SUCCESS")
        log = sunlog.log_file_to_list(logfile)
        stepidx, times, stepsizes = sunlog.get_history(log, "h", group_by_level=True)
        stats['T'] = times[0]
        stats['H'] = stepsizes[0]
        stats['t'] = times[1]
        stats['h'] = stepsizes[1]
        lines = str(result.stdout).split('\\n')
        for line in lines:
            txt = line.split()
            if ("Relative" in txt):
                stats['Accuracy'] = float(txt[3])
    if (os.path.isfile(logfile) and removelog):
        if (showcommand):
            print("Removing log file")
        os.remove(logfile)
    return stats


# common testing parameters
kpr_exe = './bin/ark_test_kpr_mriadapt_logging'
kpr_hh_exe = './bin/ark_test_kpr_mriadapt_hh_logging'
bruss_exe = './bin/ark_test_brusselator_mriadapt_logging'
bruss_hh_exe = './bin/ark_test_brusselator_mriadapt_hh_logging'
rtol = 1.e-5
atol = 1.e-11
mri_method = "ARKODE_MRI_GARK_ERK33a"
fast_order = 3
omega = 50.0  # kpr multirate parameter
e = 5.0       # kpr coupling parameter
eps = 1.e-4   # bruss parameter

# empty statistics objects
KPRStats = []
BrussStats = []

# Run both test problems using a few controllers
KPRStats.append(runtest_kpr(kpr_exe, e, omega, atol, rtol, mri_method, fast_order, 'MRIDec-H211'))
KPRStats.append(runtest_kpr(kpr_exe, e, omega, atol, rtol, mri_method, fast_order, 'MRIHTol-H211'))
KPRStats.append(runtest_kpr(kpr_hh_exe, e, omega, atol, rtol, mri_method, fast_order, 'MRICC'))

KPRDf = pd.DataFrame.from_records(KPRStats)
print("KPRDf object:")
print(KPRDf)
print("Saving as Excel")
KPRDf.to_excel('kpr_adapt_comparison_results.xlsx', index=False)


BrussStats.append(runtest_brusselator(bruss_exe, eps, atol, rtol, mri_method, fast_order, 'MRIDec-H211'))
BrussStats.append(runtest_brusselator(bruss_exe, eps, atol, rtol, mri_method, fast_order, 'MRIHTol-H211'))
BrussStats.append(runtest_brusselator(bruss_hh_exe, eps, atol, rtol, mri_method, fast_order, 'MRICC'))

BrussDf = pd.DataFrame.from_records(BrussStats)
print("BrussDf object:")
print(BrussDf)
print("Saving as Excel")
BrussDf.to_excel('brusselator_adapt_comparison_results.xlsx', index=False)
