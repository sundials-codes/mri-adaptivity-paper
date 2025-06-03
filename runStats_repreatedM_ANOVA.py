#!/usr/bin/env python3
# --------------------------------------------------------------------------------------------
# Programmer(s): Sylvia Amihere @ SMU
# --------------------------------------------------------------------------------------------
# SUNDIALS Copyright Start
# Copyright (c) 2002-2024, Lawrence Livermore National Security
# and Southern Methodist University.
# All rights reserved.
#
# See the top-level LICENSE and NOTICE files for details.
#
# SPDX-License-Identifier: BSD-3-Clause
# SUNDIALS Copyright End
# ---------------------------------------------------------------------------------------------
# README
#
# This script performs a Repeated Measures ANOVA to determine whether there are statistically 
# significant differences between MRI methods of a specific order, evaluated across all controllers 
# and test problems, for both fast and slow time scales.
# ----------------------------------------------------------------------------------------------

# Import library 
import numpy as np 
import pandas as pd 
from statsmodels.stats.anova import AnovaRM 


ctrl_to_remove = ['MRIPI', 'MRIPID', 'MRICC', 'MRILL'] #Remove the H-h controllers
metric         = {"fast", "slow"}
order          = {"Order2":[2], "Order3":[3], "Order4&5":[4,5]}

def repeatedM_ANOVA_methods(df, ctrl_to_remove, metric, order):
    data = df[(df["order"].isin(order))&(df["metric"] == metric)& ~df['Controller'].isin(ctrl_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]
    data_agg = data.groupby(['MRIMethod', 'Controller'], as_index=False)['AvgRank'].mean()
    anova_results = AnovaRM(data_agg, depvar='AvgRank', subject='Controller', within=['MRIMethod']).fit()
    return anova_results

#run test
df = pd.read_excel("rank_stats.xlsx") #Load your excel file 

for mt in metric:
    for ord_key, ord_val in order.items():
        anova_results = repeatedM_ANOVA_methods(df, ctrl_to_remove, mt, ord_val)
        prt_statement = f"**** {mt} {ord_key} Methods ****\n"
        print(prt_statement, anova_results)
