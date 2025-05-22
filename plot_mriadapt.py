#!/usr/bin/env python3
#------------------------------------------------------------
# Programmer(s):  Daniel R. Reynolds @ SMU
#------------------------------------------------------------
# Copyright (c) 2024, Southern Methodist University.
# All rights reserved.
# For details, see the LICENSE file.
#------------------------------------------------------------

# imports

import os
import matplotlib.pyplot as plt
import sys
sys.path.append('..')
import plot_utilities_paper as putil
import pandas as pd

Bruss_fname = 'brusselator_mriadapt_results.xlsx'
KPR_fname = 'kpr_mriadapt_results.xlsx'

data=pd.read_excel(Bruss_fname)
bruss_failed_pairs = data.loc[data['ReturnCode'] == 1, ['control', 'mri_method']]
data2=pd.read_excel(KPR_fname)
kpr_failed_pairs = data2.loc[data2['ReturnCode'] == 1, ['control', 'mri_method']]

# flags to turn on/off certain plots
Plot_KPR = True
Plot_Bruss = True
Hh_controllers={'MRICC',
              'MRILL',
              'MRIPI',
              'MRIPID'}
Htol_controllers={'MRIHTol-H0211',
                'MRIHTol-H0321',
                'MRIHTol-H211',
                'MRIHTol-I',
                'MRIHTol-H312'}
Decoupled_controllers={'MRIDec-H0211',
                'MRIDec-H0321',
                'MRIDec-H211',
                'MRIDec-I',
                'MRIDec-H312',}
Full_controllers={'MRICC',
                'MRILL',
                'MRIPI',
                'MRIPID',
                'MRIDec-H0211',
                'MRIDec-H0321',
                'MRIDec-H211',
                'MRIDec-I',
                'MRIDec-H312',
                'MRIHTol-H0211',
                'MRIHTol-H0321',
                'MRIHTol-H211',
                'MRIHTol-I',
                'MRIHTol-H312'}

kpr_retained_low_pairs=[('MRIDec-I','ARKODE_MRI_GARK_IRK21a'),
                    ('MRIDec-H211','ARKODE_IMEX_MRI_SR21'),
                    ('MRIDec-H0321','ARKODE_IMEX_MRI_SR21'),
                    ('MRIDec-H0321','ARKODE_MRI_GARK_IRK21a'),
                    ]

bruss_removed_pairs=list(bruss_failed_pairs.itertuples(index=False, name=None))
kpr_removed_pairs=list(kpr_failed_pairs.itertuples(index=False, name=None))
# generate plots, loading data from stored output
#axis limits= [[ax1],[ax2],[ax3],[ax4]]
kpr_xlim_lo=[[5e1,1e4],[1e3,2e5],[7e1,1e4],[1e4,2e6]]
kpr_xlim_mid=[[4e1,1e4],[5e2,1e5],[1e1,1e4],[1e4,1e7]]
kpr_xlim_hi=[[1e1,1e3],[1e1,1e4],[5e1,1e3],[1e3,1e5]]

bruss_xlim_lo=[[1e2,1e5],[1e4,1e6],[1e2,5e4],[1e5,5e6]]
bruss_xlim_mid=[[1e2,1e4],[1e4,6e5],[1e2,1e4],[1e5,5e6]]
bruss_xlim_hi=[[1e1,1e3],[1e4,1e6],[5e1,1e3],[1e4,1e7]]
if Plot_KPR:
    putil.do_comparison_plots(KPR_fname, 'omega', [50, 500], r'$\omega$', Full_controllers,'All controller',
                              'paper-kpr',kpr_removed_pairs,'kpr',kpr_xlim_lo,kpr_xlim_mid,kpr_xlim_hi)

if Plot_Bruss:
    putil.do_comparison_plots(Bruss_fname, 'ep', [1.e-4, 1.e-5], r'$\epsilon$', Full_controllers, 'All controller',
                              'paper-bruss', bruss_removed_pairs,'bruss',bruss_xlim_lo,bruss_xlim_mid,bruss_xlim_hi)
    
putil.combine()

#print a list of all failed tests to stdout
if Plot_KPR:
   putil.print_failed_tests(KPR_fname, 'KPR')
if Plot_Bruss:
   putil.print_failed_tests(Bruss_fname, 'Stiff Brusselator')

## display plots
plt.show()
