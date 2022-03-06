PROJECT=ietf_comments

#############################################################################
## Tasks

.PHONY: run
test: venv
	$(VENV)/python ietf_comments/parser.py test.md

.PHONY: clean
clean:
	find . -d -type d -name __pycache__ -exec rm -rf {} \;
	rm -rf build dist MANIFEST $(PROJECT).egg-info .venv .mypy_cache *.log

.PHONY: tidy
tidy: venv
	$(VENV)/black $(PROJECT) bin/*

.PHONY: lint
lint: venv
	PYTHONPATH=$(VENV) $(VENV)/pylint --output-format=colorized \
	  $(PROJECT) bin/*


#############################################################################
## Distribution

.PHONY: version
version: venv
	$(eval VERSION=$(shell $(VENV)/python -c "import $(PROJECT); print($(PROJECT).__version__)"))

.PHONY: build
build: clean venv
	$(VENV)/python -m build

.PHONY: upload
upload: build typecheck test version
	git tag $(PROJECT)-$(VERSION)
	git push
	git push --tags origin
	$(VENV)/python -m twine upload dist/*



include Makefile.venv
