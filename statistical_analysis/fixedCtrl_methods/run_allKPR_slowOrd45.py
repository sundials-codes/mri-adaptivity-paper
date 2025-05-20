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
# ---------------------- Select only slow 4th and 5th order methods with MRIHTol-I controller (KPR) -------------------------------
data_KPR_slowOrd45_HTol_I = df[(df["order"].isin([4, 5])) & (df["metric"] == "slow") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIHTol-I")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, slow, Order 4 and 5, MRIHTol-I) ----------------------
allAvg_KPR_slowOrd45_HTol_I = data_KPR_slowOrd45_HTol_I["AvgRank"].mean()
allStd_KPR_slowOrd45_HTol_I = data_KPR_slowOrd45_HTol_I["AvgRank"].std()

# --------------- Mean of each slow 4th and 5th order method across all controllers -----------------------
methodAvg_KPR_slowOrd45_HTol_I = data_KPR_slowOrd45_HTol_I.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_slowOrd45_HTol_I["zScore"] = data_KPR_slowOrd45_HTol_I["MRIMethod"].map(methodAvg_KPR_slowOrd45_HTol_I)
data_KPR_slowOrd45_HTol_I["zScore"] = (data_KPR_slowOrd45_HTol_I["zScore"] - allAvg_KPR_slowOrd45_HTol_I)/allStd_KPR_slowOrd45_HTol_I 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_slowOrd45_HTol_I["zScore"] < -zscore_threshold,
    data_KPR_slowOrd45_HTol_I["zScore"] > zscore_threshold
]

data_KPR_slowOrd45_HTol_I["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 4th and 5th order methods with MRIDec-I controller (KPR) -------------------------------
data_KPR_slowOrd45_Dec_I = df[(df["order"].isin([4, 5])) & (df["metric"] == "slow") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIDec-I")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, slow, Order 4 and 5, MRIDec-I) ----------------------
allAvg_KPR_slowOrd45_Dec_I = data_KPR_slowOrd45_Dec_I["AvgRank"].mean()
allStd_KPR_slowOrd45_Dec_I = data_KPR_slowOrd45_Dec_I["AvgRank"].std()

# --------------- Mean of each slow 4th and 5th order method across all controllers -----------------------
methodAvg_KPR_slowOrd45_Dec_I = data_KPR_slowOrd45_Dec_I.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_slowOrd45_Dec_I["zScore"] = data_KPR_slowOrd45_Dec_I["MRIMethod"].map(methodAvg_KPR_slowOrd45_Dec_I)
data_KPR_slowOrd45_Dec_I["zScore"] = (data_KPR_slowOrd45_Dec_I["zScore"] - allAvg_KPR_slowOrd45_Dec_I)/allStd_KPR_slowOrd45_Dec_I 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_slowOrd45_Dec_I["zScore"] < -zscore_threshold,
    data_KPR_slowOrd45_Dec_I["zScore"] > zscore_threshold
]

data_KPR_slowOrd45_Dec_I["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 4th and 5th order methods with MRIHTol-H0321 controller (KPR) -------------------------------
data_KPR_slowOrd45_HTol_H0321 = df[(df["order"].isin([4, 5])) & (df["metric"] == "slow") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIHTol-H0321")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, slow, Order 4 and 5, MRIHTol-H0321) ----------------------
allAvg_KPR_slowOrd45_HTol_H0321 = data_KPR_slowOrd45_HTol_H0321["AvgRank"].mean()
allStd_KPR_slowOrd45_HTol_H0321= data_KPR_slowOrd45_HTol_H0321["AvgRank"].std()

# --------------- Mean of each slow 4th and 5th order method across all controllers -----------------------
methodAvg_KPR_slowOrd45_HTol_H0321 = data_KPR_slowOrd45_HTol_H0321.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_slowOrd45_HTol_H0321["zScore"] = data_KPR_slowOrd45_HTol_H0321["MRIMethod"].map(methodAvg_KPR_slowOrd45_HTol_H0321)
data_KPR_slowOrd45_HTol_H0321["zScore"] = (data_KPR_slowOrd45_HTol_H0321["zScore"] - allAvg_KPR_slowOrd45_HTol_H0321)/allStd_KPR_slowOrd45_HTol_H0321 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_slowOrd45_HTol_H0321["zScore"] < -zscore_threshold,
    data_KPR_slowOrd45_HTol_H0321["zScore"] > zscore_threshold
]

data_KPR_slowOrd45_HTol_H0321["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 4th and 5th order methods with MRIDec-H0321 controller (KPR) -------------------------------
data_KPR_slowOrd45_Dec_H0321 = df[(df["order"].isin([4, 5])) & (df["metric"] == "slow") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIDec-H0321")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, slow, Order 4 and 5, MRIDec-H0321) ----------------------
allAvg_KPR_slowOrd45_Dec_H0321 = data_KPR_slowOrd45_Dec_H0321["AvgRank"].mean()
allStd_KPR_slowOrd45_Dec_H0321= data_KPR_slowOrd45_Dec_H0321["AvgRank"].std()

# --------------- Mean of each slow 4th and 5th order method across all controllers -----------------------
methodAvg_KPR_slowOrd45_Dec_H0321 = data_KPR_slowOrd45_Dec_H0321.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_slowOrd45_Dec_H0321["zScore"] = data_KPR_slowOrd45_Dec_H0321["MRIMethod"].map(methodAvg_KPR_slowOrd45_Dec_H0321)
data_KPR_slowOrd45_Dec_H0321["zScore"] = (data_KPR_slowOrd45_Dec_H0321["zScore"] - allAvg_KPR_slowOrd45_Dec_H0321)/allStd_KPR_slowOrd45_Dec_H0321 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_slowOrd45_Dec_H0321["zScore"] < -zscore_threshold,
    data_KPR_slowOrd45_Dec_H0321["zScore"] > zscore_threshold
]

data_KPR_slowOrd45_Dec_H0321["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 4th and 5th order methods with MRIHTol-H211 controller (KPR) -------------------------------
data_KPR_slowOrd45_HTol_H211 = df[(df["order"].isin([4, 5])) & (df["metric"] == "slow") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIHTol-H211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, slow, Order 4 and 5, MRIHTol-H211) ----------------------
allAvg_KPR_slowOrd45_HTol_H211 = data_KPR_slowOrd45_HTol_H211["AvgRank"].mean()
allStd_KPR_slowOrd45_HTol_H211 = data_KPR_slowOrd45_HTol_H211["AvgRank"].std()

# --------------- Mean of each slow 4th and 5th order method across all controllers -----------------------
methodAvg_KPR_slowOrd45_HTol_H211 = data_KPR_slowOrd45_HTol_H211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_slowOrd45_HTol_H211["zScore"] = data_KPR_slowOrd45_HTol_H211["MRIMethod"].map(methodAvg_KPR_slowOrd45_HTol_H211)
data_KPR_slowOrd45_HTol_H211["zScore"] = (data_KPR_slowOrd45_HTol_H211["zScore"] - allAvg_KPR_slowOrd45_HTol_H211)/allStd_KPR_slowOrd45_HTol_H211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_slowOrd45_HTol_H211["zScore"] < -zscore_threshold,
    data_KPR_slowOrd45_HTol_H211["zScore"] > zscore_threshold
]

data_KPR_slowOrd45_HTol_H211["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 4th and 5th order methods with MRIDec-H211 controller (KPR) -------------------------------
data_KPR_slowOrd45_Dec_H211 = df[(df["order"].isin([4, 5])) & (df["metric"] == "slow") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIDec-H211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, slow, Order 4 and 5, MRIDec-H211) ----------------------
allAvg_KPR_slowOrd45_Dec_H211 = data_KPR_slowOrd45_Dec_H211["AvgRank"].mean()
allStd_KPR_slowOrd45_Dec_H211= data_KPR_slowOrd45_Dec_H211["AvgRank"].std()

# --------------- Mean of each slow 4th and 5th order method across all controllers -----------------------
methodAvg_KPR_slowOrd45_Dec_H211 = data_KPR_slowOrd45_Dec_H211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_slowOrd45_Dec_H211["zScore"] = data_KPR_slowOrd45_Dec_H211["MRIMethod"].map(methodAvg_KPR_slowOrd45_Dec_H211)
data_KPR_slowOrd45_Dec_H211["zScore"] = (data_KPR_slowOrd45_Dec_H211["zScore"] - allAvg_KPR_slowOrd45_Dec_H211)/allStd_KPR_slowOrd45_Dec_H211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_slowOrd45_Dec_H211["zScore"] < -zscore_threshold,
    data_KPR_slowOrd45_Dec_H211["zScore"] > zscore_threshold
]

data_KPR_slowOrd45_Dec_H211["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 4th and 5th order methods with MRIHTol-H0211 controller (KPR) -------------------------------
data_KPR_slowOrd45_HTol_H0211 = df[(df["order"].isin([4, 5])) & (df["metric"] == "slow") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIHTol-H0211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, slow, Order 4 and 5, MRIHTol-H0211) ----------------------
allAvg_KPR_slowOrd45_HTol_H0211 = data_KPR_slowOrd45_HTol_H0211["AvgRank"].mean()
allStd_KPR_slowOrd45_HTol_H0211 = data_KPR_slowOrd45_HTol_H0211["AvgRank"].std()

# --------------- Mean of each slow 4th and 5th order method across all controllers -----------------------
methodAvg_KPR_slowOrd45_HTol_H0211 = data_KPR_slowOrd45_HTol_H0211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_slowOrd45_HTol_H0211["zScore"] = data_KPR_slowOrd45_HTol_H0211["MRIMethod"].map(methodAvg_KPR_slowOrd45_HTol_H0211)
data_KPR_slowOrd45_HTol_H0211["zScore"] = (data_KPR_slowOrd45_HTol_H0211["zScore"] - allAvg_KPR_slowOrd45_HTol_H0211)/allStd_KPR_slowOrd45_HTol_H0211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_slowOrd45_HTol_H0211["zScore"] < -zscore_threshold,
    data_KPR_slowOrd45_HTol_H0211["zScore"] > zscore_threshold
]

data_KPR_slowOrd45_HTol_H0211["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 4th and 5th order methods with MRIDec-H0211 controller (KPR) -------------------------------
data_KPR_slowOrd45_Dec_H0211 = df[(df["order"].isin([4, 5])) & (df["metric"] == "slow") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIDec-H0211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, slow, Order 4 and 5, MRIDec-H0211) ----------------------
allAvg_KPR_slowOrd45_Dec_H0211 = data_KPR_slowOrd45_Dec_H0211["AvgRank"].mean()
allStd_KPR_slowOrd45_Dec_H0211= data_KPR_slowOrd45_Dec_H0211["AvgRank"].std()

# --------------- Mean of each slow 4th and 5th order method across all controllers -----------------------
methodAvg_KPR_slowOrd45_Dec_H0211 = data_KPR_slowOrd45_Dec_H0211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_slowOrd45_Dec_H0211["zScore"] = data_KPR_slowOrd45_Dec_H0211["MRIMethod"].map(methodAvg_KPR_slowOrd45_Dec_H0211)
data_KPR_slowOrd45_Dec_H0211["zScore"] = (data_KPR_slowOrd45_Dec_H0211["zScore"] - allAvg_KPR_slowOrd45_Dec_H0211)/allStd_KPR_slowOrd45_Dec_H0211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_slowOrd45_Dec_H0211["zScore"] < -zscore_threshold,
    data_KPR_slowOrd45_Dec_H0211["zScore"] > zscore_threshold
]

data_KPR_slowOrd45_Dec_H0211["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 4th and 5th order methods with MRIHTol-H312 controller (KPR) -------------------------------
data_KPR_slowOrd45_HTol_H312 = df[(df["order"].isin([4, 5])) & (df["metric"] == "slow") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIHTol-H312")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, slow, Order 4 and 5, MRIHTol-H312) ----------------------
allAvg_KPR_slowOrd45_HTol_H312 = data_KPR_slowOrd45_HTol_H312["AvgRank"].mean()
allStd_KPR_slowOrd45_HTol_H312 = data_KPR_slowOrd45_HTol_H312["AvgRank"].std()

# --------------- Mean of each slow 4th and 5th order method across all controllers -----------------------
methodAvg_KPR_slowOrd45_HTol_H312 = data_KPR_slowOrd45_HTol_H312.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_slowOrd45_HTol_H312["zScore"] = data_KPR_slowOrd45_HTol_H312["MRIMethod"].map(methodAvg_KPR_slowOrd45_HTol_H312)
data_KPR_slowOrd45_HTol_H312["zScore"] = (data_KPR_slowOrd45_HTol_H312["zScore"] - allAvg_KPR_slowOrd45_HTol_H312)/allStd_KPR_slowOrd45_HTol_H312 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_slowOrd45_HTol_H312["zScore"] < -zscore_threshold,
    data_KPR_slowOrd45_HTol_H312["zScore"] > zscore_threshold
]

data_KPR_slowOrd45_HTol_H312["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only slow 4th and 5th order methods with MRIDec-H312 controller (KPR) -------------------------------
data_KPR_slowOrd45_Dec_H312 = df[(df["order"].isin([4, 5])) & (df["metric"] == "slow") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIDec-H312")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, slow, Order 4 and 5, MRIDec-H312) ----------------------
allAvg_KPR_slowOrd45_Dec_H312 = data_KPR_slowOrd45_Dec_H312["AvgRank"].mean()
allStd_KPR_slowOrd45_Dec_H312= data_KPR_slowOrd45_Dec_H312["AvgRank"].std()

# --------------- Mean of each slow 4th and 5th order method across all controllers -----------------------
methodAvg_KPR_slowOrd45_Dec_H312 = data_KPR_slowOrd45_Dec_H312.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_slowOrd45_Dec_H312["zScore"] = data_KPR_slowOrd45_Dec_H312["MRIMethod"].map(methodAvg_KPR_slowOrd45_Dec_H312)
data_KPR_slowOrd45_Dec_H312["zScore"] = (data_KPR_slowOrd45_Dec_H312["zScore"] - allAvg_KPR_slowOrd45_Dec_H312)/allStd_KPR_slowOrd45_Dec_H312 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_slowOrd45_Dec_H312["zScore"] < -zscore_threshold,
    data_KPR_slowOrd45_Dec_H312["zScore"] > zscore_threshold
]

data_KPR_slowOrd45_Dec_H312["status"] = np.select(conditions, status, default="intermediate")


# ----------------------------------- Store all data in one excel file with multiple sheets ---------------------------------
with pd.ExcelWriter('allKPR_slowOrder45.xlsx') as writer:
    data_KPR_slowOrd45_HTol_I.to_excel(writer, sheet_name='data_KPR_slowOrd45_HTol_I', index=False)
    data_KPR_slowOrd45_Dec_I.to_excel(writer, sheet_name='data_KPR_slowOrd45_Dec_I', index=False)

    data_KPR_slowOrd45_HTol_H0321.to_excel(writer, sheet_name='data_KPR_slowOrd45_HTol_H0321', index=False)
    data_KPR_slowOrd45_Dec_H0321.to_excel(writer, sheet_name='data_KPR_slowOrd45_Dec_H0321', index=False)

    data_KPR_slowOrd45_HTol_H211.to_excel(writer, sheet_name='data_KPR_slowOrd45_HTol_H211', index=False)
    data_KPR_slowOrd45_Dec_H211.to_excel(writer, sheet_name='data_KPR_slowOrd45_Dec_H211', index=False)

    data_KPR_slowOrd45_HTol_H0211.to_excel(writer, sheet_name='data_KPR_slowOrd45_HTol_H0211', index=False)
    data_KPR_slowOrd45_Dec_H0211.to_excel(writer, sheet_name='data_KPR_slowOrd45_Dec_H0211', index=False)

    data_KPR_slowOrd45_HTol_H312.to_excel(writer, sheet_name='data_KPR_slowOrd45_HTol_H312', index=False)
    data_KPR_slowOrd45_Dec_H312.to_excel(writer, sheet_name='data_KPR_slowOrd45_Dec_H312', index=False)



###############################################################################################################################
# --------------------------------------- Compute the Average z-score of Each Method ------------------------------------------
# load excel file
filename = "allKPR_slowOrder45.xlsx"

# load the sheetnames
xls = pd.ExcelFile(filename)
sheetNames = xls.sheet_names

# store the zsores of each method across the different controllers
ERK45a_zscores    = []
MERK43_zscores    = []
MERK54_zscores    = []
SR43_zscores      = []
ESDIRK46a_zscores = []

for sheet in sheetNames:
    df = pd.read_excel(filename, sheet_name=sheet)

    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_MRI_GARK_ERK45a
    ERK45a_values = df[df["MRIMethod"] == "ARKODE_MRI_GARK_ERK45a"]

    # since the zscore values are the same just pick one
    valueERK45a  = ERK45a_values["zScore"].iloc[0]
    ERK45a_zscores.append(valueERK45a)

    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_MERK43
    MERK43_values = df[df["MRIMethod"] == "ARKODE_MERK43"]

    # since the zscore values are the same just pick one
    valueMERK43  = MERK43_values["zScore"].iloc[0]
    MERK43_zscores.append(valueMERK43)

    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_MERK54
    MERK54_values = df[df["MRIMethod"] == "ARKODE_MERK54"]

    # since the zscore values are the same just pick one
    valueMERK54 = MERK54_values["zScore"].iloc[0]
    MERK54_zscores.append(valueMERK54)

    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_IMEX_MRI_SR43
    SR43_values = df[df["MRIMethod"] == "ARKODE_IMEX_MRI_SR43"]

    # since the zscore values are the same just pick one
    valueSR43 = SR43_values["zScore"].iloc[0]
    SR43_zscores.append(valueSR43)

    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_MRI_GARK_ESDIRK46a
    ESDIRK46a_values = df[df["MRIMethod"] == "ARKODE_MRI_GARK_ESDIRK46a"]

    # since the zscore values are the same just pick one
    valueESDIRK46a = ESDIRK46a_values["zScore"].iloc[0]
    ESDIRK46a_zscores.append(valueESDIRK46a)


# compute the average zscores
with open("AvgZscores_KPR_slowOrd45.txt", "w") as file:
    average_ERK45a = sum(ERK45a_zscores) / len(ERK45a_zscores)
    file.write(f"Average zscore for ARKODE_MRI_GARK_ERK45a (slow KPR): {average_ERK45a}\n\n")

    average_MERK43 = sum(MERK43_zscores) / len(MERK43_zscores)
    file.write(f"Average zscore for ARKODE_MERK43 (slow KPR): {average_MERK43}\n\n")

    average_MERK54= sum(MERK54_zscores) / len(MERK54_zscores)
    file.write(f"Average zscore for ARKODE_MERK54 (slow KPR): {average_MERK54}\n\n")

    average_SR43  = sum(SR43_zscores) / len(SR43_zscores)
    file.write(f"Average zscore for ARKODE_IMEX_MRI_SR43 (slow KPR): {average_SR43}\n\n")

    average_ESDIRK46a  = sum(ESDIRK46a_zscores) / len(ESDIRK46a_zscores)
    file.write(f"Average zscore for ARKODE_MRI_GARK_ESDIRK46a (slow KPR): {average_ESDIRK46a}\n\n")








