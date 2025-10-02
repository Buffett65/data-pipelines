# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
# ---

# %% [markdown]
# # Data Pipelines
#
# This notebook demonstrates the Data Pipeline workflow
# %% [markdown]
# ### 
# 
# The essence of the data pipepline section is to take the building blocks seen earlier and string them together 
# into a sequence of tasks guided by the content of the metadata report attached to each dataflow within
# the Data Pipelines Category Scheme.
#
# **Data Pipeline metadata:**
# Category Scheme: A tree representing data pipeline process/workflow.
#    [] Dataflows are attached to the tree IFF they are to be processed as a part of the workflow
#    [] Annotation attached to Category Scheme to indicate the associated Metadataflow
#    [] A metadata report is created for each dataflow. It has the 'process settings' for the dataflow and is attached to the dataflow
#
# Processing: 
#    Events trigger the pipeline. 
#    The category scheme is traversed and each dataflow is processed according to the attached metadataflow.
#
# See https://py.sdmx.io section on 'processes'
#

# %% (code)
from pathlib import Path
import json
import requests
import certifi
from lxml import etree

