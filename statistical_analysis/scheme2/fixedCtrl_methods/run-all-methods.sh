#!/bin/bash
#
# This script generates excel files for all tests (stiff Brusselator and KPR) and all MRI methods with a fixed controller. 
# These results are stored in the excel files with name: all"test-Type"_"metric"Order"order-of-MRI-method".xlsx.

# run all fast 2nd order methods for a fixed controller, for the stiff Brusselator test 
python run_allBruss_fastOrd2.py

# run all fast 3rd order methods for a fixed controller, for the stiff Brusselator test 
python run_allBruss_fastOrd3.py

# run all fast 4th and 5th order methods for a fixed controller, for the stiff Brusselator test 
python run_allBruss_fastOrd45.py

# run all slow 2nd order methods for a fixed controller, for the stiff Brusselator test 
python run_allBruss_slowOrd2.py

# run all slow 3rd order methods for a fixed controller, for the stiff Brusselator test 
python run_allBruss_slowOrd3.py

# run all slow 4th and 5th order methods for a fixed controller, for the stiff Brusselator test 
python run_allBruss_slowOrd45.py


# run all fast 2nd order methods for a fixed controller, for the KPR test 
python run_allKPR_fastOrd2.py

# run all fast 3rd order methods for a fixed controller, for the KPR test 
python run_allKPR_fastOrd3.py

# run all fast 4th and 5th order methods for a fixed controller, for the KPR test 
python run_allKPR_fastOrd45.py

# run all slow 2nd order methods for a fixed controller, for the KPR test 
python run_allKPR_slowOrd2.py

# run all slow 3rd order methods for a fixed controller, for the KPR test 
python run_allKPR_slowOrd3.py

# run all slow 4th and 5th order methods for a fixed controller, for the KPR test 
python run_allKPR_slowOrd45.py
