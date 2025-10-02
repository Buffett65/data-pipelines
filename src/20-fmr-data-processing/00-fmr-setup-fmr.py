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
# Data Processing Services (FMR)
#
# This notebook demonstrates using REST API calls to FMR running inside an SDMX Lab instance.
# %% [markdown]
# ### Submitting structural metadata to FMR
#

# %% (code)
from pathlib import Path
import json
import requests
import certifi
from lxml import etree
from getpass import getpass
from requests.auth import HTTPBasicAuth


# %% [markdown]
# ## Setup FMR Structures for the data pipelines session
# 
# ie. Load all data pipelines structures to FMR via REST-API
#
# This step demonstrates how to submit a file of structures to FMR using the REST endpoint.

# %% (code)
# Prepare SDMX structural metadata artefacts
endpoint = f"{fmr_url}/ws/secure/sdmxapi/rest"

path = f"{root_dir}/structures/AllStructures.json"
payload = open(path, "rb")

headers = {"Content-Type": "application/json"}

# Submit and upload all structures to FMR
response = requests.post(
    endpoint, 
    data=payload, 
    headers=headers, 
    auth=(user, password),
    verify=False
)

# %% (code)
# Display response
if response.status_code in [200, 201]:
    print("Resource successfully created in FMR.")
    print("Response:", response.text)
else:
    print(f"Failed to create resource. Status code: {response.status_code}")
    print("Response:", response.text)

# %% [markdown]
# ### Retrieve DSDs in submitted dataflow from FMR via REST-API
#
# This step demonstrates how to retrieve the individual DSDs in the submitted dataflow from FMR using the REST endpoint.
