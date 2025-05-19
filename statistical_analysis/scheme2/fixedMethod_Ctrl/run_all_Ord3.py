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
# ---------------------- Select all controllers with ARKODE_IMEX_MRI_SR32 (Brusselator) -------------------------------
data_Bruss_SR32 = df[(df["MRIMethod"] == "ARKODE_IMEX_MRI_SR32") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_IMEX_MRI_SR32) ----------------------
allAvg_Bruss_SR32 = data_Bruss_SR32["AvgRank"].mean()
allStd_Bruss_SR32 = data_Bruss_SR32["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_IMEX_MRI_SR32 -----------------------
methodAvg_Bruss_SR32 = data_Bruss_SR32.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_SR32["zScore_Bruss_SR32"] = data_Bruss_SR32["Controller"].map(methodAvg_Bruss_SR32)
data_Bruss_SR32["zScore_Bruss_SR32"] = (data_Bruss_SR32["zScore_Bruss_SR32"] - allAvg_Bruss_SR32)/allStd_Bruss_SR32

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_SR32["zScore_Bruss_SR32"] < -zscore_threshold,
    data_Bruss_SR32["zScore_Bruss_SR32"] > zscore_threshold
]

data_Bruss_SR32["status_Bruss_SR32"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_ERK33a (Brusselator) -------------------------------
data_Bruss_ERK33a = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_ERK33a") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MRI_GARK_ERK33a) ----------------------
allAvg_Bruss_ERK33a = data_Bruss_ERK33a["AvgRank"].mean()
allStd_Bruss_ERK33a = data_Bruss_ERK33a["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_ERK33a -----------------------
methodAvg_Bruss_ERK33a = data_Bruss_ERK33a.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_ERK33a["zScore_Bruss_ERK33a"] = data_Bruss_ERK33a["Controller"].map(methodAvg_Bruss_ERK33a)
data_Bruss_ERK33a["zScore_Bruss_ERK33a"] = (data_Bruss_ERK33a["zScore_Bruss_ERK33a"] - allAvg_Bruss_ERK33a)/allStd_Bruss_ERK33a

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_ERK33a["zScore_Bruss_ERK33a"] < -zscore_threshold,
    data_Bruss_ERK33a["zScore_Bruss_ERK33a"] > zscore_threshold
]

data_Bruss_ERK33a["status_Bruss_ERK33a"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_ESDIRK34a (Brusselator) -------------------------------
data_Bruss_ESDIRK34a = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_ESDIRK34a") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MRI_GARK_ESDIRK34a) ----------------------
allAvg_Bruss_ESDIRK34a = data_Bruss_ESDIRK34a["AvgRank"].mean()
allStd_Bruss_ESDIRK34a = data_Bruss_ESDIRK34a["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_ESDIRK34a -----------------------
methodAvg_Bruss_ESDIRK34a = data_Bruss_ESDIRK34a.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_ESDIRK34a["zScore_Bruss_ESDIRK34a"] = data_Bruss_ESDIRK34a["Controller"].map(methodAvg_Bruss_ESDIRK34a)
data_Bruss_ESDIRK34a["zScore_Bruss_ESDIRK34a"] = (data_Bruss_ESDIRK34a["zScore_Bruss_ESDIRK34a"] - allAvg_Bruss_ESDIRK34a)/allStd_Bruss_ESDIRK34a

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_ESDIRK34a["zScore_Bruss_ESDIRK34a"] < -zscore_threshold,
    data_Bruss_ESDIRK34a["zScore_Bruss_ESDIRK34a"] > zscore_threshold
]

data_Bruss_ESDIRK34a["status_Bruss_ESDIRK34a"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MERK32 (Brusselator) -------------------------------
data_Bruss_MERK32 = df[(df["MRIMethod"] == "ARKODE_MERK32") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MERK32) ----------------------
allAvg_Bruss_MERK32 = data_Bruss_MERK32["AvgRank"].mean()
allStd_Bruss_MERK32 = data_Bruss_MERK32["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MERK32 -----------------------
methodAvg_Bruss_MERK32 = data_Bruss_MERK32.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_MERK32["zScore_Bruss_MERK32"] = data_Bruss_MERK32["Controller"].map(methodAvg_Bruss_MERK32)
data_Bruss_MERK32["zScore_Bruss_MERK32"] = (data_Bruss_MERK32["zScore_Bruss_MERK32"] - allAvg_Bruss_MERK32)/allStd_Bruss_MERK32

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_MERK32["zScore_Bruss_MERK32"] < -zscore_threshold,
    data_Bruss_MERK32["zScore_Bruss_MERK32"] > zscore_threshold
]

data_Bruss_MERK32["status_Bruss_MERK32"] = np.select(conditions, status, default="intermediate")




#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_IMEX_MRI_SR32 (KPR) -------------------------------
data_KPR_SR32 = df[(df["MRIMethod"] == "ARKODE_IMEX_MRI_SR32") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_IMEX_MRI_SR32) ----------------------
allAvg_KPR_SR32 = data_KPR_SR32["AvgRank"].mean()
allStd_KPR_SR32 = data_KPR_SR32["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_IMEX_MRI_SR32 -----------------------
methodAvg_KPR_SR32 = data_KPR_SR32.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_SR32["zScore_KPR_SR32"] = data_KPR_SR32["Controller"].map(methodAvg_KPR_SR32)
data_KPR_SR32["zScore_KPR_SR32"] = (data_KPR_SR32["zScore_KPR_SR32"] - allAvg_KPR_SR32)/allStd_KPR_SR32

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_SR32["zScore_KPR_SR32"] < -zscore_threshold,
    data_KPR_SR32["zScore_KPR_SR32"] > zscore_threshold
]

data_KPR_SR32["status_KPR_SR32"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_ERK33a (KPR) -------------------------------
data_KPR_ERK33a = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_ERK33a") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_MRI_GARK_ERK33a) ----------------------
allAvg_KPR_ERK33a = data_KPR_ERK33a["AvgRank"].mean()
allStd_KPR_ERK33a = data_KPR_ERK33a["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_ERK33a -----------------------
methodAvg_KPR_ERK33a = data_KPR_ERK33a.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_ERK33a["zScore_KPR_ERK33a"] = data_KPR_ERK33a["Controller"].map(methodAvg_KPR_ERK33a)
data_KPR_ERK33a["zScore_KPR_ERK33a"] = (data_KPR_ERK33a["zScore_KPR_ERK33a"] - allAvg_KPR_ERK33a)/allStd_KPR_ERK33a

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_ERK33a["zScore_KPR_ERK33a"] < -zscore_threshold,
    data_KPR_ERK33a["zScore_KPR_ERK33a"] > zscore_threshold
]

data_KPR_ERK33a["status_KPR_ERK33a"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_ESDIRK34a (KPR) -------------------------------
data_KPR_ESDIRK34a = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_ESDIRK34a") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_MRI_GARK_ESDIRK34a) ----------------------
allAvg_KPR_ESDIRK34a = data_KPR_ESDIRK34a["AvgRank"].mean()
allStd_KPR_ESDIRK34a = data_KPR_ESDIRK34a["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_ESDIRK34a -----------------------
methodAvg_KPR_ESDIRK34a = data_KPR_ESDIRK34a.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_ESDIRK34a["zScore_KPR_ESDIRK34a"] = data_KPR_ESDIRK34a["Controller"].map(methodAvg_KPR_ESDIRK34a)
data_KPR_ESDIRK34a["zScore_KPR_ESDIRK34a"] = (data_KPR_ESDIRK34a["zScore_KPR_ESDIRK34a"] - allAvg_KPR_ESDIRK34a)/allStd_KPR_ESDIRK34a

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_ESDIRK34a["zScore_KPR_ESDIRK34a"] < -zscore_threshold,
    data_KPR_ESDIRK34a["zScore_KPR_ESDIRK34a"] > zscore_threshold
]

data_KPR_ESDIRK34a["status_KPR_ESDIRK34a"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MERK32 (KPR) -------------------------------
data_KPR_MERK32 = df[(df["MRIMethod"] == "ARKODE_MERK32") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_MERK32) ----------------------
allAvg_KPR_MERK32 = data_KPR_MERK32["AvgRank"].mean()
allStd_KPR_MERK32 = data_KPR_MERK32["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MERK32 -----------------------
methodAvg_KPR_MERK32 = data_KPR_MERK32.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_MERK32["zScore_KPR_MERK32"] = data_KPR_MERK32["Controller"].map(methodAvg_KPR_MERK32)
data_KPR_MERK32["zScore_KPR_MERK32"] = (data_KPR_MERK32["zScore_KPR_MERK32"] - allAvg_KPR_MERK32)/allStd_KPR_MERK32

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_MERK32["zScore_KPR_MERK32"] < -zscore_threshold,
    data_KPR_MERK32["zScore_KPR_MERK32"] > zscore_threshold
]

data_KPR_MERK32["status_KPR_MERK32"] = np.select(conditions, status, default="intermediate")


# ----------------------------------- Store all data in one excel file with multiple sheets ---------------------------------
with pd.ExcelWriter('allOrder3_controllers.xlsx') as writer:
    data_Bruss_SR32.to_excel(writer, sheet_name='data_Bruss_SR32', index=False)
    data_Bruss_ERK33a.to_excel(writer, sheet_name='data_Bruss_ERK33a', index=False)
    data_Bruss_ESDIRK34a.to_excel(writer, sheet_name='data_Bruss_ESDIRK34a', index=False)
    data_Bruss_MERK32.to_excel(writer, sheet_name='data_Bruss_MERK32', index=False)
    data_KPR_SR32.to_excel(writer, sheet_name='data_Bruss_SR32', index=False)
    data_KPR_ERK33a.to_excel(writer, sheet_name='data_Bruss_ERK33a', index=False)
    data_KPR_ESDIRK34a.to_excel(writer, sheet_name='data_Bruss_ESDIRK34a', index=False)
    data_KPR_MERK32.to_excel(writer, sheet_name='data_Bruss_MERK32', index=False)



