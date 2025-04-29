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

#####################
# Brusselator tests

# set executable name
executable = "./bin/ark_test_accumerror_brusselator"

# filename to hold run output
fname = "accumerror_brusselator_results.txt"

# common testing parameters
test = 2
Npart = 20
ep = 0.0004
method = 1

# orders of accuracy to test (positive are adaptive, negative are fixed-step)
Orders = [2, 3, 4, 5, 6, -2, -3, -4, -5, -6]

# open results file
with open(fname, "w") as outfile:
    subprocess.run(["ls"], stdout=outfile)

    # run each test, appending results to fname
    for ord in Orders:
        runcommand = "%s %i %i %i %e %i" % (executable, Npart, ord, method, ep, test)
        subprocess.run(shlex.split(runcommand), stdout=outfile)
        outfile.flush()


#####################
# KPR tests

# set executable name
executable = "./bin/ark_test_accumerror_kpr"

# filename to hold run output
fname = "accumerror_kpr_results.txt"

# common testing parameters
Npart = 20
G = -10.0
e = 0.1
omega = 5.0

# orders of accuracy to test (positive are adaptive, negative are fixed-step)
Orders = [2, 3, 4, 5, 6, -2, -3, -4, -5, -6]

# open results file
with open(fname, "w") as outfile:
    subprocess.run(["ls"], stdout=outfile)

    # run each test, appending results to fname
    for ord in Orders:
        runcommand = "%s %i %i %i %e %e %e" % (executable, Npart, ord, method, G, e, omega)
        subprocess.run(shlex.split(runcommand), stdout=outfile)
        outfile.flush()

