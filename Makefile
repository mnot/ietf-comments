PROJECT = ietf_comments


.PHONY: test
test: test-ietf test-rfced

.PHONY: test-ietf
test-ietf: venv
	PYTHONPATH=$(VENV) $(VENV)/pip install .
	PYTHONPATH=$(VENV):. $(VENV)/ietf-comments examples/ad_comments.md

.PHONY: test-rfced
test-rfced: venv
	PYTHONPATH=$(VENV) $(VENV)/pip install .
	PYTHONPATH=$(VENV):. $(VENV)/rfced-comments ./examples/rfced_comments.xml

.PHONY: clean
clean: clean_py

.PHONY: lint
lint: lint_py

.PHONY: typecheck
typecheck: typecheck_py

.PHONY: tidy
tidy: tidy_py



include Makefile.pyproject
