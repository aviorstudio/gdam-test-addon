.DEFAULT_GOAL := help
SHELL := /bin/bash
.PHONY: help install check clean lint test build dev stop
help:
	@echo 'make install: pinned Python; make check: fixture manifest and entrypoint'
install:
	mise trust .mise.toml
	mise install
check:
	mise exec -- python3 scripts/check_fixture.py
clean:
	mise exec -- python3 -c 'import shutil; shutil.rmtree(".artifacts", ignore_errors=True)'
lint test build dev stop:
	@echo '$@: unsupported: source fixture; runtime integration belongs to its consumer'
