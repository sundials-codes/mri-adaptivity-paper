#!/usr/bin/env python3
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Programmer(s): Sylvia Amihere @ SMU
# ------------------------------------------------------------------------------------------------------------------------------------------------
# SUNDIALS Copyright Start
# Copyright (c) 2002-2024, Lawrence Livermore National Security
# and Southern Methodist University.
# All rights reserved.
#
# See the top-level LICENSE and NOTICE files for details.
#
# SPDX-License-Identifier: BSD-3-Clause
# SUNDIALS Copyright End
# --------------------------------------------------------------------------------------------------------------------------------------------------
# README
#
# This script calculates the z-scores for all MRI methods of a specified order and controller (excluding H-h controllers), 
# across both fast and slow time scales. The calculations are performed independently of any specific test problems.
#
# Output:
#        - Results are saved in an Excel file named using the format: "metricO<methodOrder>.xlsx".
#        - Each Excel file contains separate worksheets, one for each controller, with z-scores of all MRI methods 
#          of the given order.
#        - The average z-score of each MRI method across all controllers is computed and saved in separate text files.
# ---------------------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np

# --------------------------------- z-score ----------------------------------------------
# * Determines the number of standard deviations (sd) away from the mean. 
# * 1.0 = 1sd away from mean
# * 2.0 = 2sd away from the mean
# * 3.0 = 3sd away from mean
zscore_threshold = 1.0

status      = ["best", "worse"] # Classification of Methods / Controllers 
controller  = ["MRIHTol-I", "MRIHTol-H0321", "MRIHTol-H0211", "MRIHTol-H211", "MRIHTol-H312", "MRIDec-I", "MRIDec-H0321", "MRIDec-H0211", "MRIDec-H211", "MRIDec-H312"]
order       = {"Order2":[2], "Order3":[3], "Order4&5":[4,5]}
metric      = {"fast", "slow"}


def fixedCtrl_tests(df, metric, order, controller, status, zscore_threshold):
    
    # filter the data you want
    data = df[(df["order"].isin(order)) & (df["metric"] == metric) &
             (df["Controller"] == controller)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]
    
    #calculate the mean and standard deviation
    allAvg = data["AvgRank"].mean()
    allSD  = data["AvgRank"].std()

    #calculate the mean of each method across all controllers
    methodAvg = data.groupby("MRIMethod")["AvgRank"].mean()

    #calcualte the z-score of each method (it will the same across all controllers)
    data["zScore"] = data["MRIMethod"].map(methodAvg)
    data["zScore"] = (data["zScore"] - allAvg)/allSD

    # group the methods based on performance
    conditions     = [ data["zScore"] < -zscore_threshold,data["zScore"] > zscore_threshold]
    data["status"] = np.select(conditions, status, default="intermediate")

    return data

#run test
df = pd.read_excel("rank_stats.xlsx")
for mt in metric:
    for ord_key, ord_val in order.items():
            # excel file containing the results for all methods, for a particular test problem, metric and controller
            fileName  = f"{mt}{ord_key[0]}{ord_key[5:]}.xlsx"

            # worksheets in the excel file corresponding to a particular controller 
            with pd.ExcelWriter(fileName) as writer:
                for ctrl in controller:
                    data = fixedCtrl_tests(df, mt, ord_val, ctrl, status, zscore_threshold)
                    sheetName = f"{mt}{ord_key[0]}{ord_key[5:]}_{ctrl}"
                    data.to_excel(writer, sheet_name=sheetName, index=False)

            # compute the average z-score of each MRI method across all controllers or across each worksheet
            xls = pd.ExcelFile(fileName)
            sheetNames = xls.sheet_names

            MRI_methods = {"Order2":["ARKODE_MRI_GARK_ERK22b", "ARKODE_MRI_GARK_IRK21a", "ARKODE_MRI_GARK_RALSTON2", "ARKODE_MRI_GARK_ERK22a", "ARKODE_MERK21", "ARKODE_IMEX_MRI_SR21"],
                           "Order3":["ARKODE_MRI_GARK_ERK33a", "ARKODE_MRI_GARK_ESDIRK34a", "ARKODE_MERK32", "ARKODE_IMEX_MRI_SR32"],
                           "Order4&5":["ARKODE_MRI_GARK_ERK45a", "ARKODE_MERK43", "ARKODE_MERK54", "ARKODE_IMEX_MRI_SR43", "ARKODE_MRI_GARK_ESDIRK46a"]}[ord_key]
            
            # create empty lists to store the z-scores of each MRI method 
            method_zscores = {method: [] for method in MRI_methods}

            for sheet in sheetNames:
                df_sheet = pd.read_excel(fileName, sheet_name=sheet)
                for method in MRI_methods:
                    # Filter rows of a worksheet for a particular MRI method 
                    zScore = df_sheet[df_sheet["MRIMethod"] == method]["zScore"].iloc[0] # since the zscore values are the same just pick one
                    method_zscores[method].append(zScore)
            
            # compute the average zscores
            textFileName = f"AvgZscores_{mt}{ord_key[0]}{ord_key[5:]}.txt"
            with open(textFileName, "w") as file:
                file.write(f"********************************************************************************************** \n")
                file.write(f"Below are the average z-scores for all the {ord_key} methods across all controllers for the {mt} time scale. \n")
                file.write(f"********************************************************************************************** \n\n")
                file.write(f"{'Method':50} | Average z-score\n")
                file.write(f"{'-'*75}\n")
                for method in MRI_methods:
                    zScoreList = method_zscores[method]
                    avgZscore = sum(zScoreList)/len(zScoreList)
                    file.write(f"{method:50} | {avgZscore:.5f}\n")



