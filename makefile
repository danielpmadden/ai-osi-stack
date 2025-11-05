.PHONY: test lint docs install

PYTHON ?= python3

install:
	$(PYTHON) -m pip install --upgrade pip

test:
	$(PYTHON) -m pytest -q

lint:
	$(PYTHON) -m compileall govspine protocol tools

docs:
	$(PYTHON) tools/version-check.py
