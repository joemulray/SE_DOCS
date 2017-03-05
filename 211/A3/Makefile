PYTHON = python
VIEWER = more

.PHONY: run view clean

run: alpha.py
	$(PYTHON) alpha.py

view: alpha.py model.py manufact.py
	$(VIEWER) alpha.py
	$(VIEWER) model.py
	$(VIEWER) manufact.py

clean: 
	-rm *.pyc



