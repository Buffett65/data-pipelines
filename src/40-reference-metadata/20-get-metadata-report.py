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
# ### GET A METADATA REPORT TO DATAFLOW
#
# URL to POST a metadata report:  {fmr_url}/ws/secure/sdmx/v2/metadata
# URL to GET a metadata report: {fmr_url}/sdmx/v2/metadata
#
# %% (code)
from pathlib import Path
import json
import requests
import certifi
from lxml import etree
from getpass import getpass
from requests.auth import HTTPBasicAuth

# Prepare SDMX structural metadata artifacts
endpoint = f"{fmr_url}/sdmx/v2/metadata/metadataset/BIS.SDMXIO/*/*"
headers = {"Content-Type": "application/json"}

# Retrieve metadatasets from FMR for http://localhost:8080/sdmx/v2/metadata/metadataset 
# ie. for BIS.SDMXIO/*/*
#  
if sdmx_lab: #auth
    response = requests.get(
        endpoint, 
        headers=headers, 
        auth=(user, password),
        verify=False
    )
else: # no auth
    response = requests.get(
        endpoint, 
        headers=headers, 
        verify=False
    )

# Display response
if response.status_code in [200, 201]:
    print("Resource successfully created in FMR.")
    print("Response:", response.text)
else:
    print(f"Failed to create resource. Status code: {response.status_code}")
    print("Response:", response.text)

#TODO - do the same thing now using pysdmx
#
# Open output in VS CODE or text editor ... and look at content.