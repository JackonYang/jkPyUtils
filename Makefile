PY?=python3
PIP?=pip3


dev-setup:
	$(PIP) install -r requirements-dev.txt

test:
	pytest .


build:
	$(PY) setup.py sdist bdist_wheel

upload:
	twine upload dist/*

install:
	$(PIP) install -e .


.PHONY: dev-setup
.PHONY: test

.PHONY: build upload install
