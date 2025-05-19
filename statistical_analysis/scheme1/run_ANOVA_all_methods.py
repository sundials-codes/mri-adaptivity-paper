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

# Import library 
import numpy as np 
import pandas as pd 
from statsmodels.stats.anova import AnovaRM 


# --------------------------------------- Load your excel file ----------------------------------------
df = pd.read_excel("rank_stats.xlsx")

# ------------------------------------- Remove the H-h controllers --------------------------------
controllers_to_remove = ['MRIPI', 'MRIPID', 'MRICC', 'MRILL']


#############################################################################################################################################
# ----------------------------------- Select only fast methods of order 2 ----------------------------------
data_fastOrd2 = df[(df["order"] == 2) & (df["metric"] == "fast") & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ------------------------------------ Repeated Measures of ANOVA -------------------------------------
data_fastOrd2_agg = data_fastOrd2.groupby(['MRIMethod', 'Controller'], as_index=False)['AvgRank'].mean()
print("**** Fast 2nd Order Methods ****\n", AnovaRM(data_fastOrd2_agg, depvar='AvgRank', subject='Controller', within=['MRIMethod']).fit())


#############################################################################################################################################
# ----------------------------------- Select only slow methods of order 2 ----------------------------------
data_slowOrd2 = df[(df["order"] == 2) & (df["metric"] == "slow") & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ------------------------------------ Repeated Measures of ANOVA -------------------------------------
data_slowOrd2_agg = data_slowOrd2.groupby(['MRIMethod', 'Controller'], as_index=False)['AvgRank'].mean()
print("**** Slow 2nd Order Methods ****\n", AnovaRM(data_slowOrd2_agg, depvar='AvgRank', subject='Controller', within=['MRIMethod']).fit())


#############################################################################################################################################
# ----------------------------------- Select only fast methods of order 3 ----------------------------------
data_fastOrd3 = df[(df["order"] == 3) & (df["metric"] == "fast") & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ------------------------------------ Repeated Measures of ANOVA -------------------------------------
data_fastOrd3_agg = data_fastOrd3.groupby(['MRIMethod', 'Controller'], as_index=False)['AvgRank'].mean()
print("**** Fast 3rd Order Methods ****\n", AnovaRM(data_fastOrd3_agg, depvar='AvgRank', subject='Controller', within=['MRIMethod']).fit())


#############################################################################################################################################
# ----------------------------------- Select only slow methods of order 3 ----------------------------------
data_slowOrd3 = df[(df["order"] == 3) & (df["metric"] == "slow") & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ------------------------------------ Repeated Measures of ANOVA -------------------------------------
data_slowOrd3_agg = data_slowOrd3.groupby(['MRIMethod', 'Controller'], as_index=False)['AvgRank'].mean()
print("**** Slow 3rd Order Methods ****\n", AnovaRM(data_slowOrd3_agg, depvar='AvgRank', subject='Controller', within=['MRIMethod']).fit())


#############################################################################################################################################
# ----------------------------------- Select only fast methods of order 4 and 5 ----------------------------------
data_fastOrd45 = df[(df["order"].isin([4, 5])) & (df["metric"] == "fast") & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ------------------------------------ Repeated Measures of ANOVA -------------------------------------
data_fastOrd45_agg = data_fastOrd45.groupby(['MRIMethod', 'Controller'], as_index=False)['AvgRank'].mean()
print("**** Fast 4th and 5th Order Methods ****\n", AnovaRM(data_fastOrd45_agg, depvar='AvgRank', subject='Controller', within=['MRIMethod']).fit())


#############################################################################################################################################
# ----------------------------------- Select only slow methods of order 4 and 5 ----------------------------------
data_slowOrd45 = df[(df["order"].isin([4, 5])) & (df["metric"] == "slow") & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ------------------------------------ Repeated Measures of ANOVA -------------------------------------
data_slowOrd45_agg = data_slowOrd45.groupby(['MRIMethod', 'Controller'], as_index=False)['AvgRank'].mean()
print("**** Slow 4th and 5th Order Methods ****\n", AnovaRM(data_slowOrd45_agg, depvar='AvgRank', subject='Controller', within=['MRIMethod']).fit())

