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

#######################################################################################################################
# ---------------------- Select only fast 3rd order methods with MRIHTol-I controller (Brusselator) -------------------------------
data_Bruss_fastOrd3_HTol_I = df[(df["order"] == 3) & (df["metric"] == "fast") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIHTol-I")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, Fast, Order 3, MRIHTol-I) ----------------------
allAvg_Bruss_fastOrd3_HTol_I = data_Bruss_fastOrd3_HTol_I["AvgRank"].mean()
allStd_Bruss_fastOrd3_HTol_I = data_Bruss_fastOrd3_HTol_I["AvgRank"].std()

# --------------- Mean of each fast 3rd order method across all controllers -----------------------
methodAvg_Bruss_fastOrd3_HTol_I = data_Bruss_fastOrd3_HTol_I.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_fastOrd3_HTol_I["MRI_zScore_FMO3_Bruss_HTol_I"] = data_Bruss_fastOrd3_HTol_I["MRIMethod"].map(methodAvg_Bruss_fastOrd3_HTol_I)
data_Bruss_fastOrd3_HTol_I["MRI_zScore_FMO3_Bruss_HTol_I"] = (data_Bruss_fastOrd3_HTol_I["MRI_zScore_FMO3_Bruss_HTol_I"] - allAvg_Bruss_fastOrd3_HTol_I)/allStd_Bruss_fastOrd3_HTol_I 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_fastOrd3_HTol_I["MRI_zScore_FMO3_Bruss_HTol_I"] < -zscore_threshold,
    data_Bruss_fastOrd3_HTol_I["MRI_zScore_FMO3_Bruss_HTol_I"] > zscore_threshold
]

data_Bruss_fastOrd3_HTol_I["MRI_status_FMO3_Bruss_HTol_I"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 3rd order methods with MRIDec-I controller (Brusselator) -------------------------------
data_Bruss_fastOrd3_Dec_I = df[(df["order"] == 3) & (df["metric"] == "fast") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIDec-I")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, Fast, Order 3, MRIDec-I) ----------------------
allAvg_Bruss_fastOrd3_Dec_I = data_Bruss_fastOrd3_Dec_I["AvgRank"].mean()
allStd_Bruss_fastOrd3_Dec_I = data_Bruss_fastOrd3_Dec_I["AvgRank"].std()

# --------------- Mean of each fast 3rd order method across all controllers -----------------------
methodAvg_Bruss_fastOrd3_Dec_I = data_Bruss_fastOrd3_Dec_I.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_fastOrd3_Dec_I["MRI_zScore_FMO3_Bruss_Dec_I"] = data_Bruss_fastOrd3_Dec_I["MRIMethod"].map(methodAvg_Bruss_fastOrd3_Dec_I)
data_Bruss_fastOrd3_Dec_I["MRI_zScore_FMO3_Bruss_Dec_I"] = (data_Bruss_fastOrd3_Dec_I["MRI_zScore_FMO3_Bruss_Dec_I"] - allAvg_Bruss_fastOrd3_Dec_I)/allStd_Bruss_fastOrd3_Dec_I 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_fastOrd3_Dec_I["MRI_zScore_FMO3_Bruss_Dec_I"] < -zscore_threshold,
    data_Bruss_fastOrd3_Dec_I["MRI_zScore_FMO3_Bruss_Dec_I"] > zscore_threshold
]

data_Bruss_fastOrd3_Dec_I["MRI_status_FMO3_Bruss_Dec_I"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 3rd order methods with MRIHTol-H0321 controller (Brusselator) -------------------------------
data_Bruss_fastOrd3_HTol_H0321 = df[(df["order"] == 3) & (df["metric"] == "fast") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIHTol-H0321")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, Fast, Order 3, MRIHTol-H0321) ----------------------
allAvg_Bruss_fastOrd3_HTol_H0321 = data_Bruss_fastOrd3_HTol_H0321["AvgRank"].mean()
allStd_Bruss_fastOrd3_HTol_H0321= data_Bruss_fastOrd3_HTol_H0321["AvgRank"].std()

# --------------- Mean of each fast 3rd order method across all controllers -----------------------
methodAvg_Bruss_fastOrd3_HTol_H0321 = data_Bruss_fastOrd3_HTol_H0321.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_fastOrd3_HTol_H0321["MRI_zScore_FMO3_Bruss_HTol_H0321"] = data_Bruss_fastOrd3_HTol_H0321["MRIMethod"].map(methodAvg_Bruss_fastOrd3_HTol_H0321)
data_Bruss_fastOrd3_HTol_H0321["MRI_zScore_FMO3_Bruss_HTol_H0321"] = (data_Bruss_fastOrd3_HTol_H0321["MRI_zScore_FMO3_Bruss_HTol_H0321"] - allAvg_Bruss_fastOrd3_HTol_H0321)/allStd_Bruss_fastOrd3_HTol_H0321 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_fastOrd3_HTol_H0321["MRI_zScore_FMO3_Bruss_HTol_H0321"] < -zscore_threshold,
    data_Bruss_fastOrd3_HTol_H0321["MRI_zScore_FMO3_Bruss_HTol_H0321"] > zscore_threshold
]

data_Bruss_fastOrd3_HTol_H0321["MRI_status_FMO3_Bruss_HTol_H0321"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 3rd order methods with MRIDec-H0321 controller (Brusselator) -------------------------------
data_Bruss_fastOrd3_Dec_H0321 = df[(df["order"] == 3) & (df["metric"] == "fast") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIDec-H0321")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, Fast, Order 3, MRIDec-H0321) ----------------------
allAvg_Bruss_fastOrd3_Dec_H0321 = data_Bruss_fastOrd3_Dec_H0321["AvgRank"].mean()
allStd_Bruss_fastOrd3_Dec_H0321= data_Bruss_fastOrd3_Dec_H0321["AvgRank"].std()

# --------------- Mean of each fast 3rd order method across all controllers -----------------------
methodAvg_Bruss_fastOrd3_Dec_H0321 = data_Bruss_fastOrd3_Dec_H0321.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_fastOrd3_Dec_H0321["MRI_zScore_FMO3_Bruss_Dec_H0321"] = data_Bruss_fastOrd3_Dec_H0321["MRIMethod"].map(methodAvg_Bruss_fastOrd3_Dec_H0321)
data_Bruss_fastOrd3_Dec_H0321["MRI_zScore_FMO3_Bruss_Dec_H0321"] = (data_Bruss_fastOrd3_Dec_H0321["MRI_zScore_FMO3_Bruss_Dec_H0321"] - allAvg_Bruss_fastOrd3_Dec_H0321)/allStd_Bruss_fastOrd3_Dec_H0321 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_fastOrd3_Dec_H0321["MRI_zScore_FMO3_Bruss_Dec_H0321"] < -zscore_threshold,
    data_Bruss_fastOrd3_Dec_H0321["MRI_zScore_FMO3_Bruss_Dec_H0321"] > zscore_threshold
]

data_Bruss_fastOrd3_Dec_H0321["MRI_status_FMO3_Bruss_Dec_H0321"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 3rd order methods with MRIHTol-H211 controller (Brusselator) -------------------------------
data_Bruss_fastOrd3_HTol_H211 = df[(df["order"] == 3) & (df["metric"] == "fast") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIHTol-H211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, Fast, Order 3, MRIHTol-H211) ----------------------
allAvg_Bruss_fastOrd3_HTol_H211 = data_Bruss_fastOrd3_HTol_H211["AvgRank"].mean()
allStd_Bruss_fastOrd3_HTol_H211 = data_Bruss_fastOrd3_HTol_H211["AvgRank"].std()

# --------------- Mean of each fast 3rd order method across all controllers -----------------------
methodAvg_Bruss_fastOrd3_HTol_H211 = data_Bruss_fastOrd3_HTol_H211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_fastOrd3_HTol_H211["MRI_zScore_FMO3_Bruss_HTol_H211"] = data_Bruss_fastOrd3_HTol_H211["MRIMethod"].map(methodAvg_Bruss_fastOrd3_HTol_H211)
data_Bruss_fastOrd3_HTol_H211["MRI_zScore_FMO3_Bruss_HTol_H211"] = (data_Bruss_fastOrd3_HTol_H211["MRI_zScore_FMO3_Bruss_HTol_H211"] - allAvg_Bruss_fastOrd3_HTol_H211)/allStd_Bruss_fastOrd3_HTol_H211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_fastOrd3_HTol_H211["MRI_zScore_FMO3_Bruss_HTol_H211"] < -zscore_threshold,
    data_Bruss_fastOrd3_HTol_H211["MRI_zScore_FMO3_Bruss_HTol_H211"] > zscore_threshold
]

data_Bruss_fastOrd3_HTol_H211["MRI_status_FMO3_Bruss_HTol_H211"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 3rd order methods with MRIDec-H211 controller (Brusselator) -------------------------------
data_Bruss_fastOrd3_Dec_H211 = df[(df["order"] == 3) & (df["metric"] == "fast") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIDec-H211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, Fast, Order 3, MRIDec-H211) ----------------------
allAvg_Bruss_fastOrd3_Dec_H211 = data_Bruss_fastOrd3_Dec_H211["AvgRank"].mean()
allStd_Bruss_fastOrd3_Dec_H211= data_Bruss_fastOrd3_Dec_H211["AvgRank"].std()

# --------------- Mean of each fast 3rd order method across all controllers -----------------------
methodAvg_Bruss_fastOrd3_Dec_H211 = data_Bruss_fastOrd3_Dec_H211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_fastOrd3_Dec_H211["MRI_zScore_FMO3_Bruss_Dec_H211"] = data_Bruss_fastOrd3_Dec_H211["MRIMethod"].map(methodAvg_Bruss_fastOrd3_Dec_H211)
data_Bruss_fastOrd3_Dec_H211["MRI_zScore_FMO3_Bruss_Dec_H211"] = (data_Bruss_fastOrd3_Dec_H211["MRI_zScore_FMO3_Bruss_Dec_H211"] - allAvg_Bruss_fastOrd3_Dec_H211)/allStd_Bruss_fastOrd3_Dec_H211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_fastOrd3_Dec_H211["MRI_zScore_FMO3_Bruss_Dec_H211"] < -zscore_threshold,
    data_Bruss_fastOrd3_Dec_H211["MRI_zScore_FMO3_Bruss_Dec_H211"] > zscore_threshold
]

data_Bruss_fastOrd3_Dec_H211["MRI_status_FMO3_Bruss_Dec_H211"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 3rd order methods with MRIHTol-H0211 controller (Brusselator) -------------------------------
data_Bruss_fastOrd3_HTol_H0211 = df[(df["order"] == 3) & (df["metric"] == "fast") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIHTol-H0211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, Fast, Order 3, MRIHTol-H0211) ----------------------
allAvg_Bruss_fastOrd3_HTol_H0211 = data_Bruss_fastOrd3_HTol_H0211["AvgRank"].mean()
allStd_Bruss_fastOrd3_HTol_H0211 = data_Bruss_fastOrd3_HTol_H0211["AvgRank"].std()

# --------------- Mean of each fast 3rd order method across all controllers -----------------------
methodAvg_Bruss_fastOrd3_HTol_H0211 = data_Bruss_fastOrd3_HTol_H0211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_fastOrd3_HTol_H0211["MRI_zScore_FMO3_Bruss_HTol_H0211"] = data_Bruss_fastOrd3_HTol_H0211["MRIMethod"].map(methodAvg_Bruss_fastOrd3_HTol_H0211)
data_Bruss_fastOrd3_HTol_H0211["MRI_zScore_FMO3_Bruss_HTol_H0211"] = (data_Bruss_fastOrd3_HTol_H0211["MRI_zScore_FMO3_Bruss_HTol_H0211"] - allAvg_Bruss_fastOrd3_HTol_H0211)/allStd_Bruss_fastOrd3_HTol_H0211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_fastOrd3_HTol_H0211["MRI_zScore_FMO3_Bruss_HTol_H0211"] < -zscore_threshold,
    data_Bruss_fastOrd3_HTol_H0211["MRI_zScore_FMO3_Bruss_HTol_H0211"] > zscore_threshold
]

data_Bruss_fastOrd3_HTol_H0211["MRI_status_FMO3_Bruss_HTol_H0211"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 3rd order methods with MRIDec-H0211 controller (Brusselator) -------------------------------
data_Bruss_fastOrd3_Dec_H0211 = df[(df["order"] == 3) & (df["metric"] == "fast") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIDec-H0211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, Fast, Order 3, MRIDec-H0211) ----------------------
allAvg_Bruss_fastOrd3_Dec_H0211 = data_Bruss_fastOrd3_Dec_H0211["AvgRank"].mean()
allStd_Bruss_fastOrd3_Dec_H0211= data_Bruss_fastOrd3_Dec_H0211["AvgRank"].std()

# --------------- Mean of each fast 3rd order method across all controllers -----------------------
methodAvg_Bruss_fastOrd3_Dec_H0211 = data_Bruss_fastOrd3_Dec_H0211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_fastOrd3_Dec_H0211["MRI_zScore_FMO3_Bruss_Dec_H0211"] = data_Bruss_fastOrd3_Dec_H0211["MRIMethod"].map(methodAvg_Bruss_fastOrd3_Dec_H0211)
data_Bruss_fastOrd3_Dec_H0211["MRI_zScore_FMO3_Bruss_Dec_H0211"] = (data_Bruss_fastOrd3_Dec_H0211["MRI_zScore_FMO3_Bruss_Dec_H0211"] - allAvg_Bruss_fastOrd3_Dec_H0211)/allStd_Bruss_fastOrd3_Dec_H0211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_fastOrd3_Dec_H0211["MRI_zScore_FMO3_Bruss_Dec_H0211"] < -zscore_threshold,
    data_Bruss_fastOrd3_Dec_H0211["MRI_zScore_FMO3_Bruss_Dec_H0211"] > zscore_threshold
]

data_Bruss_fastOrd3_Dec_H0211["MRI_status_FMO3_Bruss_Dec_H0211"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 3rd order methods with MRIHTol-H312 controller (Brusselator) -------------------------------
data_Bruss_fastOrd3_HTol_H312 = df[(df["order"] == 3) & (df["metric"] == "fast") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIHTol-H312")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, Fast, Order 3, MRIHTol-H312) ----------------------
allAvg_Bruss_fastOrd3_HTol_H312 = data_Bruss_fastOrd3_HTol_H312["AvgRank"].mean()
allStd_Bruss_fastOrd3_HTol_H312 = data_Bruss_fastOrd3_HTol_H312["AvgRank"].std()

# --------------- Mean of each fast 3rd order method across all controllers -----------------------
methodAvg_Bruss_fastOrd3_HTol_H312 = data_Bruss_fastOrd3_HTol_H312.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_fastOrd3_HTol_H312["MRI_zScore_FMO3_Bruss_HTol_H312"] = data_Bruss_fastOrd3_HTol_H312["MRIMethod"].map(methodAvg_Bruss_fastOrd3_HTol_H312)
data_Bruss_fastOrd3_HTol_H312["MRI_zScore_FMO3_Bruss_HTol_H312"] = (data_Bruss_fastOrd3_HTol_H312["MRI_zScore_FMO3_Bruss_HTol_H312"] - allAvg_Bruss_fastOrd3_HTol_H312)/allStd_Bruss_fastOrd3_HTol_H312 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_fastOrd3_HTol_H312["MRI_zScore_FMO3_Bruss_HTol_H312"] < -zscore_threshold,
    data_Bruss_fastOrd3_HTol_H312["MRI_zScore_FMO3_Bruss_HTol_H312"] > zscore_threshold
]

data_Bruss_fastOrd3_HTol_H312["MRI_status_FMO3_Bruss_HTol_H312"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 3rd order methods with MRIDec-H312 controller (Brusselator) -------------------------------
data_Bruss_fastOrd3_Dec_H312 = df[(df["order"] == 3) & (df["metric"] == "fast") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIDec-H312")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, Fast, Order 3, MRIDec-H312) ----------------------
allAvg_Bruss_fastOrd3_Dec_H312 = data_Bruss_fastOrd3_Dec_H312["AvgRank"].mean()
allStd_Bruss_fastOrd3_Dec_H312= data_Bruss_fastOrd3_Dec_H312["AvgRank"].std()

# --------------- Mean of each fast 3rd order method across all controllers -----------------------
methodAvg_Bruss_fastOrd3_Dec_H312 = data_Bruss_fastOrd3_Dec_H312.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_fastOrd3_Dec_H312["MRI_zScore_FMO3_Bruss_Dec_H312"] = data_Bruss_fastOrd3_Dec_H312["MRIMethod"].map(methodAvg_Bruss_fastOrd3_Dec_H312)
data_Bruss_fastOrd3_Dec_H312["MRI_zScore_FMO3_Bruss_Dec_H312"] = (data_Bruss_fastOrd3_Dec_H312["MRI_zScore_FMO3_Bruss_Dec_H312"] - allAvg_Bruss_fastOrd3_Dec_H312)/allStd_Bruss_fastOrd3_Dec_H312 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_fastOrd3_Dec_H312["MRI_zScore_FMO3_Bruss_Dec_H312"] < -zscore_threshold,
    data_Bruss_fastOrd3_Dec_H312["MRI_zScore_FMO3_Bruss_Dec_H312"] > zscore_threshold
]

data_Bruss_fastOrd3_Dec_H312["MRI_status_FMO3_Bruss_Dec_H312"] = np.select(conditions, status, default="intermediate")


# ----------------------------------- Store all data in one excel file with multiple sheets ---------------------------------
with pd.ExcelWriter('allBruss_fastOrder3.xlsx') as writer:
    data_Bruss_fastOrd3_HTol_I.to_excel(writer, sheet_name='data_Bruss_fastOrd3_HTol_I', index=False)
    data_Bruss_fastOrd3_Dec_I.to_excel(writer, sheet_name='data_Bruss_fastOrd3_Dec_I', index=False)

    data_Bruss_fastOrd3_HTol_H0321.to_excel(writer, sheet_name='data_Bruss_fastOrd3_HTol_H0321', index=False)
    data_Bruss_fastOrd3_Dec_H0321.to_excel(writer, sheet_name='data_Bruss_fastOrd3_Dec_H0321', index=False)

    data_Bruss_fastOrd3_HTol_H211.to_excel(writer, sheet_name='data_Bruss_fastOrd3_HTol_H211', index=False)
    data_Bruss_fastOrd3_Dec_H211.to_excel(writer, sheet_name='data_Bruss_fastOrd3_Dec_H211', index=False)

    data_Bruss_fastOrd3_HTol_H0211.to_excel(writer, sheet_name='data_Bruss_fastOrd3_HTol_H0211', index=False)
    data_Bruss_fastOrd3_Dec_H0211.to_excel(writer, sheet_name='data_Bruss_fastOrd3_Dec_H0211', index=False)

    data_Bruss_fastOrd3_HTol_H312.to_excel(writer, sheet_name='data_Bruss_fastOrd3_HTol_H312', index=False)
    data_Bruss_fastOrd3_Dec_H312.to_excel(writer, sheet_name='data_Bruss_fastOrd3_Dec_H312', index=False)



