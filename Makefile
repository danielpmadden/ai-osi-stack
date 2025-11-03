.PHONY: test lint docs install

PYTHON ?= python3

install:
$(PYTHON) -m pip install --upgrade pip

test:
$(PYTHON) -m pytest -q

lint:
$(PYTHON) -m compileall src protocol tools

docs:
$(PYTHON) tools/version_check.py
