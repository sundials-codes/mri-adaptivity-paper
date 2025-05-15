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
import pickle
sys.path.append('sundials-v7.3.0/tools')
from suntools import logs as sunlog

# testing executables
kpr_exe = './bin/ark_test_kpr_mriadapt_logging'
kpr_hh_exe = './bin/ark_test_kpr_mriadapt_hh_logging'
bruss_exe = './bin/ark_test_brusselator_mriadapt_logging'
bruss_hh_exe = './bin/ark_test_brusselator_mriadapt_hh_logging'


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

# utility routine to process a logging output file from sundials-mrihh branch to store step size and error estimates from within a multirate run
def get_mrihh_step_histories(fname):
    T = []
    H = []
    DSM = []
    t = []
    h = []
    dsm = []
    # open file and process results
    f = open(fname)
    separators = '[],:'
    SSteps = 0
    FSteps = 0
    for line in f:
        for sep in separators:
            line = line.replace(sep, " ")
        txt = line.split()
        if (("mriStep_TakeStepMERK" in txt) and ("end-step" in txt)):
            T.append(float(txt[11]))
            H.append(float(txt[14]))
            DSM.append(float(txt[17]))
        if (("mriStep_TakeStepMRIGARK" in txt) and ("end-step" in txt)):
            T.append(float(txt[11]))
            H.append(float(txt[14]))
            DSM.append(float(txt[17]))
        if (("mriStep_TakeStepMRISR" in txt) and ("end-step" in txt)):
            T.append(float(txt[11]))
            H.append(float(txt[14]))
            DSM.append(float(txt[17]))
        if (("erkStep_TakeStep" in txt) and ("end-step" in txt)):
            t.append(float(txt[11]))
            h.append(float(txt[14]))
            dsm.append(float(txt[17]))
        if (("arkStep_TakeStep_Z" in txt) and ("end-step" in txt)):
            t.append(float(txt[11]))
            h.append(float(txt[14]))
            dsm.append(float(txt[17]))
    f.close()
    return T, H, DSM, t, h, dsm


# utility routine to run a kpr test, storing the run options and solver statistics
def runtest_kpr(exe, e, omega, atol, rtol, mri, order, control, showcommand=True, removelog=False):
    stats = {'e': e, 'omega': omega, 'atol': atol, 'rtol': rtol, 'mri_method': mri, 'fast_order': order, 'control': control, 'ReturnCode': 1, 'T': [], 'H': [], 't': [], 'h': [], 'Accuracy': []}
    runcommand = "%s --e %e --w %e --atol %e --rtol %e --fast_rtol %e --mri_method %s --fast_order %d" % (exe, e, omega, atol, rtol, rtol, mri, order) + controller(control)
    logfile = 'kpr-log-' + control + '.txt'
    env = os.environ.copy()
    env["SUNLOGGER_INFO_FILENAME"] = logfile
    env["SUNLOGGER_DEBUG_FILENAME"] = logfile
    result = subprocess.run(shlex.split(runcommand), stdout=subprocess.PIPE, env=env)
    stats['ReturnCode'] = result.returncode
    if (result.returncode != 0):
        print("Run command " + runcommand + " FAILURE: " + str(result.returncode))
        print(result.stderr)
    else:
        if (showcommand):
            print("Run command " + runcommand + " SUCCESS")
        if (exe == kpr_exe):
            log = sunlog.log_file_to_list(logfile)
            stepidx, times, stepsizes = sunlog.get_history(log, "h", group_by_level=True)
            stats['T'] = times[0]
            stats['H'] = stepsizes[0]
            stats['t'] = times[1]
            stats['h'] = stepsizes[1]
        else:
            T, H, DSM, t, h, dsm = get_mrihh_step_histories(logfile)
            stats['T'] = T
            stats['H'] = H
            stats['t'] = t
            stats['h'] = h
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
    env["SUNLOGGER_INFO_FILENAME"] = logfile
    env["SUNLOGGER_DEBUG_FILENAME"] = logfile
    result = subprocess.run(shlex.split(runcommand), stdout=subprocess.PIPE, env=env)
    stats['ReturnCode'] = result.returncode
    if (result.returncode != 0):
        print("Run command " + runcommand + " FAILURE: " + str(result.returncode))
        print(result.stderr)
    else:
        if (showcommand):
            print("Run command " + runcommand + " SUCCESS")
        if (exe == bruss_exe):
            log = sunlog.log_file_to_list(logfile)
            stepidx, times, stepsizes = sunlog.get_history(log, "h", group_by_level=True)
            stats['T'] = times[0]
            stats['H'] = stepsizes[0]
            stats['t'] = times[1]
            stats['h'] = stepsizes[1]
        else:
            T, H, DSM, t, h, dsm = get_mrihh_step_histories(logfile)
            stats['T'] = T
            stats['H'] = H
            stats['t'] = t
            stats['h'] = h
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
KPRStats.append(runtest_kpr(kpr_exe, e, omega, atol, rtol, mri_method, fast_order, 'MRIDec-H312'))
KPRStats.append(runtest_kpr(kpr_exe, e, omega, atol, rtol, mri_method, fast_order, 'MRIHTol-H211'))
KPRStats.append(runtest_kpr(kpr_hh_exe, e, omega, atol, rtol, mri_method, fast_order, 'MRICC'))

BrussStats.append(runtest_brusselator(bruss_exe, eps, atol, rtol, mri_method, fast_order, 'MRIDec-H312'))
BrussStats.append(runtest_brusselator(bruss_exe, eps, atol, rtol, mri_method, fast_order, 'MRIHTol-H211'))
BrussStats.append(runtest_brusselator(bruss_hh_exe, eps, atol, rtol, mri_method, fast_order, 'MRICC'))

with open('kpr_adapt_comparison_results.pkl', 'wb') as file:
    pickle.dump(KPRStats, file)
with open('brusselator_adapt_comparison_results.pkl', 'wb') as file:
    pickle.dump(BrussStats, file)
