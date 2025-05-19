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
# ---------------------- Select all controllers with ARKODE_MRI_GARK_ESDIRK46a (Brusselator) -------------------------------
data_Bruss_ESDIRK46a = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_ESDIRK46a") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MRI_GARK_ESDIRK46a) ----------------------
allAvg_Bruss_ESDIRK46a = data_Bruss_ESDIRK46a["AvgRank"].mean()
allStd_Bruss_ESDIRK46a = data_Bruss_ESDIRK46a["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_ESDIRK46a -----------------------
methodAvg_Bruss_ESDIRK46a = data_Bruss_ESDIRK46a.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_ESDIRK46a["zScore_Bruss_ESDIRK46a"] = data_Bruss_ESDIRK46a["Controller"].map(methodAvg_Bruss_ESDIRK46a)
data_Bruss_ESDIRK46a["zScore_Bruss_ESDIRK46a"] = (data_Bruss_ESDIRK46a["zScore_Bruss_ESDIRK46a"] - allAvg_Bruss_ESDIRK46a)/allStd_Bruss_ESDIRK46a

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_ESDIRK46a["zScore_Bruss_ESDIRK46a"] < -zscore_threshold,
    data_Bruss_ESDIRK46a["zScore_Bruss_ESDIRK46a"] > zscore_threshold
]

data_Bruss_ESDIRK46a["status_Bruss_ESDIRK46a"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_IMEX_MRI_SR43 (Brusselator) -------------------------------
data_Bruss_SR43 = df[(df["MRIMethod"] == "ARKODE_IMEX_MRI_SR43") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_IMEX_MRI_SR43) ----------------------
allAvg_Bruss_SR43 = data_Bruss_SR43["AvgRank"].mean()
allStd_Bruss_SR43 = data_Bruss_SR43["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_IMEX_MRI_SR43 -----------------------
methodAvg_Bruss_SR43 = data_Bruss_SR43.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_SR43["zScore_Bruss_SR43"] = data_Bruss_SR43["Controller"].map(methodAvg_Bruss_SR43)
data_Bruss_SR43["zScore_Bruss_SR43"] = (data_Bruss_SR43["zScore_Bruss_SR43"] - allAvg_Bruss_SR43)/allStd_Bruss_SR43

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_SR43["zScore_Bruss_SR43"] < -zscore_threshold,
    data_Bruss_SR43["zScore_Bruss_SR43"] > zscore_threshold
]

data_Bruss_SR43["status_Bruss_SR43"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_ERK45a (Brusselator) -------------------------------
data_Bruss_ERK45a = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_ERK45a") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MRI_GARK_ERK45a) ----------------------
allAvg_Bruss_ERK45a = data_Bruss_ERK45a["AvgRank"].mean()
allStd_Bruss_ERK45a = data_Bruss_ERK45a["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_ERK45a -----------------------
methodAvg_Bruss_ERK45a = data_Bruss_ERK45a.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_ERK45a["zScore_Bruss_ERK45a"] = data_Bruss_ERK45a["Controller"].map(methodAvg_Bruss_ERK45a)
data_Bruss_ERK45a["zScore_Bruss_ERK45a"] = (data_Bruss_ERK45a["zScore_Bruss_ERK45a"] - allAvg_Bruss_ERK45a)/allStd_Bruss_ERK45a

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_ERK45a["zScore_Bruss_ERK45a"] < -zscore_threshold,
    data_Bruss_ERK45a["zScore_Bruss_ERK45a"] > zscore_threshold
]

data_Bruss_ERK45a["status_Bruss_ERK45a"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MERK54 (Brusselator) -------------------------------
data_Bruss_MERK54 = df[(df["MRIMethod"] == "ARKODE_MERK54") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MERK54) ----------------------
allAvg_Bruss_MERK54 = data_Bruss_MERK54["AvgRank"].mean()
allStd_Bruss_MERK54 = data_Bruss_MERK54["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MERK54 -----------------------
methodAvg_Bruss_MERK54 = data_Bruss_MERK54.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_MERK54["zScore_Bruss_MERK54"] = data_Bruss_MERK54["Controller"].map(methodAvg_Bruss_MERK54)
data_Bruss_MERK54["zScore_Bruss_MERK54"] = (data_Bruss_MERK54["zScore_Bruss_MERK54"] - allAvg_Bruss_MERK54)/allStd_Bruss_MERK54

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_MERK54["zScore_Bruss_MERK54"] < -zscore_threshold,
    data_Bruss_MERK54["zScore_Bruss_MERK54"] > zscore_threshold
]

data_Bruss_MERK54["status_Bruss_MERK54"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MERK43 (Brusselator) -------------------------------
data_Bruss_MERK43 = df[(df["MRIMethod"] == "ARKODE_MERK43") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MERK43) ----------------------
allAvg_Bruss_MERK43 = data_Bruss_MERK43["AvgRank"].mean()
allStd_Bruss_MERK43 = data_Bruss_MERK43["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MERK43 -----------------------
methodAvg_Bruss_MERK43 = data_Bruss_MERK43.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_MERK43["zScore_Bruss_MERK43"] = data_Bruss_MERK43["Controller"].map(methodAvg_Bruss_MERK43)
data_Bruss_MERK43["zScore_Bruss_MERK43"] = (data_Bruss_MERK43["zScore_Bruss_MERK43"] - allAvg_Bruss_MERK43)/allStd_Bruss_MERK43

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_MERK43["zScore_Bruss_MERK43"] < -zscore_threshold,
    data_Bruss_MERK43["zScore_Bruss_MERK43"] > zscore_threshold
]

data_Bruss_MERK43["status_Bruss_MERK43"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_ESDIRK46a (KPR) -------------------------------
data_KPR_ESDIRK46a = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_ESDIRK46a") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_MRI_GARK_ESDIRK46a) ----------------------
allAvg_KPR_ESDIRK46a = data_KPR_ESDIRK46a["AvgRank"].mean()
allStd_KPR_ESDIRK46a = data_KPR_ESDIRK46a["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_ESDIRK46a -----------------------
methodAvg_KPR_ESDIRK46a = data_KPR_ESDIRK46a.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_ESDIRK46a["zScore_KPR_ESDIRK46a"] = data_KPR_ESDIRK46a["Controller"].map(methodAvg_KPR_ESDIRK46a)
data_KPR_ESDIRK46a["zScore_KPR_ESDIRK46a"] = (data_KPR_ESDIRK46a["zScore_KPR_ESDIRK46a"] - allAvg_KPR_ESDIRK46a)/allStd_KPR_ESDIRK46a

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_ESDIRK46a["zScore_KPR_ESDIRK46a"] < -zscore_threshold,
    data_KPR_ESDIRK46a["zScore_KPR_ESDIRK46a"] > zscore_threshold
]

data_KPR_ESDIRK46a["status_KPR_ESDIRK46a"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_IMEX_MRI_SR43 (KPR) -------------------------------
data_KPR_SR43 = df[(df["MRIMethod"] == "ARKODE_IMEX_MRI_SR43") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_IMEX_MRI_SR43) ----------------------
allAvg_KPR_SR43 = data_KPR_SR43["AvgRank"].mean()
allStd_KPR_SR43 = data_KPR_SR43["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_IMEX_MRI_SR43 -----------------------
methodAvg_KPR_SR43 = data_KPR_SR43.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_SR43["zScore_KPR_SR43"] = data_KPR_SR43["Controller"].map(methodAvg_KPR_SR43)
data_KPR_SR43["zScore_KPR_SR43"] = (data_KPR_SR43["zScore_KPR_SR43"] - allAvg_KPR_SR43)/allStd_KPR_SR43

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_SR43["zScore_KPR_SR43"] < -zscore_threshold,
    data_KPR_SR43["zScore_KPR_SR43"] > zscore_threshold
]

data_KPR_SR43["status_KPR_SR43"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_ERK45a (KPR) -------------------------------
data_KPR_ERK45a = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_ERK45a") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_MRI_GARK_ERK45a) ----------------------
allAvg_KPR_ERK45a = data_KPR_ERK45a["AvgRank"].mean()
allStd_KPR_ERK45a = data_KPR_ERK45a["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_ERK45a -----------------------
methodAvg_KPR_ERK45a = data_KPR_ERK45a.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_ERK45a["zScore_KPR_ERK45a"] = data_KPR_ERK45a["Controller"].map(methodAvg_KPR_ERK45a)
data_KPR_ERK45a["zScore_KPR_ERK45a"] = (data_KPR_ERK45a["zScore_KPR_ERK45a"] - allAvg_KPR_ERK45a)/allStd_KPR_ERK45a

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_ERK45a["zScore_KPR_ERK45a"] < -zscore_threshold,
    data_KPR_ERK45a["zScore_KPR_ERK45a"] > zscore_threshold
]

data_KPR_ERK45a["status_KPR_ERK45a"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MERK54 (KPR) -------------------------------
data_KPR_MERK54 = df[(df["MRIMethod"] == "ARKODE_MERK54") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_MERK54) ----------------------
allAvg_KPR_MERK54 = data_KPR_MERK54["AvgRank"].mean()
allStd_KPR_MERK54 = data_KPR_MERK54["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MERK54 -----------------------
methodAvg_KPR_MERK54 = data_KPR_MERK54.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_MERK54["zScore_KPR_MERK54"] = data_KPR_MERK54["Controller"].map(methodAvg_KPR_MERK54)
data_KPR_MERK54["zScore_KPR_MERK54"] = (data_KPR_MERK54["zScore_KPR_MERK54"] - allAvg_KPR_MERK54)/allStd_KPR_MERK54

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_MERK54["zScore_KPR_MERK54"] < -zscore_threshold,
    data_KPR_MERK54["zScore_KPR_MERK54"] > zscore_threshold
]

data_KPR_MERK54["status_KPR_MERK54"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MERK43 (KPR) -------------------------------
data_KPR_MERK43 = df[(df["MRIMethod"] == "ARKODE_MERK43") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_MERK43) ----------------------
allAvg_KPR_MERK43 = data_KPR_MERK43["AvgRank"].mean()
allStd_KPR_MERK43 = data_KPR_MERK43["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MERK43 -----------------------
methodAvg_KPR_MERK43 = data_KPR_MERK43.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_MERK43["zScore_KPR_MERK43"] = data_KPR_MERK43["Controller"].map(methodAvg_KPR_MERK43)
data_KPR_MERK43["zScore_KPR_MERK43"] = (data_KPR_MERK43["zScore_KPR_MERK43"] - allAvg_KPR_MERK43)/allStd_KPR_MERK43

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_MERK43["zScore_KPR_MERK43"] < -zscore_threshold,
    data_KPR_MERK43["zScore_KPR_MERK43"] > zscore_threshold
]

data_KPR_MERK43["status_KPR_MERK43"] = np.select(conditions, status, default="intermediate")


# ----------------------------------- Store all data in one excel file with multiple sheets ---------------------------------
with pd.ExcelWriter('allOrder45_controllers.xlsx') as writer:
    data_Bruss_ESDIRK46a.to_excel(writer, sheet_name='data_Bruss_ESDIRK46a', index=False)
    data_Bruss_SR43.to_excel(writer, sheet_name='data_Bruss_SR43', index=False)
    data_Bruss_ERK45a.to_excel(writer, sheet_name='data_Bruss_ERK45a', index=False)
    data_Bruss_MERK54.to_excel(writer, sheet_name='data_Bruss_MERK54', index=False)
    data_Bruss_MERK43.to_excel(writer, sheet_name='data_Bruss_MERK43', index=False)

    data_KPR_ESDIRK46a.to_excel(writer, sheet_name='data_Bruss_ESDIRK46a', index=False)
    data_KPR_SR43.to_excel(writer, sheet_name='data_Bruss_SR43', index=False)
    data_KPR_ERK45a.to_excel(writer, sheet_name='data_Bruss_ERK45a', index=False)
    data_KPR_MERK54.to_excel(writer, sheet_name='data_Bruss_MERK54', index=False)
    data_KPR_MERK43.to_excel(writer, sheet_name='data_KPR_MERK43', index=False)



