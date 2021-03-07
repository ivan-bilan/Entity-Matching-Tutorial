## Setup
To automatically create a conda environment (using Anaconda3) with Python 3.7, run the following command:
```
make build_venv
```

If you are having issues with Anaconda, you can setup the requirements into a Python environment management system of your choice by using:
```
pip install -r requirements.txt
```

In order to be able to use some dependencies of this demo, you have to install additional requirements described under: 
https://github.com/openvenues/pypostal. 

To start the demo, open Jupyter Lab:
```
jupyter lab
```
and navigate to `Entity_Matching_Tutorial.ipynb`

## Data Overview
This tutorial includes a small sample dataset that will allow to run the tutorial in this repository. The hotels contained 
in the dataset are generated automatically and do not refer to real-world hotels.

The dataset includes 100 sample hotel record pairs already annotated:
* 70 record pairs are true matches
* 30 record pairs are negative matches
