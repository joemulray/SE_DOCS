PYTHON = python
VIEWER = more

.PHONY: run view clean

run: computer


computer: cmptr.py
	$(PYTHON) cmptr.py

view: cmptr.py pf.py
	$(VIEWER) cmptr.py
	$(VIEWER) pf.py

clean:
	- rm *.pyc

