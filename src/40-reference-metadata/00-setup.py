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
# # Reference Metadata
#
# This notebook demonstrates Reference Metadata
# ### 
# 
# The essence of the refernce metadata section is to demonstrate the elements to be created for a simple data pipeline
# system controlled by reference metadata (loosely coupled business logic, versioned, ...). In brief, metadata driven processes.
#
# **Reference Metadata**
# Category Scheme: A tree representing data pipeline process/workflow.
#    [] Dataflows are attached to the tree IFF they are to be processed as a part of the workflow
#    [] Annotation attached to Category Scheme to indicate the associated Metadataflow
#    [] A metadata report is created for each dataflow. It has the 'process settings' for the dataflow and is attached to the dataflow
# Codelists: For decision trees
# Metadata Structure Definition: 
# Metadataflows: One per process
# Metadatasets: One per dataflow. The process settings for this dataflow.
# Provision Agreements: according to needs of process workflow
#
# See artifacts in FMR (after AllStructures.json is loaded)
# See https://py.sdmx.io section on 'processes'
#
# %% [markdown]
# ### 
#

# %% (code)
from pathlib import Path
import json
import requests
import certifi
from lxml import etree

