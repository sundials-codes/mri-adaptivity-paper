#!/bin/bash
#
# This script generates excel files for all tests (stiff Brusselator and KPR) and all controllers with a fixed MRI method. 
# These results are stored in the excel files with name: allOrder"order-of-MRI-method"_controllers.xlsx.

# run all controllers for a fixed 2nd order method
python run_all_Ord2.py

# run all controllers for a fixed 3rd order method
python run_all_Ord3.py

# run all controllers for a fixed 4th and 5th order methods
python run_all_Ord45.py
