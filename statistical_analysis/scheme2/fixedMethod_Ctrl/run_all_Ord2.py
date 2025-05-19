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
# ---------------------- Select all controllers with ARKODE_MRI_GARK_ERK22b (Brusselator) -------------------------------
data_Bruss_ERK22b = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_ERK22b") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MRI_GARK_ERK22b) ----------------------
allAvg_Bruss_ERK22b = data_Bruss_ERK22b["AvgRank"].mean()
allStd_Bruss_ERK22b = data_Bruss_ERK22b["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_ERK22b -----------------------
methodAvg_Bruss_ERK22b = data_Bruss_ERK22b.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_ERK22b["zScore_Bruss_ERK22b"] = data_Bruss_ERK22b["Controller"].map(methodAvg_Bruss_ERK22b)
data_Bruss_ERK22b["zScore_Bruss_ERK22b"] = (data_Bruss_ERK22b["zScore_Bruss_ERK22b"] - allAvg_Bruss_ERK22b)/allStd_Bruss_ERK22b

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_ERK22b["zScore_Bruss_ERK22b"] < -zscore_threshold,
    data_Bruss_ERK22b["zScore_Bruss_ERK22b"] > zscore_threshold
]

data_Bruss_ERK22b["status_Bruss_ERK22b"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_ERK22a (Brusselator) -------------------------------
data_Bruss_ERK22a = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_ERK22a") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MRI_GARK_ERK22a) ----------------------
allAvg_Bruss_ERK22a = data_Bruss_ERK22a["AvgRank"].mean()
allStd_Bruss_ERK22a = data_Bruss_ERK22a["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_ERK22a -----------------------
methodAvg_Bruss_ERK22a = data_Bruss_ERK22a.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_ERK22a["zScore_Bruss_ERK22a"] = data_Bruss_ERK22a["Controller"].map(methodAvg_Bruss_ERK22a)
data_Bruss_ERK22a["zScore_Bruss_ERK22a"] = (data_Bruss_ERK22a["zScore_Bruss_ERK22a"] - allAvg_Bruss_ERK22a)/allStd_Bruss_ERK22a

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_ERK22a["zScore_Bruss_ERK22a"] < -zscore_threshold,
    data_Bruss_ERK22a["zScore_Bruss_ERK22a"] > zscore_threshold
]

data_Bruss_ERK22a["status_Bruss_ERK22a"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_IRK21a (Brusselator) -------------------------------
data_Bruss_IRK21a = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_IRK21a") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MRI_GARK_IRK21a) ----------------------
allAvg_Bruss_IRK21a = data_Bruss_IRK21a["AvgRank"].mean()
allStd_Bruss_IRK21a = data_Bruss_IRK21a["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_IRK21a -----------------------
methodAvg_Bruss_IRK21a = data_Bruss_IRK21a.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_IRK21a["zScore_Bruss_IRK21a"] = data_Bruss_IRK21a["Controller"].map(methodAvg_Bruss_IRK21a)
data_Bruss_IRK21a["zScore_Bruss_IRK21a"] = (data_Bruss_IRK21a["zScore_Bruss_IRK21a"] - allAvg_Bruss_IRK21a)/allStd_Bruss_IRK21a

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_IRK21a["zScore_Bruss_IRK21a"] < -zscore_threshold,
    data_Bruss_IRK21a["zScore_Bruss_IRK21a"] > zscore_threshold
]

data_Bruss_IRK21a["status_Bruss_IRK21a"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_IMEX_MRI_SR21 (Brusselator) -------------------------------
data_Bruss_SR21 = df[(df["MRIMethod"] == "ARKODE_IMEX_MRI_SR21") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_IMEX_MRI_SR21) ----------------------
allAvg_Bruss_SR21 = data_Bruss_SR21["AvgRank"].mean()
allStd_Bruss_SR21 = data_Bruss_SR21["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_IMEX_MRI_SR21 -----------------------
methodAvg_Bruss_SR21 = data_Bruss_SR21.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_SR21["zScore_Bruss_SR21"] = data_Bruss_SR21["Controller"].map(methodAvg_Bruss_SR21)
data_Bruss_SR21["zScore_Bruss_SR21"] = (data_Bruss_SR21["zScore_Bruss_SR21"] - allAvg_Bruss_SR21)/allStd_Bruss_SR21

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_SR21["zScore_Bruss_SR21"] < -zscore_threshold,
    data_Bruss_SR21["zScore_Bruss_SR21"] > zscore_threshold
]

data_Bruss_SR21["status_Bruss_SR21"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_RALSTON2 (Brusselator) -------------------------------
data_Bruss_RALSTON2 = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_RALSTON2") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MRI_GARK_RALSTON2) ----------------------
allAvg_Bruss_RALSTON2 = data_Bruss_RALSTON2["AvgRank"].mean()
allStd_Bruss_RALSTON2 = data_Bruss_RALSTON2["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_RALSTON2 -----------------------
methodAvg_Bruss_RALSTON2 = data_Bruss_RALSTON2.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_RALSTON2["zScore_Bruss_RALSTON2"] = data_Bruss_RALSTON2["Controller"].map(methodAvg_Bruss_RALSTON2)
data_Bruss_RALSTON2["zScore_Bruss_RALSTON2"] = (data_Bruss_RALSTON2["zScore_Bruss_RALSTON2"] - allAvg_Bruss_RALSTON2)/allStd_Bruss_RALSTON2

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_RALSTON2["zScore_Bruss_RALSTON2"] < -zscore_threshold,
    data_Bruss_RALSTON2["zScore_Bruss_RALSTON2"] > zscore_threshold
]

data_Bruss_RALSTON2["status_Bruss_RALSTON2"] = np.select(conditions, status, default="intermediate")

#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MERK21 (Brusselator) -------------------------------
data_Bruss_MERK21 = df[(df["MRIMethod"] == "ARKODE_MERK21") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MERK21) ----------------------
allAvg_Bruss_MERK21 = data_Bruss_MERK21["AvgRank"].mean()
allStd_Bruss_MERK21 = data_Bruss_MERK21["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MERK21 -----------------------
methodAvg_Bruss_MERK21 = data_Bruss_MERK21.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_MERK21["zScore_Bruss_MERK21"] = data_Bruss_MERK21["Controller"].map(methodAvg_Bruss_MERK21)
data_Bruss_MERK21["zScore_Bruss_MERK21"] = (data_Bruss_MERK21["zScore_Bruss_MERK21"] - allAvg_Bruss_MERK21)/allStd_Bruss_MERK21

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_MERK21["zScore_Bruss_MERK21"] < -zscore_threshold,
    data_Bruss_MERK21["zScore_Bruss_MERK21"] > zscore_threshold
]

data_Bruss_MERK21["status_Bruss_MERK21"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_ERK22b (KPR) -------------------------------
data_KPR_ERK22b = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_ERK22b") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_MRI_GARK_ERK22b) ----------------------
allAvg_KPR_ERK22b = data_KPR_ERK22b["AvgRank"].mean()
allStd_KPR_ERK22b = data_KPR_ERK22b["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_ERK22b -----------------------
methodAvg_KPR_ERK22b = data_KPR_ERK22b.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_ERK22b["zScore_KPR_ERK22b"] = data_KPR_ERK22b["Controller"].map(methodAvg_KPR_ERK22b)
data_KPR_ERK22b["zScore_KPR_ERK22b"] = (data_KPR_ERK22b["zScore_KPR_ERK22b"] - allAvg_KPR_ERK22b)/allStd_KPR_ERK22b

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_ERK22b["zScore_KPR_ERK22b"] < -zscore_threshold,
    data_KPR_ERK22b["zScore_KPR_ERK22b"] > zscore_threshold
]

data_KPR_ERK22b["status_KPR_ERK22b"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_ERK22a (KPR) -------------------------------
data_KPR_ERK22a = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_ERK22a") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_MRI_GARK_ERK22a) ----------------------
allAvg_KPR_ERK22a = data_KPR_ERK22a["AvgRank"].mean()
allStd_KPR_ERK22a = data_KPR_ERK22a["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_ERK22a -----------------------
methodAvg_KPR_ERK22a = data_KPR_ERK22a.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_ERK22a["zScore_KPR_ERK22a"] = data_KPR_ERK22a["Controller"].map(methodAvg_KPR_ERK22a)
data_KPR_ERK22a["zScore_KPR_ERK22a"] = (data_KPR_ERK22a["zScore_KPR_ERK22a"] - allAvg_KPR_ERK22a)/allStd_KPR_ERK22a

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_ERK22a["zScore_KPR_ERK22a"] < -zscore_threshold,
    data_KPR_ERK22a["zScore_KPR_ERK22a"] > zscore_threshold
]

data_KPR_ERK22a["status_KPR_ERK22a"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_IRK21a (KPR) -------------------------------
data_KPR_IRK21a = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_IRK21a") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_MRI_GARK_IRK21a) ----------------------
allAvg_KPR_IRK21a = data_KPR_IRK21a["AvgRank"].mean()
allStd_KPR_IRK21a = data_KPR_IRK21a["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_IRK21a -----------------------
methodAvg_KPR_IRK21a = data_KPR_IRK21a.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_IRK21a["zScore_KPR_IRK21a"] = data_KPR_IRK21a["Controller"].map(methodAvg_KPR_IRK21a)
data_KPR_IRK21a["zScore_KPR_IRK21a"] = (data_KPR_IRK21a["zScore_KPR_IRK21a"] - allAvg_KPR_IRK21a)/allStd_KPR_IRK21a

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_IRK21a["zScore_KPR_IRK21a"] < -zscore_threshold,
    data_KPR_IRK21a["zScore_KPR_IRK21a"] > zscore_threshold
]

data_KPR_IRK21a["status_KPR_IRK21a"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_IMEX_MRI_SR21 (KPR) -------------------------------
data_KPR_SR21 = df[(df["MRIMethod"] == "ARKODE_IMEX_MRI_SR21") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_IMEX_MRI_SR21) ----------------------
allAvg_KPR_SR21 = data_KPR_SR21["AvgRank"].mean()
allStd_KPR_SR21 = data_KPR_SR21["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_IMEX_MRI_SR21 -----------------------
methodAvg_KPR_SR21 = data_KPR_SR21.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_SR21["zScore_KPR_SR21"] = data_KPR_SR21["Controller"].map(methodAvg_KPR_SR21)
data_KPR_SR21["zScore_KPR_SR21"] = (data_KPR_SR21["zScore_KPR_SR21"] - allAvg_KPR_SR21)/allStd_KPR_SR21

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_SR21["zScore_KPR_SR21"] < -zscore_threshold,
    data_KPR_SR21["zScore_KPR_SR21"] > zscore_threshold
]

data_KPR_SR21["status_KPR_SR21"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_RALSTON2 (KPR) -------------------------------
data_KPR_RALSTON2 = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_RALSTON2") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_MRI_GARK_RALSTON2) ----------------------
allAvg_KPR_RALSTON2 = data_KPR_RALSTON2["AvgRank"].mean()
allStd_KPR_RALSTON2 = data_KPR_RALSTON2["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_RALSTON2 -----------------------
methodAvg_KPR_RALSTON2 = data_KPR_RALSTON2.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_RALSTON2["zScore_KPR_RALSTON2"] = data_KPR_RALSTON2["Controller"].map(methodAvg_KPR_RALSTON2)
data_KPR_RALSTON2["zScore_KPR_RALSTON2"] = (data_KPR_RALSTON2["zScore_KPR_RALSTON2"] - allAvg_KPR_RALSTON2)/allStd_KPR_RALSTON2

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_RALSTON2["zScore_KPR_RALSTON2"] < -zscore_threshold,
    data_KPR_RALSTON2["zScore_KPR_RALSTON2"] > zscore_threshold
]

data_KPR_RALSTON2["status_KPR_RALSTON2"] = np.select(conditions, status, default="intermediate")

#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MERK21 (KPR) -------------------------------
data_KPR_MERK21 = df[(df["MRIMethod"] == "ARKODE_MERK21") & (df["Param"].isin([50, 500])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, ARKODE_MERK21) ----------------------
allAvg_KPR_MERK21 = data_KPR_MERK21["AvgRank"].mean()
allStd_KPR_MERK21 = data_KPR_MERK21["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MERK21 -----------------------
methodAvg_KPR_MERK21 = data_KPR_MERK21.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_KPR_MERK21["zScore_KPR_MERK21"] = data_KPR_MERK21["Controller"].map(methodAvg_KPR_MERK21)
data_KPR_MERK21["zScore_KPR_MERK21"] = (data_KPR_MERK21["zScore_KPR_MERK21"] - allAvg_KPR_MERK21)/allStd_KPR_MERK21

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_MERK21["zScore_KPR_MERK21"] < -zscore_threshold,
    data_KPR_MERK21["zScore_KPR_MERK21"] > zscore_threshold
]

data_KPR_MERK21["status_KPR_MERK21"] = np.select(conditions, status, default="intermediate")


# ----------------------------------- Store all data in one excel file with multiple sheets ---------------------------------
with pd.ExcelWriter('allOrder2_controllers.xlsx') as writer:
    data_Bruss_ERK22b.to_excel(writer, sheet_name='data_Bruss_ERK22b', index=False)
    data_Bruss_ERK22a.to_excel(writer, sheet_name='data_Bruss_ERK22a', index=False)
    data_Bruss_IRK21a.to_excel(writer, sheet_name='data_Bruss_IRK21a', index=False)
    data_Bruss_SR21.to_excel(writer, sheet_name='data_Bruss_SR21', index=False)
    data_Bruss_RALSTON2.to_excel(writer, sheet_name='data_Bruss_RALSTON2', index=False)
    data_Bruss_MERK21.to_excel(writer, sheet_name='data_Bruss_MERK21', index=False)
    data_KPR_ERK22b.to_excel(writer, sheet_name='data_Bruss_ERK22b', index=False)
    data_KPR_ERK22a.to_excel(writer, sheet_name='data_Bruss_ERK22a', index=False)
    data_KPR_IRK21a.to_excel(writer, sheet_name='data_Bruss_IRK21a', index=False)
    data_KPR_SR21.to_excel(writer, sheet_name='data_Bruss_SR21', index=False)
    data_KPR_RALSTON2.to_excel(writer, sheet_name='data_Bruss_RALSTON2', index=False)
    data_KPR_MERK21.to_excel(writer, sheet_name='data_Bruss_MERK21', index=False)



