# MRI Adaptivity Paper Codes

This is a repository of [SUNDIALS](https://github.com/LLNL/sundials)-based applications to assess and demonstrate the performance of new capabilities for multirate temporal adaptivity that have been added to ARKODE as part of the [FASTMath SciDAC Institute](https://scidac5-fastmath.lbl.gov/).

## Installation

The following steps describe how to build the demonstration code in a Linux or MacOS environment.

### Gettting the Code

To obtain the code, clone this repository with Git:

```bash
  git clone https://github.com/sundials-codes/mri-adaptivity-paper.git
```

### Requirements

To compile the codes in this repository you will need:

* [CMake](https://cmake.org) 3.20 or newer (both for SUNDIALS and for this repository)

* C compiler (C99 standard) and C++ compiler (C++17 standard)

* Python

### Building all dependencies and test codes

The instructions below outline a step-by-step process for building the relevant dependencies (SUNDIALS, Python modules) and test codes.  However, all necessary steps are encoded in the single `build-all.sh` script.  To run this, execute:

```bash
  bash ./build-all.sh
```

This should build multiple versions of SUNDIALS and various test codes.  You may confirm that this script ran successfully by verifying that there is a new `bin` folder with the contents:

```bash
  ark_kpr_nestedmri_logging
  ark_test_accumerror_brusselator
  ark_test_accumerror_kpr
  ark_test_brusselator_mriadapt
  ark_test_brusselator_mriadapt_hh
  ark_test_brusselator_mriadapt_hh_logging
  ark_test_brusselator_mriadapt_logging
  ark_test_kpr_mriadapt
  ark_test_kpr_mriadapt_hh
  ark_test_kpr_mriadapt_hh_logging
  ark_test_kpr_mriadapt_logging
  ark_test_slowerror_brusselator
  ark_test_slowerror_kpr
```

If these were built successfully, you should "activate" the newly-constructed Python virtual environment,

```bash
source .venv/bin/activate
```

You can then skip directly to the [Running tests section below](#running-tests).

### Building the Dependencies

The codes in this repository depend on two branches of the [SUNDIALS](https://github.com/LLNL/sundials) library.  These two specific versions will be cloned from GitHub as submodules of this repository.  After cloning this repository using the command above, retrieve these submodules via:

```bash
  cd mri-adaptivity-paper
  git submodule init
  git submodule update
```

Additionally, the Python postprocessing scripts in this repository require a number of additional packages, including [NumPy](https://numpy.org/), [Matplotlib](https://matplotlib.org/), and [Pandas](https://pandas.pydata.org/).

We recommend that users follow the instructios below for installing both versions of SUNDIALS.

#### SUNDIALS

[The SUNDIALS build instructions are linked here](https://sundials.readthedocs.io/en/latest/sundials/Install_link.html#building-and-installing-with-cmake).  Note that of the many SUNDIALS build options, this repository requires only a minimal SUNDIALS build.  The following steps can be used to build SUNDIALS using this minimal configuration:

```bash
  mkdir sundials-v7.3.0/build
  cd sundials-v7.3.0/build
  cmake -DCMAKE_INSTALL_PREFIX=../install -DCMAKE_BUILD_TYPE=Release ..
  make -j install
  cd -

  mkdir sundials-mrihh/build
  cd sundials-mrihh/build
  cmake -DCMAKE_INSTALL_PREFIX=../install -DCMAKE_BUILD_TYPE=Release ..
  make -j install
  cd -
```

Additionally, to run the tests that will automatically log all internal time steps at each time scale, allowing plots of the "adaptivity history," you should build SUNDIALS two more times with additional logging enabled:

```bash
  mkdir sundials-v7.3.0/build-logging
  cd sundials-v7.3.0/build-logging
  cmake -DCMAKE_INSTALL_PREFIX=../install-logging -DCMAKE_BUILD_TYPE=Release -DSUNDIALS_LOGGING_LEVEL=4 ..
  make clean
  make -j install
  cd -

  mkdir sundials-mrihh/build-logging
  cd sundials-mrihh/build-logging
  cmake -DCMAKE_INSTALL_PREFIX=../install-logging -DCMAKE_BUILD_TYPE=Release -DSUNDIALS_LOGGING_LEVEL=4 ..
  make clean
  make -j install
  cd -
```

Instructions for building SUNDIALS with additional options [may be found here](https://sundials.readthedocs.io/en/latest/sundials/Install_link.html).

#### Python packages

Since each of NumPy, Matplotlib, and Pandas are widely used, it is likely that these are already installed on your system.  However, if those are missing or need to be updated, then we recommend that these be installed in a Python virtual environment, as follows:

```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r python_requirements.txt
```

You may "deactivate" this Python environment from your current shell with the command

```bash
  deactivate
```

and in the future you can "reactivate" the python environment in your shell by running from the top-level directory of this repository

```bash
  source .venv/bin/activate
```

### Building the tests

The codes that will link to each of the two above SUNDIALS installations must be configured and built in separate phases.  Like most CMake-based projects, in-source builds are not permitted, so the code should be configured and built from a separate build directory.  If the steps above were followed to build the two relevant versions of SUNDIALS, then the test codes in this repository may be built with the commands:

```bash
  cd src-mrihh
  mkdir build
  cd build
  cmake ..
  make -j install
  cd ../../

  cd src-v7.3.0
  mkdir build
  cd build
  cmake ..
  make -j install
  cd ../../
```

When these complete, the following executables should each be in the top-level `bin` folder:
`ark_kpr_nestedmri`,
`ark_test_accumerror_brusselator`,
`ark_test_accumerror_kpr`,
`ark_test_brusselator_mriadapt`,
`ark_test_brusselator_mriadapt_hh`,
`ark_test_kpr_mriadapt`,
`ark_test_kpr_mriadapt_hh`,
`ark_test_slowerror_brusselator`, and
`ark_test_slowerror_kpr`.

To build the additional examples that enable "logging", use the commands:

```bash
  cd src-mrihh-logging
  mkdir build
  cd build
  cmake ..
  make -j install
  cd ../../

  cd src-v7.3.0-logging
  mkdir build
  cd build
  cmake ..
  make -j install
  cd ../../
```

When these complete, the executables should each be in the top-level `bin` folder:
`ark_kpr_nestedmri_logging`,
`ark_test_brusselator_mriadapt_logging`,
`ark_test_brusselator_mriadapt_hh_logging`,
`ark_test_kpr_mriadapt_logging`, and
`ark_test_kpr_mriadapt_hh_logging` will also be installed in the top-level `bin` folder.

## Running tests

All tests and plotting utilities are organized into Python scripts.  The full set of tests can be run with the single shell script

```bash
  bash ./run-all-tests.sh
```

and when that completes, the full set of plots can be generated with the single shell script

```bash
  bash ./make-all-plots.sh
```

If these finish successfully, you may skip directly to the [Analyzing results section below](#analyzing-results).

The remainder of this section provides instructions for running individual tests and generating the corresponding plots.

### Slow error tests

To run the tests that assess the quality of the MRI method embeddings:

```bash
  ./run_slowerror_tests.py
```
or
```bash
  python3 run_slowerror_tests.py
```

To generate the corresponding plots once these tests complete:

```bash
  ./plot_slowerror.py
```
or
```bash
  python3 plot_slowerror.py
```

### Accumulated error tests

To run the tests that assess the approaches for accumulating local errors in the inner solver to predict their effect on slow error:

```bash
  ./run_accumerror_tests.py
```

To generate the corresponding plots once these tests complete:

```bash
  ./plot_accumerror.py
```

### MRI adaptivity tests

To run the tests that assess the quality of various combinations of embedded MRI methods and MRI adaptivity controllers:

```bash
  ./run_mriadapt_tests.py
```

Note that this script runs 4200 different test combinations, and so it can take some time to complete.  We also note that some of these combinations will fail (particularly for the stiff Brusselator problem), causing error messages to print to the screen.

To generate the corresponding plots from the paper once these tests complete:

```bash
  ./plot_mriadapt.py
```

Run this line to generate extras plots that do not show up in the paper:

```bash
  ./plot_mriadapt_extras.py
```

### Nested MRI tests

To run the tests that demonstrate MRI adaptivity within a nested multirate test problem:

```bash
  ./run_nested_kpr_tests.py
```

This test has no corresponding plot, but it generates an Excel file with a table of the results (`kpr_nested_results.xlsx`)

### Adaptivity comparison tests

To run the tests that examine slow and fast time step size histories for a sampling of MRI adaptivity controllers:

```bash
  ./run_adaptivity_comparison.py
```

To generate the corresponding plots once these tests complete:

```bash
  ./plot_adaptivity_comparison.py
```

## Analyzing results
To run the full suite of statistical analyses across all controllers, MRI methods, and test problems:

```bash
  bash ./run-all-statsTests.sh
```

This script runs the following individual statistical analysis modules:

- **runStats_repeatedM_ANOVA.py**: Performs a Repeated Measures ANOVA for all MRI methods across all controllers and test problems, for both fast and slow time scales. It determines whether there is a statistically significant difference between the MRI methods.
```bash
  python3 ./runStats_repeatedM_ANOVA.py
```

- **runStats_oneWayANOVA_ctrl.py**: Performs a One-Way ANOVA for all controllers, across all MRI methods and test problems. It determines whether there is a statistically significant difference between the controllers.
```bash
  python3 ./runStats_oneWayANOVA_ctrl.py
```

- **runStats_fixedCtrl_tests.py**: Performs statistical analysis for the stiff Brusselator and KPR test problems, using a fixed controller across all MRI methods.
```bash
  python3 ./runStats_fixedCtrl_tests.py
```

- **runStats_fixedMethod_tests.py**: Performs statistical analysis for the stiff Brusselator and KPR test problems, using a fixed MRI method across all controllers.
```bash
  python3 ./runStats_fixedMethod_tests.py
```

- **runStats_fixedCtrl_Indep_tests.py**: Performs statistical analysis for all MRI methods using a fixed controller, across all test problems.
```bash
  python3 ./runStats_fixedCtrl_Indep_tests.py
```

- **runStats_fixedMethod_Indep_tests.py**: Performs statistical analysis for all controllers using a fixed MRI method, across all test problems.
```bash
  python3 ./runStats_fixedMethod_Indep_tests.py
```

- **runStats_allCtrls.py**: Performs statistical analysis for all controllers on both the Brusselator and KPR test problems.
```bash
  python3 ./runStats_allCtrls.py
```

- **runStats_hTol_dec_ctrl.py**: Performs statistical analysis for all HTol and Decoupled controllers on the Brusselator and KPR test problems.
```bash
  python3 ./runStats_hTol_dec_ctrl.py
```
