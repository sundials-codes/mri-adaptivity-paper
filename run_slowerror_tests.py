#!/usr/bin/env python3
#------------------------------------------------------------
# Programmer(s):  Daniel R. Reynolds @ SMU
#------------------------------------------------------------
# Copyright (c) 2024, Southern Methodist University.
# All rights reserved.
# For details, see the LICENSE file.
#------------------------------------------------------------

# imports
import subprocess
import shlex

# MRI methods to test
MethodsLo = ["ARKODE_MRI_GARK_RALSTON2", "ARKODE_MRI_GARK_ERK22a", "ARKODE_MRI_GARK_ERK22b",
             "ARKODE_MERK21", "ARKODE_MRI_GARK_IRK21a", "ARKODE_IMEX_MRI_SR21"]
MethodsHi = ["ARKODE_MRI_GARK_ERK33a", "ARKODE_MERK32", "ARKODE_MRI_GARK_ESDIRK34a",
             "ARKODE_IMEX_MRI_SR32", "ARKODE_MRI_GARK_ERK45a", "ARKODE_MERK43",
             "ARKODE_MRI_GARK_ESDIRK46a", "ARKODE_IMEX_MRI_SR43", "ARKODE_MERK54"]


#####################
# Brusselator tests

# set executable name
executable = "./bin/ark_test_slowerror_brusselator"

# filenames to hold run output
fname_lo = "slowerror_brusselator_results_lo.txt"
fname_hi = "slowerror_brusselator_results_hi.txt"

# common testing parameters
test = 2
Npart = 20
ep = 0.0004

# open results file for low order methods, and run each test (appending results to fname_lo)
with open(fname_lo, "w") as outfile:
    for method in MethodsLo:
        runcommand = "%s %s %i %e %i" % (executable, method, Npart, ep, test)
        subprocess.run(shlex.split(runcommand), stdout=outfile)
        outfile.flush()

# open results file for high order methods, and run each test (appending results to fname_hi)
with open(fname_hi, "w") as outfile:
    for method in MethodsHi:
        runcommand = "%s %s %i %e %i" % (executable, method, Npart, ep, test)
        subprocess.run(shlex.split(runcommand), stdout=outfile)
        outfile.flush()


#####################
# KPR tests

# set executable name
executable = "./bin/ark_test_slowerror_kpr"

# filenames to hold run output
fname_lo = "slowerror_kpr_results_lo.txt"
fname_hi = "slowerror_kpr_results_hi.txt"

# common testing parameters
Npart = 20
G = -10.0
e = 0.1
omega = 5.0

# open results file for low order methods, and run each test (appending results to fname_lo)
with open(fname_lo, "w") as outfile:
    for method in MethodsLo:
        runcommand = "%s %s %i %e %e %e" % (executable, method, Npart, G, e, omega)
        subprocess.run(shlex.split(runcommand), stdout=outfile)
        outfile.flush()

# open results file for high order methods, and run each test (appending results to fname_hi)
with open(fname_hi, "w") as outfile:
    for method in MethodsHi:
        runcommand = "%s %s %i %e %e %e" % (executable, method, Npart, G, e, omega)
        subprocess.run(shlex.split(runcommand), stdout=outfile)
        outfile.flush()


