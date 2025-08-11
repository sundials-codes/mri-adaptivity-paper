#!/bin/bash
#
# This script generates excel files and text files for all tests (stiff Brusselator and KPR), controllers and MRI methods.

echo -e "Running repeated measures ANOVA for all MRI methods of a specific order\n"
python3 runStats_repeatedM_ANOVA.py

echo -e "Running One-Way ANOVA for all controllers\n"
python3 runStats_oneWayANOVA_ctrl.py

echo -e "Running statistical analysis for Brusselator and KPR, for all MRI methods with a fixed controller \n"
python3 runStats_fixedCtrl_tests.py

echo -e "Running statistical analysis for Brusselator and KPR, for all controllers with a fixed MRI method \n"
python3 runStats_fixedMethod_tests.py

echo -e "Running statistical analysis for Brusselator and KPR, for all controllers \n"
python3 runStats_allCtrls.py

echo -e "Running statistical analysis for Brusselator and KPR, for all HTol, Decoupled and Hh controllers \n"
python3 runStats_hTol_dec_ctrl.py

echo -e "Run tests completed!\n"
