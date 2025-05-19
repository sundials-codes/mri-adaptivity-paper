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

# ----------------------- Classification of Methods / Controllers -------------------------
status = ["best", "worse"]

# --------------------------------- Load your Excel file ------------------------------------------
df = pd.read_excel("rank_stats.xlsx")

# ------------------------------------- Remove the H-h controllers --------------------------------
controllers_to_remove = ['MRIPI', 'MRIPID', 'MRICC', 'MRILL']

#######################################################################################################################
# ---------------------- Select only fast 2nd order methods (Brusselator) -------------------------------
data_Bruss_fastOrd2 = df[(df["order"] == 2) & (df["metric"] == "fast") & (df["Param"].isin([0.0001, 0.00001])) 
                      & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------- Mean and standard deviation of the selected data (Brusselator, Fast, Order 2) --------
allAvg_Bruss_fastOrd2 = data_Bruss_fastOrd2["AvgRank"].mean()
allStd_Bruss_fastOrd2 = data_Bruss_fastOrd2["AvgRank"].std()

# --------------- Mean of each fast 2nd order method across all controllers -----------------------
methodAvg_fastOrd2_Bruss = data_Bruss_fastOrd2.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_fastOrd2["MRI_zScore_FMO2_Bruss"] = data_Bruss_fastOrd2["MRIMethod"].map(methodAvg_fastOrd2_Bruss)
data_Bruss_fastOrd2["MRI_zScore_FMO2_Bruss"] = (data_Bruss_fastOrd2["MRI_zScore_FMO2_Bruss"] - allAvg_Bruss_fastOrd2)/allStd_Bruss_fastOrd2 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_fastOrd2["MRI_zScore_FMO2_Bruss"] < -zscore_threshold,
    data_Bruss_fastOrd2["MRI_zScore_FMO2_Bruss"] > zscore_threshold
]

data_Bruss_fastOrd2["MRI_status_FMO2_Bruss"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------------- Select only fast 2nd order methods (KPR) ------------------------------------
data_KPR_fastOrd2 = df[(df["order"] == 2) & (df["metric"] == "fast") & (df["Param"].isin([50, 500])) 
                      & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ---------------- Mean and standard deviation of the selected data (KPRelator, Fast, Order 2) ---------------
allAvg_KPR_fastOrd2 = data_KPR_fastOrd2["AvgRank"].mean()
allStd_KPR_fastOrd2 = data_KPR_fastOrd2["AvgRank"].std()

# ---------------------- Mean of each fast 2nd order method across all controllers --------------------------
methodAvg_fastOrd2_KPR = data_KPR_fastOrd2.groupby("MRIMethod")["AvgRank"].mean()

# ------------ Calculate the z-score of each method and store on each row corresponding to the method --------
data_KPR_fastOrd2["MRI_zScore_FMO2_KPR"] = data_KPR_fastOrd2["MRIMethod"].map(methodAvg_fastOrd2_KPR)
data_KPR_fastOrd2["MRI_zScore_FMO2_KPR"] = (data_KPR_fastOrd2["MRI_zScore_FMO2_KPR"] - allAvg_KPR_fastOrd2)/allStd_KPR_fastOrd2 

# -------------------------------- Classify each method based on z-score --------------------------------------
conditions = [
    data_KPR_fastOrd2["MRI_zScore_FMO2_KPR"] < -zscore_threshold,
    data_KPR_fastOrd2["MRI_zScore_FMO2_KPR"] > zscore_threshold
]

data_KPR_fastOrd2["MRI_status_FMO2_KPR"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 2nd order methods (Brusselator) -------------------------------
data_Bruss_slowOrd2 = df[(df["order"] == 2) & (df["metric"] == "slow") & (df["Param"].isin([0.0001, 0.00001])) 
                      & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------- Mean and standard deviation of the selected data (Brusselator, slow, Order 2) --------
allAvg_Bruss_slowOrd2 = data_Bruss_slowOrd2["AvgRank"].mean()
allStd_Bruss_slowOrd2 = data_Bruss_slowOrd2["AvgRank"].std()

# --------------- Mean of each slow 2nd order method across all controllers -----------------------
methodAvg_slowOrd2_Bruss = data_Bruss_slowOrd2.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_slowOrd2["MRI_zScore_SMO2_Bruss"] = data_Bruss_slowOrd2["MRIMethod"].map(methodAvg_slowOrd2_Bruss)
data_Bruss_slowOrd2["MRI_zScore_SMO2_Bruss"] = (data_Bruss_slowOrd2["MRI_zScore_SMO2_Bruss"] - allAvg_Bruss_slowOrd2)/allStd_Bruss_slowOrd2 

# ---------------------------- Classify each method based on z-score ---------------------------------
conditions = [
    data_Bruss_slowOrd2["MRI_zScore_SMO2_Bruss"] < -zscore_threshold,
    data_Bruss_slowOrd2["MRI_zScore_SMO2_Bruss"] > zscore_threshold
]

data_Bruss_slowOrd2["MRI_status_SMO2_Bruss"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------------- Select only slow 2nd order methods (KPR) ------------------------------------
data_KPR_slowOrd2 = df[(df["order"] == 2) & (df["metric"] == "slow") & (df["Param"].isin([50, 500])) 
                      & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ---------------- Mean and standard deviation of the selected data (KPRelator, slow, Order 2) ---------------
allAvg_KPR_slowOrd2 = data_KPR_slowOrd2["AvgRank"].mean()
allStd_KPR_slowOrd2 = data_KPR_slowOrd2["AvgRank"].std()

# ---------------------- Mean of each slow 2nd order method across all controllers --------------------------
methodAvg_Order2_KPR = data_KPR_slowOrd2.groupby("MRIMethod")["AvgRank"].mean()

# ------------ Calculate the z-score of each method and store on each row corresponding to the method --------
data_KPR_slowOrd2["MRI_zScore_SMO2_KPR"] = data_KPR_slowOrd2["MRIMethod"].map(methodAvg_Order2_KPR)
data_KPR_slowOrd2["MRI_zScore_SMO2_KPR"] = (data_KPR_slowOrd2["MRI_zScore_SMO2_KPR"] - allAvg_KPR_slowOrd2)/allStd_KPR_slowOrd2 

# -------------------------------- Classify each method based on z-score --------------------------------------
conditions = [
    data_KPR_slowOrd2["MRI_zScore_SMO2_KPR"] < -zscore_threshold,
    data_KPR_slowOrd2["MRI_zScore_SMO2_KPR"] > zscore_threshold
]

data_KPR_slowOrd2["MRI_status_SMO2_KPR"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 3rd order methods (Brusselator) -------------------------------
data_Bruss_fastOrd3 = df[(df["order"] == 3) & (df["metric"] == "fast") & (df["Param"].isin([0.0001, 0.00001])) 
                      & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------- Mean and standard deviation of the selected data (Brusselator, Fast, Order 3) --------
allAvg_Bruss_fastOrd3 = data_Bruss_fastOrd3["AvgRank"].mean()
allStd_Bruss_fastOrd3 = data_Bruss_fastOrd3["AvgRank"].std()

# --------------- Mean of each fast 3rd order method across all controllers -----------------------
methodAvg_fastOrd3_Bruss = data_Bruss_fastOrd3.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_fastOrd3["MRI_zScore_FMO3_Bruss"] = data_Bruss_fastOrd3["MRIMethod"].map(methodAvg_fastOrd3_Bruss)
data_Bruss_fastOrd3["MRI_zScore_FMO3_Bruss"] = (data_Bruss_fastOrd3["MRI_zScore_FMO3_Bruss"] - allAvg_Bruss_fastOrd3)/allStd_Bruss_fastOrd3 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_fastOrd3["MRI_zScore_FMO3_Bruss"] < -zscore_threshold,
    data_Bruss_fastOrd3["MRI_zScore_FMO3_Bruss"] > zscore_threshold
]

data_Bruss_fastOrd3["MRI_status_FMO3_Bruss"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------------- Select only fast 3rd order methods (KPR) ------------------------------------
data_KPR_fastOrd3 = df[(df["order"] == 3) & (df["metric"] == "fast") & (df["Param"].isin([50, 500])) 
                      & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ---------------- Mean and standard deviation of the selected data (KPRelator, Fast, Order 3) ---------------
allAvg_KPR_fastOrd3 = data_KPR_fastOrd3["AvgRank"].mean()
allStd_KPR_fastOrd3 = data_KPR_fastOrd3["AvgRank"].std()

# ---------------------- Mean of each fast 3rd order method across all controllers --------------------------
methodAvg_fastOrd3_KPR = data_KPR_fastOrd3.groupby("MRIMethod")["AvgRank"].mean()

# ------------ Calculate the z-score of each method and store on each row corresponding to the method --------
data_KPR_fastOrd3["MRI_zScore_FMO3_KPR"] = data_KPR_fastOrd3["MRIMethod"].map(methodAvg_fastOrd3_KPR)
data_KPR_fastOrd3["MRI_zScore_FMO3_KPR"] = (data_KPR_fastOrd3["MRI_zScore_FMO3_KPR"] - allAvg_KPR_fastOrd3)/allStd_KPR_fastOrd3 

# -------------------------------- Classify each method based on z-score --------------------------------------
conditions = [
    data_KPR_fastOrd3["MRI_zScore_FMO3_KPR"] < -zscore_threshold,
    data_KPR_fastOrd3["MRI_zScore_FMO3_KPR"] > zscore_threshold
]

data_KPR_fastOrd3["MRI_status_FMO3_KPR"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 3rd order methods (Brusselator) -------------------------------
data_Bruss_slowOrd3 = df[(df["order"] == 3) & (df["metric"] == "slow") & (df["Param"].isin([0.0001, 0.00001])) 
                      & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------- Mean and standard deviation of the selected data (Brusselator, slow, Order 3) --------
allAvg_Bruss_slowOrd3 = data_Bruss_slowOrd3["AvgRank"].mean()
allStd_Bruss_slowOrd3 = data_Bruss_slowOrd3["AvgRank"].std()

# --------------- Mean of each slow 3rd order method across all controllers -----------------------
methodAvg_slowOrd3_Bruss = data_Bruss_slowOrd3.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_slowOrd3["MRI_zScore_SMO3_Bruss"] = data_Bruss_slowOrd3["MRIMethod"].map(methodAvg_slowOrd3_Bruss)
data_Bruss_slowOrd3["MRI_zScore_SMO3_Bruss"] = (data_Bruss_slowOrd3["MRI_zScore_SMO3_Bruss"] - allAvg_Bruss_slowOrd3)/allStd_Bruss_slowOrd3 

# ---------------------------- Classify each method based on z-score ---------------------------------
conditions = [
    data_Bruss_slowOrd3["MRI_zScore_SMO3_Bruss"] < -zscore_threshold,
    data_Bruss_slowOrd3["MRI_zScore_SMO3_Bruss"] > zscore_threshold
]

data_Bruss_slowOrd3["MRI_status_SMO3_Bruss"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------------- Select only slow 3rd order methods (KPR) ------------------------------------
data_KPR_slowOrd3 = df[(df["order"] == 3) & (df["metric"] == "slow") & (df["Param"].isin([50, 500])) 
                      & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ---------------- Mean and standard deviation of the selected data (KPRelator, slow, Order 3) ---------------
allAvg_KPR_slowOrd3 = data_KPR_slowOrd3["AvgRank"].mean()
allStd_KPR_slowOrd3 = data_KPR_slowOrd3["AvgRank"].std()

# ---------------------- Mean of each slow 3rd order method across all controllers --------------------------
methodAvg_Order3_KPR = data_KPR_slowOrd3.groupby("MRIMethod")["AvgRank"].mean()

# ------------ Calculate the z-score of each method and store on each row corresponding to the method --------
data_KPR_slowOrd3["MRI_zScore_SMO3_KPR"] = data_KPR_slowOrd3["MRIMethod"].map(methodAvg_Order3_KPR)
data_KPR_slowOrd3["MRI_zScore_SMO3_KPR"] = (data_KPR_slowOrd3["MRI_zScore_SMO3_KPR"] - allAvg_KPR_slowOrd3)/allStd_KPR_slowOrd3 

# -------------------------------- Classify each method based on z-score --------------------------------------
conditions = [
    data_KPR_slowOrd3["MRI_zScore_SMO3_KPR"] < -zscore_threshold,
    data_KPR_slowOrd3["MRI_zScore_SMO3_KPR"] > zscore_threshold
]

data_KPR_slowOrd3["MRI_status_SMO3_KPR"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 4th and 5th order methods (Brusselator) -------------------------------
data_Bruss_fastOrd45 = df[(df["order"].isin([4, 5])) & (df["metric"] == "fast") & (df["Param"].isin([0.0001, 0.00001])) 
                       & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------- Mean and standard deviation of the selected data (Brusselator, Fast, Order 4 and 5) --------
allAvg_Bruss_fastOrd45 = data_Bruss_fastOrd45["AvgRank"].mean()
allStd_Bruss_fastOrd45 = data_Bruss_fastOrd45["AvgRank"].std()

# --------------- Mean of each fast 4th and 5th order method across all controllers -----------------------
methodAvg_fastOrd45_Bruss = data_Bruss_fastOrd45.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_fastOrd45["MRI_zScore_FMO45_Bruss"] = data_Bruss_fastOrd45["MRIMethod"].map(methodAvg_fastOrd45_Bruss)
data_Bruss_fastOrd45["MRI_zScore_FMO45_Bruss"] = (data_Bruss_fastOrd45["MRI_zScore_FMO45_Bruss"] - allAvg_Bruss_fastOrd45)/allStd_Bruss_fastOrd45 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_fastOrd45["MRI_zScore_FMO45_Bruss"] < -zscore_threshold,
    data_Bruss_fastOrd45["MRI_zScore_FMO45_Bruss"] > zscore_threshold
]

data_Bruss_fastOrd45["MRI_status_FMO45_Bruss"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------------- Select only fast 4th and 5th order methods (KPR) ------------------------------------
data_KPR_fastOrd45 = df[(df["order"].isin([4, 5])) & (df["metric"] == "fast") & (df["Param"].isin([50, 500])) 
                      & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ---------------- Mean and standard deviation of the selected data (KPRelator, Fast, Order 4 and 5) ---------------
allAvg_KPR_fastOrd45 = data_KPR_fastOrd45["AvgRank"].mean()
allStd_KPR_fastOrd45 = data_KPR_fastOrd45["AvgRank"].std()

# ---------------------- Mean of each fast 4th and 5th order method across all controllers --------------------------
methodAvg_fastOrd45_KPR = data_KPR_fastOrd45.groupby("MRIMethod")["AvgRank"].mean()

# ------------ Calculate the z-score of each method and store on each row corresponding to the method --------
data_KPR_fastOrd45["MRI_zScore_FMO45_KPR"] = data_KPR_fastOrd45["MRIMethod"].map(methodAvg_fastOrd45_KPR)
data_KPR_fastOrd45["MRI_zScore_FMO45_KPR"] = (data_KPR_fastOrd45["MRI_zScore_FMO45_KPR"] - allAvg_KPR_fastOrd45)/allStd_KPR_fastOrd45 

# -------------------------------- Classify each method based on z-score --------------------------------------
conditions = [
    data_KPR_fastOrd45["MRI_zScore_FMO45_KPR"] < -zscore_threshold,
    data_KPR_fastOrd45["MRI_zScore_FMO45_KPR"] > zscore_threshold
]

data_KPR_fastOrd45["MRI_status_FMO45_KPR"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 4th and 5th order methods (Brusselator) -------------------------------
data_Bruss_slowOrd45 = df[(df["order"].isin([4, 5])) & (df["metric"] == "slow") & (df["Param"].isin([0.0001, 0.00001])) 
                      & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------- Mean and standard deviation of the selected data (Brusselator, slow, Order 4 and 5) --------
allAvg_Bruss_slowOrd45 = data_Bruss_slowOrd45["AvgRank"].mean()
allStd_Bruss_slowOrd45 = data_Bruss_slowOrd45["AvgRank"].std()

# --------------- Mean of each slow 4th and 5th order method across all controllers -----------------------
methodAvg_slowOrd45_Bruss = data_Bruss_slowOrd45.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_slowOrd45["MRI_zScore_SMO45_Bruss"] = data_Bruss_slowOrd45["MRIMethod"].map(methodAvg_slowOrd45_Bruss)
data_Bruss_slowOrd45["MRI_zScore_SMO45_Bruss"] = (data_Bruss_slowOrd45["MRI_zScore_SMO45_Bruss"] - allAvg_Bruss_slowOrd45)/allStd_Bruss_slowOrd45 

# ---------------------------- Classify each method based on z-score ---------------------------------
conditions = [
    data_Bruss_slowOrd45["MRI_zScore_SMO45_Bruss"] < -zscore_threshold,
    data_Bruss_slowOrd45["MRI_zScore_SMO45_Bruss"] > zscore_threshold
]

data_Bruss_slowOrd45["MRI_status_SMO45_Bruss"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------------- Select only slow 4th and 5th order methods (KPR) ------------------------------------
data_KPR_slowOrd45 = df[(df["order"].isin([4, 5])) & (df["metric"] == "slow") & (df["Param"].isin([50, 500])) 
                      & ~df['Controller'].isin(controllers_to_remove)][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ---------------- Mean and standard deviation of the selected data (KPRelator, slow, Order 4 and 5) ---------------
allAvg_KPR_slowOrd45 = data_KPR_slowOrd45["AvgRank"].mean()
allStd_KPR_slowOrd45 = data_KPR_slowOrd45["AvgRank"].std()

# ---------------------- Mean of each slow 4th and 5th order method across all controllers --------------------------
methodAvg_Order45_KPR = data_KPR_slowOrd45.groupby("MRIMethod")["AvgRank"].mean()

# ------------ Calculate the z-score of each method and store on each row corresponding to the method --------
data_KPR_slowOrd45["MRI_zScore_SMO45_KPR"] = data_KPR_slowOrd45["MRIMethod"].map(methodAvg_Order45_KPR)
data_KPR_slowOrd45["MRI_zScore_SMO45_KPR"] = (data_KPR_slowOrd45["MRI_zScore_SMO45_KPR"] - allAvg_KPR_slowOrd45)/allStd_KPR_slowOrd45 

# -------------------------------- Classify each method based on z-score --------------------------------------
conditions = [
    data_KPR_slowOrd45["MRI_zScore_SMO45_KPR"] < -zscore_threshold,
    data_KPR_slowOrd45["MRI_zScore_SMO45_KPR"] > zscore_threshold
]

data_KPR_slowOrd45["MRI_status_SMO45_KPR"] = np.select(conditions, status, default="intermediate")


# ----------------------------------- Store all data in one excel file with multiple sheets ---------------------------------
with pd.ExcelWriter('all_methods_tests.xlsx') as writer:
    data_Bruss_fastOrd2.to_excel(writer, sheet_name='data_Bruss_fastOrd2', index=False)
    data_Bruss_slowOrd2.to_excel(writer, sheet_name='data_Bruss_slowOrd2', index=False)
    data_KPR_fastOrd2.to_excel(writer, sheet_name='data_KPR_fastOrd2', index=False)
    data_KPR_slowOrd2.to_excel(writer, sheet_name='data_KPR_slowOrd2', index=False)

    data_Bruss_fastOrd3.to_excel(writer, sheet_name='data_Bruss_fastOrd3', index=False)
    data_Bruss_slowOrd3.to_excel(writer, sheet_name='data_Bruss_slowOrd3', index=False)
    data_KPR_fastOrd3.to_excel(writer, sheet_name='data_KPR_fastOrd3', index=False)
    data_KPR_slowOrd3.to_excel(writer, sheet_name='data_KPR_slowOrd3', index=False)

    data_Bruss_fastOrd45.to_excel(writer, sheet_name='data_Bruss_fastOrd45', index=False)
    data_Bruss_slowOrd45.to_excel(writer, sheet_name='data_Bruss_slowOrd45', index=False)
    data_KPR_fastOrd45.to_excel(writer, sheet_name='data_KPR_fastOrd45', index=False)
    data_KPR_slowOrd45.to_excel(writer, sheet_name='data_KPR_slowOrd45', index=False)