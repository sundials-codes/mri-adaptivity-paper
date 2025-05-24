#!/usr/bin/env python3
# ------------------------------------------------------------------------------
# Programmer(s): Sylvia Amihere @ SMU
# ------------------------------------------------------------------------------
# SUNDIALS Copyright Start
# Copyright (c) 2002-2024, Lawrence Livermore National Security
# and Southern Methodist University.
# All rights reserved.
#
# See the top-level LICENSE and NOTICE files for details.
#
# SPDX-License-Identifier: BSD-3-Clause
# SUNDIALS Copyright End
# ------------------------------------------------------------------------------
# This script returns the results of a One-Way ANOVA indicating whether there is 
# a statistically significant difference between the controllers across all methods 
# and test problems.
# ------------------------------------------------------------------------------

# Import library 
import numpy as np 
import pandas as pd 
from scipy import stats
from statsmodels.stats.anova import AnovaRM 


# ------------------------------------------ Load your excel file --------------------------------------------
df = pd.read_excel("rank_stats.xlsx")

# --------------------------- Contains the list of AvgRank values for each controller ------------------------
controller_groups = []

# -------------------- Loop through each controller group and extract the AvgRank values ---------------------
for name, group in df.groupby("Controller"):
    controller_groups.append(group["AvgRank"].values)

# -------------------------- Perform the one-way ANOVA on the controller groups ------------------------------
anova_results = stats.f_oneway(*controller_groups)

# ----------------------------------------- Print the results ------------------------------------------------ 
print("One-Way ANOVA Results:")
print( anova_results)