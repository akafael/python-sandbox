##
# Makefile for Python Projects
##

###############################################################################
# Variables
###############################################################################
VENV3_DIR = venv3
VENV2_DIR = venv2
PYSRC = $(wildcard src/*.py)
PYOBJ = $(PYSRC .py:.pyc)

###############################################################################
# Rules
###############################################################################

# Print help for all commands
.PHONY: help
help:
	@echo "Use: make -f openbuild.mk [OPTION]"
	@echo "\nOPTIONS"
	@sed openbuild.mk -n -e "N;s/^# \(.*\)\n.PHONY:\(.*\)/ \2:\1/p;D" | column -ts:
	@echo ""

# Remove Generated files
.PHONY: clean
clean:
	rm -rfv .venv2 .venv3

# Compile All codes
.PHONY: compile
compile: ${PYOBJ}

# Implicity rule for python code check
src/%.pyc: src/%.py
	python -m py_compile $<

# Virtual Enviroment -----------------------------------------------------------

# Create virtual enviroment for python2
.venv2:
	virtualenv -p python2 $@

# Create and activate virtual enviroment for python 2
.PHONY: venv2
venv2: .venv2 requirements.txt
	. .venv2/bin/activate
	pip install -r requirements.txt

# Create virtual enviroment for python3
.venv3:
	virtualenv -p python3 $@

# Create and activate virtual enviroment for python 3
.PHONY: venv3
venv3: .venv3 requirements.txt
	. .venv3/bin/activate
	pip3 install -r requirements.txt

