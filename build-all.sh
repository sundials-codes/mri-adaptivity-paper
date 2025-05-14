#!/bin/bash
#
# This script builds all dependencies and test codes, following the instructions in the README.md file.

# pull submodules
git submodule init
git submodule update

# build sundials four ways: (v7.3.0 and the archived branch with mrihh) x (Release and Logging)
# Note: the sundials-mrihh branch is archived and not maintained. It is only used for testing the MRI-HH adaptivity controllers.
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

# build python dependencies as a virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r python_requirements.txt

# build test codes
mkdir src-mrihh/build
cd src-mrihh/build
cmake ..
make -j install
cd -
mkdir src-v7.3.0/build
cd src-v7.3.0/build
cmake ..
make -j install
cd -
mkdir src-mrihh-logging/build
cd src-mrihh-logging/build
cmake ..
make -j install
cd -
mkdir src-v7.3.0-logging/build
cd src-v7.3.0-logging/build
cmake ..
make -j install
cd -
