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
# README
#
# This script calculates the z-scores for all HTol and Decoupled controllers (excluding H-h controllers), 
# aggregated across all MRI methods, test problems (stiff Brusselator and KPR), and time scales (fast and slow).
#
# Output:
#        - Results are saved in an Excel file named: "htol_dec_controllers.xlsx"
#        - The z-scores are identical for all HTol controllers and likewise identical across all Decoupled controllers.
#        - The final z-scores for each controller type are also saved to a text file: "zScores_HTol_Dec.txt"
# --------------------------------------------------------------------------------------------------------------------------


import pandas as pd
import numpy as np

def ctrl_rename(df):
    data = df[["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]].copy()
    data.loc[df["Controller"].str.startswith("MRIHTol"), "ctrl_name"] = "HTol"
    data.loc[df["Controller"].str.startswith("MRIDec"), "ctrl_name"]  = "Dec"
    data.loc[df["Controller"].str.startswith("MRIPI"), "ctrl_name"]   = "Hh"
    data.loc[df["Controller"].str.startswith("MRIPID"), "ctrl_name"]  = "Hh"
    data.loc[df["Controller"].str.startswith("MRICC"), "ctrl_name"]   = "Hh"
    data.loc[df["Controller"].str.startswith("MRILL"), "ctrl_name"]   = "Hh"
    return data

df = pd.read_excel("rank_stats.xlsx")
final_data_rename = ctrl_rename(df)
final_data_rename.to_excel("rename_controllers.xlsx", index=False)


ctrl_type = ["HTol", "Dec",'Hh']
def allCtrl_tests(df,ctrl_type):
    
    # filter the data you want
    data = df[["metric", "order", "Param", "MRIMethod", "Controller", "ctrl_name", "AvgRank"]].copy()
    
    #calculate the overall mean and standard deviation
    allAvg = data["AvgRank"].mean()
    allSD  = data["AvgRank"].std()

    for ctrl_prefix in ctrl_type:
        #calculate the mean of all controllers with a particular prefix
        ctrl_subset = data[data["ctrl_name"].str.startswith(ctrl_prefix)]
        prefix_avg = ctrl_subset["AvgRank"].mean()

        zScore = (prefix_avg - allAvg)/allSD

        data.loc[ctrl_subset.index, "zScore"] = zScore

    return data

# # run test
df = pd.read_excel("rename_controllers.xlsx")
final_data = allCtrl_tests(df,ctrl_type)

# excel file containing the results for all controllers, across all prolems types, methods and metric
final_data.to_excel("htol_dec_Hh_controllers.xlsx", index=False)

# output the zscore for all HTol and Decoupled controllers to a text file
select_data = final_data[(final_data["Controller"] == "MRIHTol-I")]
HTol_zScore = select_data["zScore"].iloc[0] #the zscores are the same for all HTol controllers so just choose one

select_data = final_data[(final_data["Controller"] == "MRIDec-I")]
Dec_zScore = select_data["zScore"].iloc[0] #the zscores are the same for all Decoupled controllers so just choose one

select_data = final_data[(final_data["Controller"] == "MRIPID")]
Hh_zScore = select_data["zScore"].iloc[0] #the zscores are the same for all Decoupled controllers so just choose one

with open("zScores_HTol_Dec.txt", "w") as file:
    file.write(f"The z-score for the MRIHTol controllers is: {HTol_zScore}\n\n")
    file.write(f"The z-score for the MRIDec controllers is: {Dec_zScore}\n\n")
    file.write(f"The z-score for the Hh controllers is: {Hh_zScore}\n\n")
