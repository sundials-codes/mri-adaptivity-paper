#!/bin/bash
#
# This script generates excel files for all tests (stiff Brusselator and KPR) and all controllers with a fixed MRI method. 
# These results are stored in the excel files with name: allOrder"order-of-MRI-method"_controllers.xlsx.

# run repeated measures ANOVA to show that there is a statistically significant difference between methods of a particular order
echo -e "Running statistical analysis for all methods\n"
python  run_ANOVA_all_methods.py

# run all methods 
python run_all_methods.py

echo -e "Running statistical analysis for all controllers\n"
# run a one-way ANOVA to show that there is a statistically significant difference between controllers
python run_oneWayANOVA_ctrl.py

# run all controllers 
python run_all_controllers.py


