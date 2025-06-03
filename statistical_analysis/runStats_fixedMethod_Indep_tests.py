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
# This script computes z-scores for all controllers (except H-h controllers) for a given MRI method of a specific order, 
# evaluated across both fast and slow time scales. The calculations are performed independently of any specific test problems.
#
# Output:
#        - Results are saved in an Excel file named using the format: "O<methodOrder>_controllers.xlsx".
#        - Each Excel file contains separate worksheets, one for each MRI method of the specified order, with z-scores of all controllers.
#        - The average z-score of each controller across all MRI methods of teh specified order is computed and saved in separate text files.
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
ctrl_to_remove = ['MRIPI', 'MRIPID', 'MRICC', 'MRILL'] #Remove the H-h controllers
MRIMethod      = {"Order2":["ARKODE_MRI_GARK_ERK22b", "ARKODE_MRI_GARK_IRK21a", "ARKODE_MRI_GARK_RALSTON2", "ARKODE_MRI_GARK_ERK22a", "ARKODE_MERK21", "ARKODE_IMEX_MRI_SR21"],
                  "Order3":["ARKODE_MRI_GARK_ERK33a", "ARKODE_MRI_GARK_ESDIRK34a", "ARKODE_MERK32", "ARKODE_IMEX_MRI_SR32"],
                  "Order4&5":["ARKODE_MRI_GARK_ERK45a", "ARKODE_MERK43", "ARKODE_MERK54", "ARKODE_IMEX_MRI_SR43", "ARKODE_MRI_GARK_ESDIRK46a"]}

def fixedCtrl_tests(df, method_ord, ctrl_to_remove, status, zscore_threshold):
    
    # filter the data you want
    data = df[(df["MRIMethod"]==method_ord) & (~df['Controller'].isin(ctrl_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]
    
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
for mriM_key, mriM_val in MRIMethod.items():
        
        # excel file containing the results for all controllers, for a particular test problem, metric and method
        fileName  = f"{mriM_key[0]}{mriM_key[5:]}_controllers.xlsx"
             
        # worksheets in the excel file corresponding to a particular method 
        with pd.ExcelWriter(fileName) as writer:
            for mriM_part in mriM_val:
                data = fixedCtrl_tests(df, mriM_part, ctrl_to_remove, status, zscore_threshold)
                sheetName = f"_{mriM_key[0]}{mriM_key[5:]}_{mriM_part.split('_')[-1]}"
                data.to_excel(writer, sheet_name=sheetName, index=False)

        # compute the average z-score of each controller across the worksheets
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
        textFileName = f"AvgZscores_{mriM_key[0]}{mriM_key[5:]}_controllers.txt"
        with open(textFileName, "w") as file:
                file.write(f"********************************************************************************************** \n")
                file.write(f"Below are the average z-scores for the various controllers and for {mriM_key} methods. \n")
                file.write(f"********************************************************************************************** \n\n")
                file.write(f"{'Controller':50} | Average z-score\n")
                file.write(f"{'-'*75}\n")
                for ctrl in controllers:
                    zScoreList = ctrl_zscores[ctrl]
                    avgZscore = sum(zScoreList)/len(zScoreList)
                    file.write(f"{ctrl:50} | {avgZscore:.5f}\n")



