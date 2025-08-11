#!/bin/bash
#
# This script generates plots of all test results.  These results should already be stored on disk, from running the companion run-all-test.sh script.

# plot accumulated error results
python3 plot_accumerror.py

## plot main MRI adaptivity results
python3 plot_mriadapt.py

# plot adaptivity stepsize comparisons
python3 plot_adaptivity_comparison.py

