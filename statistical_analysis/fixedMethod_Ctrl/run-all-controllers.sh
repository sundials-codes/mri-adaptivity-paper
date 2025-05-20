#!/bin/bash
#
# This script generates excel files for all tests (stiff Brusselator and KPR) and all controllers with a fixed MRI method. 
# These results are stored in the excel files with name: allOrder"order-of-MRI-method"_controllers.xlsx.

echo -e "Running statistical analysis for Brusselator and KPR, for all 2nd order methods across all controllers \n"
# run all controllers for a fixed 2nd order method
python run_ctrlBruss_Ord2.py
python run_ctrlKPR_Ord2.py

echo -e "Running statistical analysis for Brusselator and KPR, for all 3rd order methods across all controllers \n"
# run all controllers for a fixed 3rd order method
python run_ctrlBruss_Ord3.py
python run_ctrlKPR_Ord3.py

echo -e "Running statistical analysis for Brusselator and KPR, for all 4th and 5th order methods across all controllers \n"
# run all controllers for a fixed 4th and 5th order methods
python run_ctrlBruss_Ord45.py
python run_ctrlKPR_Ord45.py

echo -e "Run tests completed!\n"