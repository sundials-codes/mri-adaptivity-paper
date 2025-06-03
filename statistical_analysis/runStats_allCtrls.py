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
# for the stiff Brusselator and KPR test problems.
#
# Output:
#        - Results are saved in an Excel file named: "All_controllers.xlsx"
#        - The Excel file contains separate worksheets for each test problem, with each worksheet 
#          containing the z-scores of all controllers.
#        - The average z-score for each controller (across both test problems) is computed and 
#          saved in the text file: "AvgZscores_AllControllers.txt"
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
params         = {"Brusselator":[0.0001, 0.00001], "KPR":[50,500]}
ctrl_to_remove = ['MRIPI', 'MRIPID', 'MRICC', 'MRILL'] #Remove the H-h controllers

def allCtrl_tests(df, params, ctrl_to_remove, status, zscore_threshold):
    
    # filter the data you want
    data = df[(df["Param"].isin(params)) & (~df['Controller'].isin(ctrl_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]
    
    #calculate the mean and standard deviation
    allAvg = data["AvgRank"].mean()
    allSD  = data["AvgRank"].std()

    #calculate the mean of each controller
    ctrlAvg = data.groupby("Controller")["AvgRank"].mean()

    #calcualte the z-score of each method (it will the same across all controllers)
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
    for prb_key, prb_val in params.items():
        data = allCtrl_tests(df, prb_val, ctrl_to_remove, status, zscore_threshold)
        sheetName = f"{prb_key}"
        data.to_excel(writer, sheet_name=sheetName, index=False)

# compute the average z-score of controller across each worksheet
xls = pd.ExcelFile(fileName)
sheetNames = xls.sheet_names

controllers = ["MRIHTol-I", "MRIHTol-H0321", "MRIHTol-H0211", "MRIHTol-H211", "MRIHTol-H312", "MRIDec-I", "MRIDec-H0321", "MRIDec-H0211", "MRIDec-H211", "MRIDec-H312"]
        
# create empty lists to store the z-scores of each controller  
ctrl_zscores = {ctrl: [] for ctrl in controllers}

for sheet in sheetNames:
    df_sheet = pd.read_excel(fileName, sheet_name=sheet)
    for ctrl in controllers:
        # Filter rows of a worksheet for a particular controller
        zScore = df_sheet[df_sheet["Controller"] == ctrl]["zScore"].iloc[0] # since the zscore values are the same just pick one
        ctrl_zscores[ctrl].append(zScore)
    
# compute the average zscores
textFileName = f"AvgZscores_AllControllers.txt"
with open(textFileName, "w") as file:
        file.write(f"********************************************************************************************** \n")
        file.write(f"Below are the average z-scores for the various controllers aggregated across the stiff Brusselator and KPR test problems. \n")
        file.write(f"********************************************************************************************** \n\n")
        file.write(f"{'Controller':50} | Average z-score\n")
        file.write(f"{'-'*75}\n")
        for ctrl in controllers:
            zScoreList = ctrl_zscores[ctrl]
            avgZscore = sum(zScoreList)/len(zScoreList)
            file.write(f"{ctrl:50} | {avgZscore:.5f}\n")



