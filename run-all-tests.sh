#!/bin/bash
#
# This script runs all the test scripts.  Results for each test are stored separately on disk, and may be plotted by running the make-all-plots.sh script.

# run slow error tests
python3 run_slowerror_tests.py

# run accumulated error tests
python3 run_accumerror_tests.py

# run main MRI adaptivity tests
python3 run_mriadapt_tests.py

# run nested MRI adaptivity tests
python3 run_nested_kpr_tests.py

# run adaptivity stepsize comparison tests
python3 run_adaptivity_comparison.py

