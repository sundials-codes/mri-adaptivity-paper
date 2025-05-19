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

import pandas as pd
import numpy as np

# --------------------------------- z-score ----------------------------------------------
# * Determines the number of standard deviations (sd) away from the mean. 
# * 1.0 = 1sd away from mean
# * 2.0 = 2sd away from the mean
# * 3.0 = 3sd away from mean
zscore_threshold = 1.0

# --------------------------------- Classification of Controllers ---------------------------------------
status = ["best", "worse"]

# Load your Excel file
df = pd.read_excel("rank_stats.xlsx")

# ------------------------------------- Remove the H-h controllers --------------------------------
controllers_to_remove = ['MRIPI', 'MRIPID', 'MRICC', 'MRILL']


#######################################################################################################################
# ------------------------------------- Select only all controllers ------------------------------------------------
data_Ctrl = df[~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "Controller", "MRIMethod", "AvgRank"]]

# ------------------------ Calculate the mean and standard deviation of the selected data -------------------------
allAvg_Ctrl = data_Ctrl["AvgRank"].mean()
allStD_Ctrl = data_Ctrl["AvgRank"].std()

# ----------------------------- Calculate the mean of each controller across all methods -------------------------
methodAvg_Ctrl = data_Ctrl.groupby("Controller")["AvgRank"].mean()

# -------- Calculate the z-score of each controller and store on each row corresponding to the controller ----------
data_Ctrl["Ctrl_zScore"] = data_Ctrl["Controller"].map(methodAvg_Ctrl)
data_Ctrl["Ctrl_zScore"] = (data_Ctrl["Ctrl_zScore"] - allAvg_Ctrl)/allStD_Ctrl 

# --------------------------------------- Classify each method based on z-score -------------------------------------
conditions = [
    data_Ctrl["Ctrl_zScore"] < -zscore_threshold,
    data_Ctrl["Ctrl_zScore"] > zscore_threshold
]

data_Ctrl["Ctrl_status"] = np.select(conditions, status, default="intermediate")

# ----------------------------------------- Update excel file with z-scores -------------------------------------------
data_Ctrl.to_excel("controllers_zscores.xlsx", index=False)



# #######################################################################################################################
# # ------------------------------------- Select only fast controllers ----------------------------------------------
# data_fastCtrl = df[(df["metric"] == "fast")& ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "Controller", "MRIMethod", "AvgRank"]]

# # ------------------------ Calculate the mean and standard deviation of the selected data -------------------------
# allAvg_fastCtrl = data_fastCtrl["AvgRank"].mean()
# allStD_fastCtrl = data_fastCtrl["AvgRank"].std()

# # ----------------------------- Calculate the mean of each controller across all methods -------------------------
# methodAvg_fastCtrl = data_fastCtrl.groupby("Controller")["AvgRank"].mean()

# # -------- Calculate the z-score of each controller and store on each row corresponding to the controller ----------
# data_fastCtrl["fastCtrl_zScore"] = data_fastCtrl["Controller"].map(methodAvg_fastCtrl)
# data_fastCtrl["fastCtrl_zScore"] = (data_fastCtrl["fastCtrl_zScore"] - allAvg_fastCtrl)/allStD_fastCtrl 

# # --------------------------------------- Classify each method based on z-score -------------------------------------
# conditions = [
#     data_fastCtrl["fastCtrl_zScore"] < -zscore_threshold,
#     data_fastCtrl["fastCtrl_zScore"] > zscore_threshold
# ]

# data_fastCtrl["fastCtrl_status"] = np.select(conditions, status, default="intermediate")

# # ----------------------------------------- Update excel file with z-scores -------------------------------------------
# data_fastCtrl.to_excel("fast_controllers_zscores.xlsx", index=False)



# #######################################################################################################################
# # ------------------------------------- Select only slow controllers ----------------------------------------------
# data_slowCtrl = df[(df["metric"] == "slow")& ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "Controller", "MRIMethod", "AvgRank"]]

# # ------------------------ Calculate the mean and standard deviation of the selected data -------------------------
# allAvg_slowCtrl = data_slowCtrl["AvgRank"].mean()
# allStD_slowCtrl = data_slowCtrl["AvgRank"].std()

# # ----------------------------- Calculate the mean of each controller across all methods -------------------------
# methodAvg_slowCtrl = data_slowCtrl.groupby("Controller")["AvgRank"].mean()

# # -------- Calculate the z-score of each controller and store on each row corresponding to the controller ----------
# data_slowCtrl["slowCtrl_zScore"] = data_slowCtrl["Controller"].map(methodAvg_slowCtrl)
# data_slowCtrl["slowCtrl_zScore"] = (data_slowCtrl["slowCtrl_zScore"] - allAvg_slowCtrl)/allStD_slowCtrl 

# # --------------------------------------- Classify each method based on z-score -------------------------------------
# conditions = [
#     data_slowCtrl["slowCtrl_zScore"] < -zscore_threshold,
#     data_slowCtrl["slowCtrl_zScore"] > zscore_threshold
# ]

# data_slowCtrl["slowCtrl_status"] = np.select(conditions, status, default="intermediate")

# # ----------------------------------------- Update excel file with z-scores -------------------------------------------
# data_slowCtrl.to_excel("slow_controllers_zscores.xlsx", index=False)