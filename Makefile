##
# Makefile for Python3 enviroments
#
# @author Akafael
# @version 1.1
#
##

###############################################################################
# Variables
###############################################################################

# Custom Python Version Variables
PYVERSION := 3.7.7
VIRTUALENVVERSION := 20.0.21 # Link hardcoded Unable to Change

# Get Makefile directory
MAKEFILE_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

# Temporary Directories
TMP_DIR := ${MAKEFILE_DIR}/tmp
INSTALLPYTHON_DIR := ${MAKEFILE_DIR}/tmp/python-${PYVERSION}
INSTALLVIRTUALENV_DIR := ${MAKEFILE_DIR}/tmp/virtualenv-${VIRTUALENVVERSION}

# Tools Directories
LOCALPYTHON_DIR := ${MAKEFILE_DIR}/tools/python-${PYVERSION}
LOCALVIRTUALENV_DIR := ${MAKEFILE_DIR}/tools/py${PYVERSION}

# Python Source Files
PYSRC = $(wildcard src/*.py)
PYOBJ = $(PYSRC:.py=.pyc)

###############################################################################
# Rules
###############################################################################

# Print help for Makefile commands
.PHONY: help
help:
	@echo "Use: make -f Makefile [OPTION]"
	@echo "\nOPTIONS"
	@sed Makefile -n -e "N;s/^# \(.*\)\n.PHONY:\(.*\)/ \2:\1/p;D" | column -ts:
	@echo ""

# Enviroment Phony Rules ------------------------------------------------------

# Compile All codes
.PHONY: compile
compile: ${PYOBJ}

##
# Implicity rule for python code check
# - Using Installed Python
##
src/%.pyc: src/%.py
	. ${LOCALVIRTUALENV_DIR}/bin/activate &&\
	python -m py_compile $<

# Download Tools and Create Local Enviroment
.PHONY: env
env: install-python install-virtualenv create-virtualenv install-pythonlibs

# Download Python and build it locally
.PHONY: install-python
install-python: ${LOCALPYTHON_DIR}

# Download and Install Virtualenv using Installed Python
.PHONY: install-virtualenv
install-virtualenv: ${LOCALPYTHON_DIR} ${INSTALLVIRTUALENV_DIR}

# Create Virtualenv using Local Python
.PHONY: create-virtualenv
create-virtualenv: ${LOCALVIRTUALENV_DIR}

# Activate Virtualenv and Install Python libraries
.PHONY: install-pythonlibs
install-pythonlibs: ${LOCALVIRTUALENV_DIR} requirements.txt
	. ${LOCALVIRTUALENV_DIR}/bin/activate &&\
	pip install -r requirements.txt

# Remove Enviromment Installation Files
.PHONY: clean-install
clean-install:
	rm -vf tmp/Python-${PYVERSION}.tgz
	rm -rvf tmp/Python-${PYVERSION}
	rm -vf tmp/virtualenv-20.0.21.tar.gz
	rm -rvf tmp/virtualenv-20.0.21

# Remove Local Enviroment Files
.PHONY: clean-env
clean-env:
	rm -rvf ${LOCALPYTHON_DIR} ${LOCALVIRTUALENV_DIR}

# Enviroment Explicity Rules --------------------------------------------------

##
# Download Chosen Python Version and build locally
##
${LOCALPYTHON_DIR}:
	mkdir -p ${TMP_DIR} && cd ${TMP_DIR} &&\
	wget --inet4-only https://www.python.org/ftp/python/${PYVERSION}/Python-${PYVERSION}.tgz &&\
	mkdir -p ${INSTALLPYTHON_DIR} &&\
	tar -zxvf Python-${PYVERSION}.tgz -C ${INSTALLPYTHON_DIR} --strip-components=1 &&\
	cd ${INSTALLPYTHON_DIR} &&\
   	./configure --prefix=${LOCALPYTHON_DIR} &&\
	make && make install

##
# Download and Install Virtualenv using Installed Python
# - Link Hardcoded for  20.0.21
##
${INSTALLVIRTUALENV_DIR}: ${LOCALPYTHON_DIR}
	mkdir -p ${TMP_DIR} && cd ${TMP_DIR} &&\
	wget --inet4-only https://files.pythonhosted.org/packages/55/67/beb3ecfa973181a52fad76fc959b745631b258c5387348ae1e06c8ca7a81/virtualenv-20.0.21.tar.gz &&\
	mkdir -p ${INSTALLVIRTUALENV_DIR} &&\
	tar -zxvf virtualenv-20.0.21.tar.gz -C ${INSTALLVIRTUALENV_DIR} --strip-components=1 &&\
	cd ${INSTALLVIRTUALENV_DIR} &&\
	${LOCALPYTHON_DIR}/bin/python3 setup.py install

##
# Create Virtualenv using Installed Python
##
${LOCALVIRTUALENV_DIR}: ${LOCALPYTHON_DIR} ${INSTALLVIRTUALENV_DIR}
	mkdir -p ${LOCALVIRTUALENV_DIR}/.. &&\
	cd ${LOCALVIRTUALENV_DIR}/.. &&\
	${LOCALPYTHON_DIR}/bin/virtualenv py${PYVERSION} --python=${LOCALPYTHON_DIR}/bin/python3


