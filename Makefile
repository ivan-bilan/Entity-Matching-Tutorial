.PHONY: build_venv remove_env

VENV_NAME=entity_matching_demo
CONDA_HOME=$(HOME)/anaconda3
CONDA_ENVS=$(CONDA_HOME)/envs

help:
	@echo "build_env - create a fresh conda environment with all requirements already installed"
	@echo "remove_env - delete the previously created virtual environment"

build_venv:
	command -v conda || . $(CONDA_HOME)/etc/profile.d/conda.sh && \
	conda env create -n $(VENV_NAME) -f environment.yml --force && \
	conda activate $(VENV_NAME)

remove_env:
	command -v conda || . $(CONDA_HOME)/etc/profile.d/conda.sh && \
	conda remove --name $(VENV_NAME) --all