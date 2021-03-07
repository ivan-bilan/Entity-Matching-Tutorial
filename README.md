## General Description of Entity Matching
Entity matching describes the approach of finding records throughout different databases or any other 
data storage types that refer to the same real-world entity. These entities are identified by crosschecking
their identifiers such as name, address, phone number, and similar. Entity matching, also known as record 
linkage, has applications in various scientific fields and industrial solutions. They range from matching 
people in census data, bibliographic databases, 
forensic data and DNA matching, physical objects like businesses, and many more. It is mainly 
used to consolidate records of the same type and especially used with textual data. For example, when 
matching company entities from two databases, we can match them by name and address and merge the two 
databases into one. Additionally, entity matching is often used in the process of finding duplicates 
within the same database.

Entity Matching approaches usually follow similar steps. 
The problem usually starts with data pre-processing step, then pre-filtering of potential candidate 
pairs, record pair comparison, and finally classification of each record pair as a true or negative match.

This tutorial shows how to apply threshold-based and neural based approaches to an Entity Matching task between two 
record sources containing hotel entities.

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

The dataset includes 84 sample hotel record pairs already annotated:
* 55 record pairs are true matches
* 29 record pairs are negative matches
