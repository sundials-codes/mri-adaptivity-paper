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
# --------------------------------------------------------------------------------------------------------------------------
# This script calculates the z-scores for all HTol and Decoupled controllers (except H-h controllers), across all metric, test problems and methods.
# The results are saved in an an excel file labelled as "htol_dec_controllers.xlsx"
# The z-scores are the same for all HTol controllers.
# Likewise, the z-scores are the same for all decoupled controllers.
# The z-score of each controller type is saved to the text file "zScores_HTol_Dec.txt".
# --------------------------------------------------------------------------------------------------------------------------


import pandas as pd
import numpy as np

ctrl_type      = ["MRIHTol", "MRIDec"]
ctrl_to_remove = ['MRIPI', 'MRIPID', 'MRICC', 'MRILL'] #Remove the H-h controllers

def allCtrl_tests(df,ctrl_type, ctrl_to_remove):
    
    # filter the data you want
    data = df[(~df['Controller'].isin(ctrl_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]
    
    #calculate the overall mean and standard deviation
    allAvg = data["AvgRank"].mean()
    allSD  = data["AvgRank"].std()

    for ctrl_prefix in ctrl_type:
        #calculate the mean of all controllers with a particular prefix
        ctrl_subset = data[data["Controller"].str.startswith(ctrl_prefix)]
        prefix_avg = ctrl_subset["AvgRank"].mean()

        zScore = (prefix_avg - allAvg)/allSD

        data.loc[ctrl_subset.index, "zScore"] = zScore

    return data

#run test
df = pd.read_excel("rank_stats.xlsx")
final_data = allCtrl_tests(df,ctrl_type, ctrl_to_remove)

# excel file containing the results for all controllers, across all prolems types, methods and metric
final_data.to_excel("htol_dec_controllers.xlsx", index=False)

# output the zscore for all HTol and Decoupled controllers to a text file
select_data = final_data[(final_data["Controller"] == "MRIHTol-I")]
HTol_zScore = select_data["zScore"].iloc[0] #the zscores are the same for all HTol controllers so just choose one

select_data = final_data[(final_data["Controller"] == "MRIDec-I")]
Dec_zScore = select_data["zScore"].iloc[0] #the zscores are the same for all Decoupled controllers so just choose one

with open("zScores_HTol_Dec.txt", "w") as file:
    file.write(f"The zscore for the MRIHTol controllers is: {HTol_zScore}\n\n")
    file.write(f"The zscore for the MRIDec controllers is: {Dec_zScore}\n\n")



