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
data_Bruss_ERK22b["zScore"] = data_Bruss_ERK22b["Controller"].map(methodAvg_Bruss_ERK22b)
data_Bruss_ERK22b["zScore"] = (data_Bruss_ERK22b["zScore"] - allAvg_Bruss_ERK22b)/allStd_Bruss_ERK22b

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_ERK22b["zScore"] < -zscore_threshold,
    data_Bruss_ERK22b["zScore"] > zscore_threshold
]

data_Bruss_ERK22b["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_ERK22a (Brusselator) -------------------------------
data_Bruss_ERK22a = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_ERK22a") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MRI_GARK_ERK22a) ----------------------
allAvg_Bruss_ERK22a = data_Bruss_ERK22a["AvgRank"].mean()
allStd_Bruss_ERK22a = data_Bruss_ERK22a["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_ERK22a -----------------------
methodAvg_Bruss_ERK22a = data_Bruss_ERK22a.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_ERK22a["zScore"] = data_Bruss_ERK22a["Controller"].map(methodAvg_Bruss_ERK22a)
data_Bruss_ERK22a["zScore"] = (data_Bruss_ERK22a["zScore"] - allAvg_Bruss_ERK22a)/allStd_Bruss_ERK22a

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_ERK22a["zScore"] < -zscore_threshold,
    data_Bruss_ERK22a["zScore"] > zscore_threshold
]

data_Bruss_ERK22a["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_IRK21a (Brusselator) -------------------------------
data_Bruss_IRK21a = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_IRK21a") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MRI_GARK_IRK21a) ----------------------
allAvg_Bruss_IRK21a = data_Bruss_IRK21a["AvgRank"].mean()
allStd_Bruss_IRK21a = data_Bruss_IRK21a["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_IRK21a -----------------------
methodAvg_Bruss_IRK21a = data_Bruss_IRK21a.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_IRK21a["zScore"] = data_Bruss_IRK21a["Controller"].map(methodAvg_Bruss_IRK21a)
data_Bruss_IRK21a["zScore"] = (data_Bruss_IRK21a["zScore"] - allAvg_Bruss_IRK21a)/allStd_Bruss_IRK21a

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_IRK21a["zScore"] < -zscore_threshold,
    data_Bruss_IRK21a["zScore"] > zscore_threshold
]

data_Bruss_IRK21a["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_IMEX_MRI_SR21 (Brusselator) -------------------------------
data_Bruss_SR21 = df[(df["MRIMethod"] == "ARKODE_IMEX_MRI_SR21") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_IMEX_MRI_SR21) ----------------------
allAvg_Bruss_SR21 = data_Bruss_SR21["AvgRank"].mean()
allStd_Bruss_SR21 = data_Bruss_SR21["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_IMEX_MRI_SR21 -----------------------
methodAvg_Bruss_SR21 = data_Bruss_SR21.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_SR21["zScore"] = data_Bruss_SR21["Controller"].map(methodAvg_Bruss_SR21)
data_Bruss_SR21["zScore"] = (data_Bruss_SR21["zScore"] - allAvg_Bruss_SR21)/allStd_Bruss_SR21

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_SR21["zScore"] < -zscore_threshold,
    data_Bruss_SR21["zScore"] > zscore_threshold
]

data_Bruss_SR21["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MRI_GARK_RALSTON2 (Brusselator) -------------------------------
data_Bruss_RALSTON2 = df[(df["MRIMethod"] == "ARKODE_MRI_GARK_RALSTON2") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MRI_GARK_RALSTON2) ----------------------
allAvg_Bruss_RALSTON2 = data_Bruss_RALSTON2["AvgRank"].mean()
allStd_Bruss_RALSTON2 = data_Bruss_RALSTON2["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MRI_GARK_RALSTON2 -----------------------
methodAvg_Bruss_RALSTON2 = data_Bruss_RALSTON2.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_RALSTON2["zScore"] = data_Bruss_RALSTON2["Controller"].map(methodAvg_Bruss_RALSTON2)
data_Bruss_RALSTON2["zScore"] = (data_Bruss_RALSTON2["zScore"] - allAvg_Bruss_RALSTON2)/allStd_Bruss_RALSTON2

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_RALSTON2["zScore"] < -zscore_threshold,
    data_Bruss_RALSTON2["zScore"] > zscore_threshold
]

data_Bruss_RALSTON2["status"] = np.select(conditions, status, default="intermediate")

#######################################################################################################################
# ---------------------- Select all controllers with ARKODE_MERK21 (Brusselator) -------------------------------
data_Bruss_MERK21 = df[(df["MRIMethod"] == "ARKODE_MERK21") & (df["Param"].isin([0.0001, 0.00001])) & (~df['Controller'].isin(controllers_to_remove))][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, ARKODE_MERK21) ----------------------
allAvg_Bruss_MERK21 = data_Bruss_MERK21["AvgRank"].mean()
allStd_Bruss_MERK21 = data_Bruss_MERK21["AvgRank"].std()

# --------------- Mean of each controller for ARKODE_MERK21 -----------------------
methodAvg_Bruss_MERK21 = data_Bruss_MERK21.groupby("Controller")["AvgRank"].mean()

# ------------- Calculate the z-score of each controller and store on each row corresponding to the controller -----------------
data_Bruss_MERK21["zScore"] = data_Bruss_MERK21["Controller"].map(methodAvg_Bruss_MERK21)
data_Bruss_MERK21["zScore"] = (data_Bruss_MERK21["zScore"] - allAvg_Bruss_MERK21)/allStd_Bruss_MERK21

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_MERK21["zScore"] < -zscore_threshold,
    data_Bruss_MERK21["zScore"] > zscore_threshold
]

data_Bruss_MERK21["status"] = np.select(conditions, status, default="intermediate")


# ----------------------------------- Store all data in one excel file with multiple sheets ---------------------------------
with pd.ExcelWriter('allOrder2_BrussControllers.xlsx') as writer:
    data_Bruss_ERK22b.to_excel(writer, sheet_name='data_Bruss_ERK22b', index=False)
    data_Bruss_ERK22a.to_excel(writer, sheet_name='data_Bruss_ERK22a', index=False)
    data_Bruss_IRK21a.to_excel(writer, sheet_name='data_Bruss_IRK21a', index=False)
    data_Bruss_SR21.to_excel(writer, sheet_name='data_Bruss_SR21', index=False)
    data_Bruss_RALSTON2.to_excel(writer, sheet_name='data_Bruss_RALSTON2', index=False)
    data_Bruss_MERK21.to_excel(writer, sheet_name='data_Bruss_MERK21', index=False)


###############################################################################################################################
# --------------------------------------- Compute the Average z-score of Each Controller ------------------------------------------
# load excel file
filename = "allOrder2_BrussControllers.xlsx"

# load the sheetnames
xls = pd.ExcelFile(filename)
sheetNames = xls.sheet_names

MRIHTol_I_zscores     = []
MRIDec_I_zscores      = []
MRIHTol_H0321_zscores = []
MRIDec_H0321_zscores  = []
MRIHTol_H211_zscores  = []
MRIDec_H211_zscores   = []
MRIHTol_H0211_zscores = []
MRIDec_H0211_zscores  = []
MRIHTol_H312_zscores  = []
MRIDec_H312_zscores   = []

for sheet in sheetNames:
    df = pd.read_excel(filename, sheet_name=sheet)

    ###########################################################################
    # Filter rows where Controller is MRIHTol-I
    MRIHTol_I_values = df[df["Controller"] == "MRIHTol-I"]

    # since the zscore values are the same just pick one
    valueMRIHTol_I  = MRIHTol_I_values["zScore"].iloc[0]
    MRIHTol_I_zscores.append(valueMRIHTol_I)

    ###########################################################################
    # Filter rows where Controller is MRIDec-I
    MRIDec_I_values = df[df["Controller"] == "MRIDec-I"]

    # since the zscore values are the same just pick one
    valueMRIDec_I  = MRIDec_I_values["zScore"].iloc[0]
    MRIDec_I_zscores.append(valueMRIDec_I)

   ###########################################################################
    # Filter rows where Controller is MRIHTol-H0321
    MRIHTol_H0321_values = df[df["Controller"] == "MRIHTol-H0321"]

    # since the zscore values are the same just pick one
    valueMRIHTol_H0321 = MRIHTol_H0321_values["zScore"].iloc[0]
    MRIHTol_H0321_zscores.append(valueMRIHTol_H0321)

    ###########################################################################
    # Filter rows where Controller is MRIDec-H0321
    MRIDec_H0321_values = df[df["Controller"] == "MRIDec-H0321"]

    # since the zscore values are the same just pick one
    valueMRIDec_H0321 = MRIDec_H0321_values["zScore"].iloc[0]
    MRIDec_H0321_zscores.append(valueMRIDec_H0321)

    ###########################################################################
    # Filter rows where Controller is MRIHTol-H211
    MRIHTol_H211_values = df[df["Controller"] == "MRIHTol-H211"]

    # since the zscore values are the same just pick one
    valueMRIHTol_H211 = MRIHTol_H211_values["zScore"].iloc[0]
    MRIHTol_H211_zscores.append(valueMRIHTol_H211)

    ###########################################################################
    # Filter rows where Controller is MRIDec-H211
    MRIDec_H211_values = df[df["Controller"] == "MRIDec-H211"]

    # since the zscore values are the same just pick one
    valueMRIDec_H211 = MRIDec_H211_values["zScore"].iloc[0]
    MRIDec_H211_zscores.append(valueMRIDec_H211)

    ###########################################################################
    # Filter rows where Controller is MRIHTol-H0211
    MRIHTol_H0211_values = df[df["Controller"] == "MRIHTol-H0211"]

    # since the zscore values are the same just pick one
    valueMRIHTol_H0211 = MRIHTol_H0211_values["zScore"].iloc[0]
    MRIHTol_H0211_zscores.append(valueMRIHTol_H0211)

    ###########################################################################
    # Filter rows where Controller is MRIDec-H0211
    MRIDec_H0211_values = df[df["Controller"] == "MRIDec-H0211"]

    # since the zscore values are the same just pick one
    valueMRIDec_H0211 = MRIDec_H0211_values["zScore"].iloc[0]
    MRIDec_H0211_zscores.append(valueMRIDec_H0211)

    ###########################################################################
    # Filter rows where Controller is MRIHTol-H312
    MRIHTol_H312_values = df[df["Controller"] == "MRIHTol-H312"]

    # since the zscore values are the same just pick one
    valueMRIHTol_H312 = MRIHTol_H312_values["zScore"].iloc[0]
    MRIHTol_H312_zscores.append(valueMRIHTol_H312)

    ###########################################################################
    # Filter rows where Controller is MRIDec-H312
    MRIDec_H312_values = df[df["Controller"] == "MRIDec-H312"]

    # since the zscore values are the same just pick one
    valueMRIDec_H312 = MRIDec_H312_values["zScore"].iloc[0]
    MRIDec_H312_zscores.append(valueMRIDec_H312)


# compute the average zscores
with open("AvgZscores_Bruss_Ord2.txt", "w") as file:
    average_MRIHTol_I = sum(MRIHTol_I_zscores) / len(MRIHTol_I_zscores)
    file.write(f"Average zscore for MRIHTol-I (Brusselator, 2nd Order): {average_MRIHTol_I}\n\n")

    average_MRIDec_I = sum(MRIDec_I_zscores) / len(MRIDec_I_zscores)
    file.write(f"Average zscore for MRIDec-I (Brusselator, 2nd Order): {average_MRIDec_I}\n\n")

    average_MRIHTol_H0321 = sum(MRIHTol_H0321_zscores) / len(MRIHTol_H0321_zscores)
    file.write(f"Average zscore for MRIHTol-H0321 (Brusselator, 2nd Order): {average_MRIHTol_H0321}\n\n")

    average_MRIDec_H0321 = sum(MRIDec_H0321_zscores) / len(MRIDec_H0321_zscores)
    file.write(f"Average zscore for MRIDec-H0321 (Brusselator, 2nd Order): {average_MRIDec_H0321}\n\n")

    average_MRIHTol_H211 = sum(MRIHTol_H211_zscores) / len(MRIHTol_H211_zscores)
    file.write(f"Average zscore for MRIHTol-H211 (Brusselator, 2nd Order): {average_MRIHTol_H211}\n\n")

    average_MRIDec_H211 = sum(MRIDec_H211_zscores) / len(MRIDec_H211_zscores)
    file.write(f"Average zscore for MRIDec-H211 (Brusselator, 2nd Order): {average_MRIDec_H211}\n\n")

    average_MRIHTol_H0211 = sum(MRIHTol_H0211_zscores) / len(MRIHTol_H0211_zscores)
    file.write(f"Average zscore for MRIHTol-H0211 (Brusselator, 2nd Order): {average_MRIHTol_H0211}\n\n")

    average_MRIDec_H0211 = sum(MRIDec_H0211_zscores) / len(MRIDec_H0211_zscores)
    file.write(f"Average zscore for MRIDec-H0211 (Brusselator, 2nd Order): {average_MRIDec_H0211}\n\n")

    average_MRIHTol_H312 = sum(MRIHTol_H312_zscores) / len(MRIHTol_H312_zscores)
    file.write(f"Average zscore for MRIHTol-H312 (Brusselator, 2nd Order): {average_MRIHTol_H312}\n\n")

    average_MRIDec_H312 = sum(MRIDec_H312_zscores) / len(MRIDec_H312_zscores)
    file.write(f"Average zscore for MRIDec-H312 (Brusselator, 2nd Order): {average_MRIDec_H312}\n\n")








