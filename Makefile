PYTHON := python
VENV_DIR := ../venv/bin
PYLINT := ${VENV_DIR}/pylint --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}"
PROJECT_DIR:=service

.PHONY: setup_env freeze clean lint flake

all: flake run


setup_env: requirements.txt
	@echo -e "Installing requirements..."
	@pip install -r requirements.txt
	@echo -e "\nDone!\n"

freeze:
	@echo "Freezing new requirements..."
	@pip freeze > requirements.txt
	@echo -e "Done!\n"

lint:
	${VENV_DIR}/pylint service/

flake:
	@${VENV_DIR}/flake8 --ignore F401

run: setup_env
	${PYTHON} run.py

clean:
	@echo "Removing empty test file"
