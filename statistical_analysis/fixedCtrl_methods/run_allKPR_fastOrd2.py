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
# ---------------------- Select only fast 2nd order methods with MRIHTol-I controller (KPR) -------------------------------
data_KPR_fastOrd2_HTol_I = df[(df["order"] == 2) & (df["metric"] == "fast") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIHTol-I")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, Fast, Order 2, MRIHTol-I) ----------------------
allAvg_KPR_fastOrd2_HTol_I = data_KPR_fastOrd2_HTol_I["AvgRank"].mean()
allStd_KPR_fastOrd2_HTol_I = data_KPR_fastOrd2_HTol_I["AvgRank"].std()

# --------------- Mean of each fast 2nd order method across all controllers -----------------------
methodAvg_KPR_fastOrd2_HTol_I = data_KPR_fastOrd2_HTol_I.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_fastOrd2_HTol_I["zScore"] = data_KPR_fastOrd2_HTol_I["MRIMethod"].map(methodAvg_KPR_fastOrd2_HTol_I)
data_KPR_fastOrd2_HTol_I["zScore"] = (data_KPR_fastOrd2_HTol_I["zScore"] - allAvg_KPR_fastOrd2_HTol_I)/allStd_KPR_fastOrd2_HTol_I 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_fastOrd2_HTol_I["zScore"] < -zscore_threshold,
    data_KPR_fastOrd2_HTol_I["zScore"] > zscore_threshold
]

data_KPR_fastOrd2_HTol_I["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 2nd order methods with MRIDec-I controller (KPR) -------------------------------
data_KPR_fastOrd2_Dec_I = df[(df["order"] == 2) & (df["metric"] == "fast") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIDec-I")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, Fast, Order 2, MRIDec-I) ----------------------
allAvg_KPR_fastOrd2_Dec_I = data_KPR_fastOrd2_Dec_I["AvgRank"].mean()
allStd_KPR_fastOrd2_Dec_I = data_KPR_fastOrd2_Dec_I["AvgRank"].std()

# --------------- Mean of each fast 2nd order method across all controllers -----------------------
methodAvg_KPR_fastOrd2_Dec_I = data_KPR_fastOrd2_Dec_I.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_fastOrd2_Dec_I["zScore"] = data_KPR_fastOrd2_Dec_I["MRIMethod"].map(methodAvg_KPR_fastOrd2_Dec_I)
data_KPR_fastOrd2_Dec_I["zScore"] = (data_KPR_fastOrd2_Dec_I["zScore"] - allAvg_KPR_fastOrd2_Dec_I)/allStd_KPR_fastOrd2_Dec_I 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_fastOrd2_Dec_I["zScore"] < -zscore_threshold,
    data_KPR_fastOrd2_Dec_I["zScore"] > zscore_threshold
]

data_KPR_fastOrd2_Dec_I["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 2nd order methods with MRIHTol-H0321 controller (KPR) -------------------------------
data_KPR_fastOrd2_HTol_H0321 = df[(df["order"] == 2) & (df["metric"] == "fast") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIHTol-H0321")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, Fast, Order 2, MRIHTol-H0321) ----------------------
allAvg_KPR_fastOrd2_HTol_H0321 = data_KPR_fastOrd2_HTol_H0321["AvgRank"].mean()
allStd_KPR_fastOrd2_HTol_H0321= data_KPR_fastOrd2_HTol_H0321["AvgRank"].std()

# --------------- Mean of each fast 2nd order method across all controllers -----------------------
methodAvg_KPR_fastOrd2_HTol_H0321 = data_KPR_fastOrd2_HTol_H0321.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_fastOrd2_HTol_H0321["zScore"] = data_KPR_fastOrd2_HTol_H0321["MRIMethod"].map(methodAvg_KPR_fastOrd2_HTol_H0321)
data_KPR_fastOrd2_HTol_H0321["zScore"] = (data_KPR_fastOrd2_HTol_H0321["zScore"] - allAvg_KPR_fastOrd2_HTol_H0321)/allStd_KPR_fastOrd2_HTol_H0321 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_fastOrd2_HTol_H0321["zScore"] < -zscore_threshold,
    data_KPR_fastOrd2_HTol_H0321["zScore"] > zscore_threshold
]

data_KPR_fastOrd2_HTol_H0321["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 2nd order methods with MRIDec-H0321 controller (KPR) -------------------------------
data_KPR_fastOrd2_Dec_H0321 = df[(df["order"] == 2) & (df["metric"] == "fast") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIDec-H0321")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, Fast, Order 2, MRIDec-H0321) ----------------------
allAvg_KPR_fastOrd2_Dec_H0321 = data_KPR_fastOrd2_Dec_H0321["AvgRank"].mean()
allStd_KPR_fastOrd2_Dec_H0321= data_KPR_fastOrd2_Dec_H0321["AvgRank"].std()

# --------------- Mean of each fast 2nd order method across all controllers -----------------------
methodAvg_KPR_fastOrd2_Dec_H0321 = data_KPR_fastOrd2_Dec_H0321.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_fastOrd2_Dec_H0321["zScore"] = data_KPR_fastOrd2_Dec_H0321["MRIMethod"].map(methodAvg_KPR_fastOrd2_Dec_H0321)
data_KPR_fastOrd2_Dec_H0321["zScore"] = (data_KPR_fastOrd2_Dec_H0321["zScore"] - allAvg_KPR_fastOrd2_Dec_H0321)/allStd_KPR_fastOrd2_Dec_H0321 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_fastOrd2_Dec_H0321["zScore"] < -zscore_threshold,
    data_KPR_fastOrd2_Dec_H0321["zScore"] > zscore_threshold
]

data_KPR_fastOrd2_Dec_H0321["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 2nd order methods with MRIHTol-H211 controller (KPR) -------------------------------
data_KPR_fastOrd2_HTol_H211 = df[(df["order"] == 2) & (df["metric"] == "fast") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIHTol-H211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, Fast, Order 2, MRIHTol-H211) ----------------------
allAvg_KPR_fastOrd2_HTol_H211 = data_KPR_fastOrd2_HTol_H211["AvgRank"].mean()
allStd_KPR_fastOrd2_HTol_H211 = data_KPR_fastOrd2_HTol_H211["AvgRank"].std()

# --------------- Mean of each fast 2nd order method across all controllers -----------------------
methodAvg_KPR_fastOrd2_HTol_H211 = data_KPR_fastOrd2_HTol_H211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_fastOrd2_HTol_H211["zScore"] = data_KPR_fastOrd2_HTol_H211["MRIMethod"].map(methodAvg_KPR_fastOrd2_HTol_H211)
data_KPR_fastOrd2_HTol_H211["zScore"] = (data_KPR_fastOrd2_HTol_H211["zScore"] - allAvg_KPR_fastOrd2_HTol_H211)/allStd_KPR_fastOrd2_HTol_H211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_fastOrd2_HTol_H211["zScore"] < -zscore_threshold,
    data_KPR_fastOrd2_HTol_H211["zScore"] > zscore_threshold
]

data_KPR_fastOrd2_HTol_H211["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 2nd order methods with MRIDec-H211 controller (KPR) -------------------------------
data_KPR_fastOrd2_Dec_H211 = df[(df["order"] == 2) & (df["metric"] == "fast") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIDec-H211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, Fast, Order 2, MRIDec-H211) ----------------------
allAvg_KPR_fastOrd2_Dec_H211 = data_KPR_fastOrd2_Dec_H211["AvgRank"].mean()
allStd_KPR_fastOrd2_Dec_H211= data_KPR_fastOrd2_Dec_H211["AvgRank"].std()

# --------------- Mean of each fast 2nd order method across all controllers -----------------------
methodAvg_KPR_fastOrd2_Dec_H211 = data_KPR_fastOrd2_Dec_H211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_fastOrd2_Dec_H211["zScore"] = data_KPR_fastOrd2_Dec_H211["MRIMethod"].map(methodAvg_KPR_fastOrd2_Dec_H211)
data_KPR_fastOrd2_Dec_H211["zScore"] = (data_KPR_fastOrd2_Dec_H211["zScore"] - allAvg_KPR_fastOrd2_Dec_H211)/allStd_KPR_fastOrd2_Dec_H211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_fastOrd2_Dec_H211["zScore"] < -zscore_threshold,
    data_KPR_fastOrd2_Dec_H211["zScore"] > zscore_threshold
]

data_KPR_fastOrd2_Dec_H211["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 2nd order methods with MRIHTol-H0211 controller (KPR) -------------------------------
data_KPR_fastOrd2_HTol_H0211 = df[(df["order"] == 2) & (df["metric"] == "fast") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIHTol-H0211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, Fast, Order 2, MRIHTol-H0211) ----------------------
allAvg_KPR_fastOrd2_HTol_H0211 = data_KPR_fastOrd2_HTol_H0211["AvgRank"].mean()
allStd_KPR_fastOrd2_HTol_H0211 = data_KPR_fastOrd2_HTol_H0211["AvgRank"].std()

# --------------- Mean of each fast 2nd order method across all controllers -----------------------
methodAvg_KPR_fastOrd2_HTol_H0211 = data_KPR_fastOrd2_HTol_H0211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_fastOrd2_HTol_H0211["zScore"] = data_KPR_fastOrd2_HTol_H0211["MRIMethod"].map(methodAvg_KPR_fastOrd2_HTol_H0211)
data_KPR_fastOrd2_HTol_H0211["zScore"] = (data_KPR_fastOrd2_HTol_H0211["zScore"] - allAvg_KPR_fastOrd2_HTol_H0211)/allStd_KPR_fastOrd2_HTol_H0211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_fastOrd2_HTol_H0211["zScore"] < -zscore_threshold,
    data_KPR_fastOrd2_HTol_H0211["zScore"] > zscore_threshold
]

data_KPR_fastOrd2_HTol_H0211["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 2nd order methods with MRIDec-H0211 controller (KPR) -------------------------------
data_KPR_fastOrd2_Dec_H0211 = df[(df["order"] == 2) & (df["metric"] == "fast") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIDec-H0211")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, Fast, Order 2, MRIDec-H0211) ----------------------
allAvg_KPR_fastOrd2_Dec_H0211 = data_KPR_fastOrd2_Dec_H0211["AvgRank"].mean()
allStd_KPR_fastOrd2_Dec_H0211= data_KPR_fastOrd2_Dec_H0211["AvgRank"].std()

# --------------- Mean of each fast 2nd order method across all controllers -----------------------
methodAvg_KPR_fastOrd2_Dec_H0211 = data_KPR_fastOrd2_Dec_H0211.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_fastOrd2_Dec_H0211["zScore"] = data_KPR_fastOrd2_Dec_H0211["MRIMethod"].map(methodAvg_KPR_fastOrd2_Dec_H0211)
data_KPR_fastOrd2_Dec_H0211["zScore"] = (data_KPR_fastOrd2_Dec_H0211["zScore"] - allAvg_KPR_fastOrd2_Dec_H0211)/allStd_KPR_fastOrd2_Dec_H0211 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_fastOrd2_Dec_H0211["zScore"] < -zscore_threshold,
    data_KPR_fastOrd2_Dec_H0211["zScore"] > zscore_threshold
]

data_KPR_fastOrd2_Dec_H0211["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 2nd order methods with MRIHTol-H312 controller (KPR) -------------------------------
data_KPR_fastOrd2_HTol_H312 = df[(df["order"] == 2) & (df["metric"] == "fast") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIHTol-H312")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, Fast, Order 2, MRIHTol-H312) ----------------------
allAvg_KPR_fastOrd2_HTol_H312 = data_KPR_fastOrd2_HTol_H312["AvgRank"].mean()
allStd_KPR_fastOrd2_HTol_H312 = data_KPR_fastOrd2_HTol_H312["AvgRank"].std()

# --------------- Mean of each fast 2nd order method across all controllers -----------------------
methodAvg_KPR_fastOrd2_HTol_H312 = data_KPR_fastOrd2_HTol_H312.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_fastOrd2_HTol_H312["zScore"] = data_KPR_fastOrd2_HTol_H312["MRIMethod"].map(methodAvg_KPR_fastOrd2_HTol_H312)
data_KPR_fastOrd2_HTol_H312["zScore"] = (data_KPR_fastOrd2_HTol_H312["zScore"] - allAvg_KPR_fastOrd2_HTol_H312)/allStd_KPR_fastOrd2_HTol_H312 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_fastOrd2_HTol_H312["zScore"] < -zscore_threshold,
    data_KPR_fastOrd2_HTol_H312["zScore"] > zscore_threshold
]

data_KPR_fastOrd2_HTol_H312["status"] = np.select(conditions, status, default="intermediate")


#######################################################################################################################
# ---------------------- Select only fast 2nd order methods with MRIDec-H312 controller (KPR) -------------------------------
data_KPR_fastOrd2_Dec_H312 = df[(df["order"] == 2) & (df["metric"] == "fast") & (df["Param"].isin([50, 500])) & (df["Controller"] == "MRIDec-H312")][["metric", "order", "Param", "MRIMethod", "Controller", "AvgRank"]]

# ----------------------- Mean and standard deviation of the selected data (KPR, Fast, Order 2, MRIDec-H312) ----------------------
allAvg_KPR_fastOrd2_Dec_H312 = data_KPR_fastOrd2_Dec_H312["AvgRank"].mean()
allStd_KPR_fastOrd2_Dec_H312= data_KPR_fastOrd2_Dec_H312["AvgRank"].std()

# --------------- Mean of each fast 2nd order method across all controllers -----------------------
methodAvg_KPR_fastOrd2_Dec_H312 = data_KPR_fastOrd2_Dec_H312.groupby("MRIMethod")["AvgRank"].mean()

# ------ Calculate the z-score of each method and store on each row corresponding to the method ----
data_KPR_fastOrd2_Dec_H312["zScore"] = data_KPR_fastOrd2_Dec_H312["MRIMethod"].map(methodAvg_KPR_fastOrd2_Dec_H312)
data_KPR_fastOrd2_Dec_H312["zScore"] = (data_KPR_fastOrd2_Dec_H312["zScore"] - allAvg_KPR_fastOrd2_Dec_H312)/allStd_KPR_fastOrd2_Dec_H312 

# ----------------------------- Classify each method based on z-score ------------------------------------
conditions = [
    data_KPR_fastOrd2_Dec_H312["zScore"] < -zscore_threshold,
    data_KPR_fastOrd2_Dec_H312["zScore"] > zscore_threshold
]

data_KPR_fastOrd2_Dec_H312["status"] = np.select(conditions, status, default="intermediate")


# ----------------------------------- Store all data in one excel file with multiple sheets ---------------------------------
with pd.ExcelWriter('allKPR_fastOrder2.xlsx') as writer:
    data_KPR_fastOrd2_HTol_I.to_excel(writer, sheet_name='data_KPR_fastOrd2_HTol_I', index=False)
    data_KPR_fastOrd2_Dec_I.to_excel(writer, sheet_name='data_KPR_fastOrd2_Dec_I', index=False)

    data_KPR_fastOrd2_HTol_H0321.to_excel(writer, sheet_name='data_KPR_fastOrd2_HTol_H0321', index=False)
    data_KPR_fastOrd2_Dec_H0321.to_excel(writer, sheet_name='data_KPR_fastOrd2_Dec_H0321', index=False)

    data_KPR_fastOrd2_HTol_H211.to_excel(writer, sheet_name='data_KPR_fastOrd2_HTol_H211', index=False)
    data_KPR_fastOrd2_Dec_H211.to_excel(writer, sheet_name='data_KPR_fastOrd2_Dec_H211', index=False)

    data_KPR_fastOrd2_HTol_H0211.to_excel(writer, sheet_name='data_KPR_fastOrd2_HTol_H0211', index=False)
    data_KPR_fastOrd2_Dec_H0211.to_excel(writer, sheet_name='data_KPR_fastOrd2_Dec_H0211', index=False)

    data_KPR_fastOrd2_HTol_H312.to_excel(writer, sheet_name='data_KPR_fastOrd2_HTol_H312', index=False)
    data_KPR_fastOrd2_Dec_H312.to_excel(writer, sheet_name='data_KPR_fastOrd2_Dec_H312', index=False)



###############################################################################################################################
# --------------------------------------- Compute the Average z-score of Each Method ------------------------------------------
# load excel file
filename = "allKPR_fastOrder2.xlsx"

# load the sheetnames
xls = pd.ExcelFile(filename)
sheetNames = xls.sheet_names

ERK22b_zscores   = []
IRK21a_zscores   = []
RALSTON2_zscores = []
ERK22a_zscores   = []
MERK21_zscores   = []
SR21_zscores     = []

for sheet in sheetNames:
    df = pd.read_excel(filename, sheet_name=sheet)

    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_MRI_GARK_ERK22b
    ERK22b_values = df[df["MRIMethod"] == "ARKODE_MRI_GARK_ERK22b"]

    # since the zscore values are the same just pick one
    valueERK22b   = ERK22b_values["zScore"].iloc[0]
    ERK22b_zscores.append(valueERK22b)

    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_MRI_GARK_IRK21a
    IRK21a_values = df[df["MRIMethod"] == "ARKODE_MRI_GARK_IRK21a"]

    # since the zscore values are the same just pick one
    valueIRK21a  = IRK21a_values["zScore"].iloc[0]
    IRK21a_zscores.append(valueIRK21a)

    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_MRI_GARK_RALSTON2
    RALSTON2_values = df[df["MRIMethod"] == "ARKODE_MRI_GARK_RALSTON2"]

    # since the zscore values are the same just pick one
    valueRALSTON2  = RALSTON2_values["zScore"].iloc[0]
    RALSTON2_zscores.append(valueRALSTON2)

    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_MRI_GARK_ERK22a
    ERK22a_values = df[df["MRIMethod"] == "ARKODE_MRI_GARK_ERK22a"]

    # since the zscore values are the same just pick one
    valueERK22a  = ERK22a_values["zScore"].iloc[0]
    ERK22a_zscores.append(valueERK22a)


    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_MERK21
    MERK21_values = df[df["MRIMethod"] == "ARKODE_MERK21"]

    # since the zscore values are the same just pick one
    valueMERK21 = MERK21_values["zScore"].iloc[0]
    MERK21_zscores.append(valueMERK21)


    ###########################################################################
    # Filter rows where MRIMethod is ARKODE_IMEX_MRI_SR21
    SR21_values = df[df["MRIMethod"] == "ARKODE_IMEX_MRI_SR21"]

    # since the zscore values are the same just pick one
    valueSR21 = SR21_values["zScore"].iloc[0]
    SR21_zscores.append(valueSR21)


# compute the average zscores
with open("AvgZscores_KPR_fastOrd2.txt", "w") as file:
    average_ERK22b = sum(ERK22b_zscores) / len(ERK22b_zscores)
    file.write(f"Average zscore for ARKODE_MRI_GARK_ERK22b (fast KPR): {average_ERK22b}\n\n")

    average_IRK21a = sum(IRK21a_zscores) / len(IRK21a_zscores)
    file.write(f"Average zscore for ARKODE_MRI_GARK_IRK21a (fast KPR): {average_IRK21a}\n\n")

    average_RALSTON2 = sum(RALSTON2_zscores) / len(RALSTON2_zscores)
    file.write(f"Average zscore for ARKODE_MRI_GARK_RALSTON2 (fast KPR): {average_RALSTON2}\n\n")

    average_ERK22a = sum(ERK22a_zscores) / len(ERK22a_zscores)
    file.write(f"Average zscore for ARKODE_MRI_GARK_ERK22a (fast KPR): {average_ERK22a}\n\n")

    average_MERK21 = sum(MERK21_zscores) / len(MERK21_zscores)
    file.write(f"Average zscore for ARKODE_MERK21 (fast KPR): {average_MERK21}\n\n")

    average_SR21 = sum(SR21_zscores) / len(SR21_zscores)
    file.write(f"Average zscore for ARKODE_IMEX_MRI_SR21 (fast KPR): {average_SR21}\n\n")






