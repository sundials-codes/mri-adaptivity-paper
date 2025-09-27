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
# --------------------------------------------------------------------------------------------------------------------------
# README
#
# This script calculates the z-scores for all controllers (excluding H-h controllers) 
# for the fast and slow time scales.
#
# Output:
#        - Results are saved in an Excel file named: "All_controllers.xlsx"
#        - The Excel file contains separate worksheets for each time scale, with each worksheet 
#          containing the z-scores of all controllers.
#        - The average z-score for each controller (across both time scales) is computed and 
#          saved in the text file: "AvgZscores_AllControllers_"timeScale".txt". So if the fast
#          the text file will be "AvgZscores_AllControllers_fast.txt"
# --------------------------------------------------------------------------------------------------------------------------


import pandas as pd
import numpy as np

# --------------------------------- z-score ----------------------------------------------
# * Determines the number of standard deviations (sd) away from the mean. 
# * 1.0 = 1sd away from mean
# * 2.0 = 2sd away from the mean
# * 3.0 = 3sd away from mean
zscore_threshold = 1.0

status         = ["best", "worse"] # Classification of Methods / Controllers 
# params         = {"Brusselator":[0.0001, 0.00001], "KPR":[50,500]}
ctrl_to_remove = ['MRIPI', 'MRIPID', 'MRICC', 'MRILL'] #Remove the H-h controllers
metric      = {"fast", "slow"}

def allCtrl_tests(df, metric, ctrl_to_remove, status, zscore_threshold):
    
    # filter the data you want
    data = df[(df["metric"] == metric) & (~df['Controller'].isin(ctrl_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]
    
    #calculate the mean and standard deviation
    allAvg = data["AvgRank"].mean()
    allSD  = data["AvgRank"].std()

    #calculate the mean of each controller
    ctrlAvg = data.groupby("Controller")["AvgRank"].mean()

    #calculate the z-score of each controller (it will be the same across all methods)
    data["zScore"] = data["Controller"].map(ctrlAvg)
    data["zScore"] = (data["zScore"] - allAvg)/allSD

    # group the methods based on performance
    conditions     = [ data["zScore"] < -zscore_threshold,data["zScore"] > zscore_threshold]
    data["status"] = np.select(conditions, status, default="intermediate")

    return data

#run test
df = pd.read_excel("rank_stats.xlsx")
   
# excel file containing z-scores for all controllers across all methods for each test problem
fileName  = f"All_controllers.xlsx" 
            
# worksheets in the excel file corresponding to a particular test problem 
with pd.ExcelWriter(fileName) as writer:
    for mt in metric:
        data = allCtrl_tests(df, mt, ctrl_to_remove, status, zscore_threshold)
        sheetName = f"{mt}"
        data.to_excel(writer, sheet_name=sheetName, index=False)

for mt in metric:
    controllers = ["MRIHTol-I", "MRIDec-I", "MRIHTol-H0321", "MRIDec-H0321", "MRIHTol-H0211", "MRIDec-H0211", "MRIHTol-H211", "MRIDec-H211", "MRIHTol-H312",   "MRIDec-H312"]
    ctrl_zscores = {ctrl: [] for ctrl in controllers} #an empty list to store zscores for all controllers for a particular time scale
    sheetName = f"{mt}"
    df_sheet = pd.read_excel(fileName, sheet_name=sheetName)

    for ctrl in controllers:
        # Filter rows of a worksheet for a particular controller
        zScore = df_sheet[df_sheet["Controller"] == ctrl]["zScore"].iloc[0] # since the zscore values are the same just pick one
        ctrl_zscores[ctrl].append(zScore)
            
    textFileName = f"AvgZscores_AllControllers_{mt}.txt"
    with open(textFileName, "w") as file:
        file.write(f"********************************************************************************************** \n")
        file.write(f"Average z-scores for the various controllers aggregated across the stiff Brusselator and KPR test problems at the {mt} scale. \n")
        file.write(f"********************************************************************************************** \n\n")
        file.write(f"{'Controller':50} | Average z-score\n")
        file.write(f"{'-'*75}\n")
        for ctrl in controllers:
            zScoreList = ctrl_zscores[ctrl]
            avgZscore = sum(zScoreList)/len(zScoreList)
            file.write(f"{ctrl:50} | {avgZscore:.14f}\n")

