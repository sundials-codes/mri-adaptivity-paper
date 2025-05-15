#!/bin/bash
#
# This script generates plots of all test results.  These results should already be stored on disk, from running the companion run-all-test.sh script.

# plot slow error test results
python plot_slowerror.py

# plot accumulated error results
python plot_accumerror.py

## plot main MRI adaptivity results
#python plot_mriadapt.py

# plot adaptivity stepsize comparisons
python plot_adaptivity_comparison.py

