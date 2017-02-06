#Joseph Mulray, Makefile for CSV Library

PYTHON = python
VIEWER = less

.PHONY: clean view run

run: csv

csv: csvlib.py
	$(PYTHON) csvlib.py $(arg)


view:  csvlib.py
	$(VIEWER) csvlib.py

clean:
	- rm $(outFile) >/ dev/null 2>&1
	- rm *.pyc > /dev/null 2>&1
