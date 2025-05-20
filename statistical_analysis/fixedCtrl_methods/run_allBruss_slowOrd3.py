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
# ---------------------- Select only slow 3rd order methods with MRIHTol-I controller (Brusselator) -------------------------------
data_Bruss_slowOrd3_HTol_I = df[(df["order"] == 3) & (df["metric"] == "slow") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIHTol-I")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, slow, Order 3, MRIHTol-I) ----------------------
allAvg_Bruss_slowOrd3_HTol_I = data_Bruss_slowOrd3_HTol_I["AvgRank"].mean()
allStd_Bruss_slowOrd3_HTol_I = data_Bruss_slowOrd3_HTol_I["AvgRank"].std()

# --------------- Mean of each slow 3rd order method across all controllers -----------------------
methodAvg_Bruss_slowOrd3_HTol_I = data_Bruss_slowOrd3_HTol_I.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_slowOrd3_HTol_I["zScore"] = data_Bruss_slowOrd3_HTol_I["MRIMethod"].map(methodAvg_Bruss_slowOrd3_HTol_I)
data_Bruss_slowOrd3_HTol_I["zScore"] = (data_Bruss_slowOrd3_HTol_I["zScore"] - allAvg_Bruss_slowOrd3_HTol_I)/allStd_Bruss_slowOrd3_HTol_I 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_slowOrd3_HTol_I["zScore"] < -zscore_threshold,
    data_Bruss_slowOrd3_HTol_I["zScore"] > zscore_threshold
]

data_Bruss_slowOrd3_HTol_I["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 3rd order methods with MRIDec-I controller (Brusselator) -------------------------------
data_Bruss_slowOrd3_Dec_I = df[(df["order"] == 3) & (df["metric"] == "slow") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIDec-I")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, slow, Order 3, MRIDec-I) ----------------------
allAvg_Bruss_slowOrd3_Dec_I = data_Bruss_slowOrd3_Dec_I["AvgRank"].mean()
allStd_Bruss_slowOrd3_Dec_I = data_Bruss_slowOrd3_Dec_I["AvgRank"].std()

# --------------- Mean of each slow 3rd order method across all controllers -----------------------
methodAvg_Bruss_slowOrd3_Dec_I = data_Bruss_slowOrd3_Dec_I.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_slowOrd3_Dec_I["zScore"] = data_Bruss_slowOrd3_Dec_I["MRIMethod"].map(methodAvg_Bruss_slowOrd3_Dec_I)
data_Bruss_slowOrd3_Dec_I["zScore"] = (data_Bruss_slowOrd3_Dec_I["zScore"] - allAvg_Bruss_slowOrd3_Dec_I)/allStd_Bruss_slowOrd3_Dec_I 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_slowOrd3_Dec_I["zScore"] < -zscore_threshold,
    data_Bruss_slowOrd3_Dec_I["zScore"] > zscore_threshold
]

data_Bruss_slowOrd3_Dec_I["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 3rd order methods with MRIHTol-H0321 controller (Brusselator) -------------------------------
data_Bruss_slowOrd3_HTol_H0321 = df[(df["order"] == 3) & (df["metric"] == "slow") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIHTol-H0321")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, slow, Order 3, MRIHTol-H0321) ----------------------
allAvg_Bruss_slowOrd3_HTol_H0321 = data_Bruss_slowOrd3_HTol_H0321["AvgRank"].mean()
allStd_Bruss_slowOrd3_HTol_H0321= data_Bruss_slowOrd3_HTol_H0321["AvgRank"].std()

# --------------- Mean of each slow 3rd order method across all controllers -----------------------
methodAvg_Bruss_slowOrd3_HTol_H0321 = data_Bruss_slowOrd3_HTol_H0321.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_slowOrd3_HTol_H0321["zScore"] = data_Bruss_slowOrd3_HTol_H0321["MRIMethod"].map(methodAvg_Bruss_slowOrd3_HTol_H0321)
data_Bruss_slowOrd3_HTol_H0321["zScore"] = (data_Bruss_slowOrd3_HTol_H0321["zScore"] - allAvg_Bruss_slowOrd3_HTol_H0321)/allStd_Bruss_slowOrd3_HTol_H0321 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_slowOrd3_HTol_H0321["zScore"] < -zscore_threshold,
    data_Bruss_slowOrd3_HTol_H0321["zScore"] > zscore_threshold
]

data_Bruss_slowOrd3_HTol_H0321["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 3rd order methods with MRIDec-H0321 controller (Brusselator) -------------------------------
data_Bruss_slowOrd3_Dec_H0321 = df[(df["order"] == 3) & (df["metric"] == "slow") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIDec-H0321")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, slow, Order 3, MRIDec-H0321) ----------------------
allAvg_Bruss_slowOrd3_Dec_H0321 = data_Bruss_slowOrd3_Dec_H0321["AvgRank"].mean()
allStd_Bruss_slowOrd3_Dec_H0321= data_Bruss_slowOrd3_Dec_H0321["AvgRank"].std()

# --------------- Mean of each slow 3rd order method across all controllers -----------------------
methodAvg_Bruss_slowOrd3_Dec_H0321 = data_Bruss_slowOrd3_Dec_H0321.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_slowOrd3_Dec_H0321["zScore"] = data_Bruss_slowOrd3_Dec_H0321["MRIMethod"].map(methodAvg_Bruss_slowOrd3_Dec_H0321)
data_Bruss_slowOrd3_Dec_H0321["zScore"] = (data_Bruss_slowOrd3_Dec_H0321["zScore"] - allAvg_Bruss_slowOrd3_Dec_H0321)/allStd_Bruss_slowOrd3_Dec_H0321 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_slowOrd3_Dec_H0321["zScore"] < -zscore_threshold,
    data_Bruss_slowOrd3_Dec_H0321["zScore"] > zscore_threshold
]

data_Bruss_slowOrd3_Dec_H0321["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 3rd order methods with MRIHTol-H211 controller (Brusselator) -------------------------------
data_Bruss_slowOrd3_HTol_H211 = df[(df["order"] == 3) & (df["metric"] == "slow") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIHTol-H211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, slow, Order 3, MRIHTol-H211) ----------------------
allAvg_Bruss_slowOrd3_HTol_H211 = data_Bruss_slowOrd3_HTol_H211["AvgRank"].mean()
allStd_Bruss_slowOrd3_HTol_H211 = data_Bruss_slowOrd3_HTol_H211["AvgRank"].std()

# --------------- Mean of each slow 3rd order method across all controllers -----------------------
methodAvg_Bruss_slowOrd3_HTol_H211 = data_Bruss_slowOrd3_HTol_H211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_slowOrd3_HTol_H211["zScore"] = data_Bruss_slowOrd3_HTol_H211["MRIMethod"].map(methodAvg_Bruss_slowOrd3_HTol_H211)
data_Bruss_slowOrd3_HTol_H211["zScore"] = (data_Bruss_slowOrd3_HTol_H211["zScore"] - allAvg_Bruss_slowOrd3_HTol_H211)/allStd_Bruss_slowOrd3_HTol_H211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_slowOrd3_HTol_H211["zScore"] < -zscore_threshold,
    data_Bruss_slowOrd3_HTol_H211["zScore"] > zscore_threshold
]

data_Bruss_slowOrd3_HTol_H211["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 3rd order methods with MRIDec-H211 controller (Brusselator) -------------------------------
data_Bruss_slowOrd3_Dec_H211 = df[(df["order"] == 3) & (df["metric"] == "slow") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIDec-H211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, slow, Order 3, MRIDec-H211) ----------------------
allAvg_Bruss_slowOrd3_Dec_H211 = data_Bruss_slowOrd3_Dec_H211["AvgRank"].mean()
allStd_Bruss_slowOrd3_Dec_H211= data_Bruss_slowOrd3_Dec_H211["AvgRank"].std()

# --------------- Mean of each slow 3rd order method across all controllers -----------------------
methodAvg_Bruss_slowOrd3_Dec_H211 = data_Bruss_slowOrd3_Dec_H211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_slowOrd3_Dec_H211["zScore"] = data_Bruss_slowOrd3_Dec_H211["MRIMethod"].map(methodAvg_Bruss_slowOrd3_Dec_H211)
data_Bruss_slowOrd3_Dec_H211["zScore"] = (data_Bruss_slowOrd3_Dec_H211["zScore"] - allAvg_Bruss_slowOrd3_Dec_H211)/allStd_Bruss_slowOrd3_Dec_H211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_slowOrd3_Dec_H211["zScore"] < -zscore_threshold,
    data_Bruss_slowOrd3_Dec_H211["zScore"] > zscore_threshold
]

data_Bruss_slowOrd3_Dec_H211["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 3rd order methods with MRIHTol-H0211 controller (Brusselator) -------------------------------
data_Bruss_slowOrd3_HTol_H0211 = df[(df["order"] == 3) & (df["metric"] == "slow") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIHTol-H0211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, slow, Order 3, MRIHTol-H0211) ----------------------
allAvg_Bruss_slowOrd3_HTol_H0211 = data_Bruss_slowOrd3_HTol_H0211["AvgRank"].mean()
allStd_Bruss_slowOrd3_HTol_H0211 = data_Bruss_slowOrd3_HTol_H0211["AvgRank"].std()

# --------------- Mean of each slow 3rd order method across all controllers -----------------------
methodAvg_Bruss_slowOrd3_HTol_H0211 = data_Bruss_slowOrd3_HTol_H0211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_slowOrd3_HTol_H0211["zScore"] = data_Bruss_slowOrd3_HTol_H0211["MRIMethod"].map(methodAvg_Bruss_slowOrd3_HTol_H0211)
data_Bruss_slowOrd3_HTol_H0211["zScore"] = (data_Bruss_slowOrd3_HTol_H0211["zScore"] - allAvg_Bruss_slowOrd3_HTol_H0211)/allStd_Bruss_slowOrd3_HTol_H0211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_slowOrd3_HTol_H0211["zScore"] < -zscore_threshold,
    data_Bruss_slowOrd3_HTol_H0211["zScore"] > zscore_threshold
]

data_Bruss_slowOrd3_HTol_H0211["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 3rd order methods with MRIDec-H0211 controller (Brusselator) -------------------------------
data_Bruss_slowOrd3_Dec_H0211 = df[(df["order"] == 3) & (df["metric"] == "slow") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIDec-H0211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, slow, Order 3, MRIDec-H0211) ----------------------
allAvg_Bruss_slowOrd3_Dec_H0211 = data_Bruss_slowOrd3_Dec_H0211["AvgRank"].mean()
allStd_Bruss_slowOrd3_Dec_H0211= data_Bruss_slowOrd3_Dec_H0211["AvgRank"].std()

# --------------- Mean of each slow 3rd order method across all controllers -----------------------
methodAvg_Bruss_slowOrd3_Dec_H0211 = data_Bruss_slowOrd3_Dec_H0211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_slowOrd3_Dec_H0211["zScore"] = data_Bruss_slowOrd3_Dec_H0211["MRIMethod"].map(methodAvg_Bruss_slowOrd3_Dec_H0211)
data_Bruss_slowOrd3_Dec_H0211["zScore"] = (data_Bruss_slowOrd3_Dec_H0211["zScore"] - allAvg_Bruss_slowOrd3_Dec_H0211)/allStd_Bruss_slowOrd3_Dec_H0211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_slowOrd3_Dec_H0211["zScore"] < -zscore_threshold,
    data_Bruss_slowOrd3_Dec_H0211["zScore"] > zscore_threshold
]

data_Bruss_slowOrd3_Dec_H0211["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 3rd order methods with MRIHTol-H312 controller (Brusselator) -------------------------------
data_Bruss_slowOrd3_HTol_H312 = df[(df["order"] == 3) & (df["metric"] == "slow") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIHTol-H312")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, slow, Order 3, MRIHTol-H312) ----------------------
allAvg_Bruss_slowOrd3_HTol_H312 = data_Bruss_slowOrd3_HTol_H312["AvgRank"].mean()
allStd_Bruss_slowOrd3_HTol_H312 = data_Bruss_slowOrd3_HTol_H312["AvgRank"].std()

# --------------- Mean of each slow 3rd order method across all controllers -----------------------
methodAvg_Bruss_slowOrd3_HTol_H312 = data_Bruss_slowOrd3_HTol_H312.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_slowOrd3_HTol_H312["zScore"] = data_Bruss_slowOrd3_HTol_H312["MRIMethod"].map(methodAvg_Bruss_slowOrd3_HTol_H312)
data_Bruss_slowOrd3_HTol_H312["zScore"] = (data_Bruss_slowOrd3_HTol_H312["zScore"] - allAvg_Bruss_slowOrd3_HTol_H312)/allStd_Bruss_slowOrd3_HTol_H312 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_slowOrd3_HTol_H312["zScore"] < -zscore_threshold,
    data_Bruss_slowOrd3_HTol_H312["zScore"] > zscore_threshold
]

data_Bruss_slowOrd3_HTol_H312["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 3rd order methods with MRIDec-H312 controller (Brusselator) -------------------------------
data_Bruss_slowOrd3_Dec_H312 = df[(df["order"] == 3) & (df["metric"] == "slow") & (df["Param"].isin([0.0001, 0.00001])) & (df["Controller"] == "MRIDec-H312")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (Brusselator, slow, Order 3, MRIDec-H312) ----------------------
allAvg_Bruss_slowOrd3_Dec_H312 = data_Bruss_slowOrd3_Dec_H312["AvgRank"].mean()
allStd_Bruss_slowOrd3_Dec_H312= data_Bruss_slowOrd3_Dec_H312["AvgRank"].std()

# --------------- Mean of each slow 3rd order method across all controllers -----------------------
methodAvg_Bruss_slowOrd3_Dec_H312 = data_Bruss_slowOrd3_Dec_H312.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_Bruss_slowOrd3_Dec_H312["zScore"] = data_Bruss_slowOrd3_Dec_H312["MRIMethod"].map(methodAvg_Bruss_slowOrd3_Dec_H312)
data_Bruss_slowOrd3_Dec_H312["zScore"] = (data_Bruss_slowOrd3_Dec_H312["zScore"] - allAvg_Bruss_slowOrd3_Dec_H312)/allStd_Bruss_slowOrd3_Dec_H312 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_Bruss_slowOrd3_Dec_H312["zScore"] < -zscore_threshold,
    data_Bruss_slowOrd3_Dec_H312["zScore"] > zscore_threshold
]

data_Bruss_slowOrd3_Dec_H312["status"] = np.select(conditions, status, default="intermediate")


# ----------------------------------- Store all data in one excel file with multiple sheets ---------------------------------
with pd.ExcelWriter('allBruss_slowOrder3.xlsx') as writer:
    data_Bruss_slowOrd3_HTol_I.to_excel(writer, sheet_name='data_Bruss_slowOrd3_HTol_I', index=False)
    data_Bruss_slowOrd3_Dec_I.to_excel(writer, sheet_name='data_Bruss_slowOrd3_Dec_I', index=False)

    data_Bruss_slowOrd3_HTol_H0321.to_excel(writer, sheet_name='data_Bruss_slowOrd3_HTol_H0321', index=False)
    data_Bruss_slowOrd3_Dec_H0321.to_excel(writer, sheet_name='data_Bruss_slowOrd3_Dec_H0321', index=False)

    data_Bruss_slowOrd3_HTol_H211.to_excel(writer, sheet_name='data_Bruss_slowOrd3_HTol_H211', index=False)
    data_Bruss_slowOrd3_Dec_H211.to_excel(writer, sheet_name='data_Bruss_slowOrd3_Dec_H211', index=False)

    data_Bruss_slowOrd3_HTol_H0211.to_excel(writer, sheet_name='data_Bruss_slowOrd3_HTol_H0211', index=False)
    data_Bruss_slowOrd3_Dec_H0211.to_excel(writer, sheet_name='data_Bruss_slowOrd3_Dec_H0211', index=False)

    data_Bruss_slowOrd3_HTol_H312.to_excel(writer, sheet_name='data_Bruss_slowOrd3_HTol_H312', index=False)
    data_Bruss_slowOrd3_Dec_H312.to_excel(writer, sheet_name='data_Bruss_slowOrd3_Dec_H312', index=False)



###############################################################################################################################
# --------------------------------------- Compute the Average z-score of Each Method ------------------------------------------
# load excel file
filename = "allBruss_slowOrder3.xlsx"

# load the sheetnames
xls = pd.ExcelFile(filename)
sheetNames = xls.sheet_names

# store the zsores of each method across the different controllers
ERK33a_zscores    = []
ESDIRK34a_zscores = []
MERK32_zscores    = []
SR32_zscores      = []

for sheet in sheetNames:
    df = pd.read_excel(filename, sheet_name=sheet)

    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_MRI_GARK_ERK33a
    ERK33a_values = df[df["MRIMethod"] == "ARKODE_MRI_GARK_ERK33a"]

    # since the zscore values are the same just pick one
    valueERK33a   = ERK33a_values["zScore"].iloc[0]
    ERK33a_zscores.append(valueERK33a)

    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_MRI_GARK_ESDIRK34a
    ESDIRK34a_values = df[df["MRIMethod"] == "ARKODE_MRI_GARK_ESDIRK34a"]

    # since the zscore values are the same just pick one
    valueESDIRK34a  = ESDIRK34a_values["zScore"].iloc[0]
    ESDIRK34a_zscores.append(valueESDIRK34a)

    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_MERK32
    MERK32_values = df[df["MRIMethod"] == "ARKODE_MERK32"]

    # since the zscore values are the same just pick one
    valueMERK32 = MERK32_values["zScore"].iloc[0]
    MERK32_zscores.append(valueMERK32)

    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_IMEX_MRI_SR32
    SR32_values = df[df["MRIMethod"] == "ARKODE_IMEX_MRI_SR32"]

    # since the zscore values are the same just pick one
    valueSR32 = SR32_values["zScore"].iloc[0]
    SR32_zscores.append(valueSR32)


# compute the average zscores
with open("AvgZscores_Bruss_slowOrd3.txt", "w") as file:
    average_ERK33a = sum(ERK33a_zscores) / len(ERK33a_zscores)
    file.write(f"Average zscore for ARKODE_MRI_GARK_ERK33a (slow Brusselator): {average_ERK33a}\n\n")

    average_ESDIRK34a = sum(ESDIRK34a_zscores) / len(ESDIRK34a_zscores)
    file.write(f"Average zscore for ARKODE_MRI_GARK_ESDIRK34a (slow Brusselator): {average_ESDIRK34a}\n\n")

    average_MERK32 = sum(MERK32_zscores) / len(MERK32_zscores)
    file.write(f"Average zscore for ARKODE_MERK32 (slow Brusselator): {average_MERK32}\n\n")

    average_SR32  = sum(SR32_zscores) / len(SR32_zscores)
    file.write(f"Average zscore for ARKODE_IMEX_MRI_SR32 (slow Brusselator): {average_SR32}\n\n")


