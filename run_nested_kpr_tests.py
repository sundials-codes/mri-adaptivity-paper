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
        case 'MRIHTol-I':
            txt = ' --scontrol 1 --fcontrol 1'
        case 'MRIDec-I':
            txt = ' --scontrol 6 --fcontrol 1'
        case 'MRIHTol-H0211':
            txt = ' --scontrol 2 --fcontrol 2'
        case 'MRIDec-H0211':
            txt = ' --scontrol 7 --fcontrol 2'
        case 'MRIHTol-H0321':
            txt = ' --scontrol 3 --fcontrol 3'
        case 'MRIDec-H0321':
            txt = ' --scontrol 8 --fcontrol 3'
        case 'MRIHTol-H211':
            txt = ' --scontrol 4 --fcontrol 4'
        case 'MRIDec-H211':
            txt = ' --scontrol 9 --fcontrol 4'
        case 'MRIHTol-H312':
            txt = ' --scontrol 5 --fcontrol 5'
        case 'MRIDec-H312':
            txt = ' --scontrol 10 --fcontrol 5'
        case _:
            txt = ' '
    return txt

# utility routine to run a single nested KPR test, storing the run options and solver statistics
def runtest_nested_kpr(exe, e, al, be, omega, atol, rtol, mri, order, control, showcommand=False):
    stats = {'e': e, 'al': al, 'be': be, 'omega': omega, 'atol': atol, 'rtol': rtol, 'mri_method': mri, 'fast_order': order, 'control': control, 'ReturnCode': 0, 'SlowSteps': 0, 'SlowFails': 0, 'MedSteps': 0, 'MedFails': 0, 'FastSteps': 0, 'FastFails': 0, 'Accuracy': 0.0, 'FfEvals': 0, 'FmeEvals': 0, 'FmiEvals': 0, 'FseEvals': 0, 'FsiEvals': 0}
    runcommand = "%s --e %e --al %e --be %e --w %e --atol %e --rtol %e --fast_rtol %e --mri_method %s --mid_method %s --fast_order %d" % (exe, e, al, be, omega, atol, rtol, rtol, mri, mri, order) + controller(control)
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
                stats['SlowFails'] = int((txt[9].split(","))[0])
            if (("Intermediate" in txt) and ("steps" in txt)):
                stats['MedSteps'] = int(txt[3])
                stats['MedFails'] = int((txt[9].split(","))[0])
            elif (("Fast" in txt) and ("steps" in txt)):
                stats['FastSteps'] = int(txt[3])
                stats['FastFails'] = int((txt[9].split(")"))[0])
            elif ("Relative" in txt):
                stats['Accuracy'] = float(txt[3])
            elif ("RHS" in txt):
                stats['FfEvals'] = int(txt[17])
                stats['FseEvals'] = int((txt[5].split(","))[0])
                stats['FsiEvals'] = int((txt[8].split(","))[0])
                stats['FmeEvals'] = int((txt[11].split(","))[0])
                stats['FmiEvals'] = int((txt[14].split(","))[0])
    return stats


#####################
# testing setup

# Flags to enable/disable categories of tests
DoKPR = True
DoBrusselator = True

# Lists of MRI methods/orders, controllers, and tolerances to test
method = ["ARKODE_MRI_GARK_ERK22b", 2]
Controls = ['MRIHTol-I']
RTols = [1.e-2, 1.e-4, 1.e-6, 1.e-8]
atol = 1.e-11

# Nested KPR parameters
om = 50.0
e = 5.0
al = -1.0
be = 1.0

# set executable name
Executable = "./bin/ark_kpr_nestedmri"

# filename to hold run statistics
fname = "kpr_nested_results"

# run first set of tests and collect results
KPRNestedStats = []
for rtol in RTols:
    for control in Controls:
        KPRNestedStats.append(runtest_nested_kpr(Executable, e, al, be, om, atol, rtol, method[0], method[1], control))

KPRNestedDf = pd.DataFrame.from_records(KPRNestedStats)
print("KPRNestedDf object:")
print(KPRNestedDf)
print("Saving as Excel")
KPRNestedDf.to_excel(fname + '.xlsx', index=False)
