#!/usr/bin/env python3
#------------------------------------------------------------
# Programmer(s):  Daniel R. Reynolds @ SMU
#------------------------------------------------------------
# Copyright (c) 2025, Southern Methodist University.
# All rights reserved.
# For details, see the LICENSE file.
#------------------------------------------------------------

# imports
import pandas as pd
import subprocess
import shlex

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

# utility routine to run a single KPR test, storing the run options and solver statistics
def runtest_kpr(exe, es, ef, omega, atol, rtol, mri, order, control, showcommand=False):
    stats = {'es': es, 'ef': ef, 'omega': omega, 'atol': atol, 'rtol': rtol, 'mri_method': mri, 'fast_order': order, 'control': control, 'ReturnCode': 1, 'SlowSteps': 1e10, 'SlowFails': 1e10, 'FastSteps': 1e10, 'FastFails': 1e10, 'Accuracy': 1e10, 'FfEvals': 1e10, 'FseEvals': 1e10, 'FsiEvals': 1e10}
    runcommand = "%s --es %e --ef %e --w %e --atol %e --rtol %e --fast_rtol %e --mri_method %s --fast_order %d" % (exe, es, ef, omega, atol, rtol, rtol, mri, order) + controller(control)
    result = subprocess.run(shlex.split(runcommand), stdout=subprocess.PIPE)
    stats['ReturnCode'] = result.returncode
    if (result.returncode != 0):
        print("Run command " + runcommand + " FAILURE: " + str(result.returncode))
        print(result.stderr)
    else:
        if (showcommand):
            print("Run command " + runcommand + " SUCCESS")
        lines = str(result.stdout).split('\\n')
        for line in lines:
            txt = line.split()
            if (("Slow" in txt) and ("steps" in txt)):
                stats['SlowSteps'] = int(txt[3])
                stats['SlowFails'] = int((txt[9].split(")"))[0])
            elif (("Fast" in txt) and ("steps" in txt)):
                stats['FastSteps'] = int(txt[3])
                stats['FastFails'] = int((txt[9].split(")"))[0])
            elif ("Relative" in txt):
                stats['Accuracy'] = float(txt[3])
            elif ("RHS" in txt):
                stats['FfEvals'] = int(txt[11])
                stats['FseEvals'] = int((txt[5].split(","))[0])
                stats['FsiEvals'] = int((txt[8].split(","))[0])
    return stats

# utility routine to run a single Brusselator test, storing the run options and solver statistics
def runtest_brusselator(exe, ep, atol, rtol, mri, order, control, showcommand=False):
    stats = {'ep': ep, 'atol': atol, 'rtol': rtol, 'mri_method': mri, 'fast_order': order, 'control': control, 'ReturnCode': 1, 'SlowSteps': 1e10, 'SlowFails': 1e10, 'FastSteps': 1e10, 'FastFails': 1e10, 'Accuracy': 1e10, 'FfEvals': 1e10, 'FseEvals': 1e10, 'FsiEvals': 1e10}
    runcommand = "%s --ep %e --atol %e --rtol %e --fast_rtol %e --mri_method %s --fast_order %d" % (exe, ep, atol, rtol, rtol, mri, order) + controller(control)
    result = subprocess.run(shlex.split(runcommand), stdout=subprocess.PIPE)
    stats['ReturnCode'] = result.returncode
    if (result.returncode != 0):
        print("Run command " + runcommand + " FAILURE: " + str(result.returncode))
        print(result.stderr)
    else:
        if (showcommand):
            print("Run command " + runcommand + " SUCCESS")
        lines = str(result.stdout).split('\\n')
        for line in lines:
            txt = line.split()
            if (("Slow" in txt) and ("steps" in txt)):
                stats['SlowSteps'] = int(txt[3])
                stats['SlowFails'] = int((txt[9].split(")"))[0])
            elif (("Fast" in txt) and ("steps" in txt)):
                stats['FastSteps'] = int(txt[3])
                stats['FastFails'] = int((txt[9].split(")"))[0])
            elif ("Relative" in txt):
                stats['Accuracy'] = float(txt[3])
            elif ("RHS" in txt):
                stats['FfEvals'] = int(txt[11])
                stats['FseEvals'] = int((txt[5].split(","))[0])
                stats['FsiEvals'] = int((txt[8].split(","))[0])
    return stats


#####################
# testing setup

# Flags to enable/disable categories of tests
DoKPR = True
DoBrusselator = True

# Lists of MRI methods/orders, controllers, and tolerances
MRIMethods = [["ARKODE_MRI_GARK_RALSTON2", 2], ["ARKODE_MRI_GARK_ERK22a", 2], ["ARKODE_MRI_GARK_ERK22b", 2],
              ["ARKODE_MERK21", 2], ["ARKODE_MRI_GARK_IRK21a", 2], ["ARKODE_IMEX_MRI_SR21", 2],
              ["ARKODE_MRI_GARK_ERK33a", 3], ["ARKODE_MERK32", 3], ["ARKODE_MRI_GARK_ESDIRK34a", 3],
              ["ARKODE_IMEX_MRI_SR32", 3],
              ["ARKODE_MRI_GARK_ERK45a", 4], ["ARKODE_MERK43", 4], ["ARKODE_MRI_GARK_ESDIRK46a", 4],
              ["ARKODE_IMEX_MRI_SR43", 4], ["ARKODE_MERK54", 5]]
DControls = ['MRIDec-I', 'MRIDec-H0211', 'MRIDec-H0321', 'MRIDec-H211', 'MRIDec-H312']
HTControls = ['MRIHTol-I', 'MRIHTol-H0211', 'MRIHTol-H0321', 'MRIHTol-H211', 'MRIHTol-H312']
HhControls = ['MRICC', 'MRILL', 'MRIPI', 'MRIPID']
RTols = [1.e-3, 1.e-4, 1.e-5, 1.e-6, 1.e-7]
atol = 1.e-11

# Parameter arrays to iterate over
Omegas = [50.0, 500.0]   # KPR
es = 5.0                 # KPR fast->slow coupling parameter
ef = 5.0                 # KPR slow->fast coupling parameter
Eps = [1.e-4, 1.e-5]     # Brusselator

#####################
# KPR tests
if (DoKPR):

    # set executable name
    Executable = "./bin/ark_test_kpr_mriadapt"
    HhExecutable = "./bin/ark_test_kpr_mriadapt_hh"

    # filename to hold run statistics
    fname = "kpr_mriadapt_results"

    # run first set of tests and collect results
    KPRStats = []
    for omega in Omegas:
        for rtol in RTols:
            for method in MRIMethods:
                for control in DControls:
                    KPRStats.append(runtest_kpr(Executable, es, ef, omega, atol, rtol, method[0], method[1], control))
                for control in HTControls:
                    KPRStats.append(runtest_kpr(Executable, es, ef, omega, atol, rtol, method[0], method[1], control))
                for control in HhControls:
                    KPRStats.append(runtest_kpr(HhExecutable, es, ef, omega, atol, rtol, method[0], method[1], control))

    KPRDf = pd.DataFrame.from_records(KPRStats)
    print("KPRDf object:")
    print(KPRDf)
    print("Saving as Excel")
    KPRDf.to_excel(fname + '.xlsx', index=False)

#####################
# Brusselator tests
if (DoBrusselator):

    # set executable name
    Executable = "./bin/ark_test_brusselator_mriadapt"
    HhExecutable = "./bin/ark_test_brusselator_mriadapt_hh"

    # filename to hold run statistics
    fname = "brusselator_mriadapt_results"

    # run first set of tests and collect results
    BrusselatorStats = []
    for ep in Eps:
        for rtol in RTols:
            for method in MRIMethods:
                for control in DControls:
                    BrusselatorStats.append(runtest_brusselator(Executable, ep, atol, rtol, method[0], method[1], control))
                for control in HTControls:
                    BrusselatorStats.append(runtest_brusselator(Executable, ep, atol, rtol, method[0], method[1], control))
                for control in HhControls:
                    BrusselatorStats.append(runtest_brusselator(HhExecutable, ep, atol, rtol, method[0], method[1], control))

    BrusselatorDf = pd.DataFrame.from_records(BrusselatorStats)
    print("BrusselatorDf object:")
    print(BrusselatorDf)
    print("Saving as Excel")
    BrusselatorDf.to_excel(fname + '.xlsx', index=False)
