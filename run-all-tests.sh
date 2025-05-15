#!/bin/bash
#
# This script runs all the test scripts.  Results for each test are stored separately on disk, and may be plotted by running the make-all-plots.sh script.

# run slow error tests
python run_slowerror_tests.py

# run accumulated error tests
python run_accumerror_tests.py

# run main MRI adaptivity tests
python run_mriadapt_tests.py

# run nested MRI adaptivity tests
python run_nested_kpr_tests.py

# run adaptivity stepsize comparison tests
python run_adaptivity_comparison.py

