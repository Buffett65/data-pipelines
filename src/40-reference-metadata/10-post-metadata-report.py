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
# ### POST A METADATA REPORT TO DATAFLOW
#
# URL to POST a metadata report:  {fmr_url}/ws/secure/sdmx/v2/metadata
# URL to GET a metadata report: {fmr_url}/sdmx/v2/metadata
# %% (code)
from pathlib import Path
import json
import requests
import certifi
from lxml import etree
from getpass import getpass
from requests.auth import HTTPBasicAuth

root_dir = f"/Users/client-bis/dev/repos/data-pipelines" #FIX

# Prepare SDMX structural metadata artefacts
endpoint = f"{fmr_url}/ws/secure/sdmx/v2/metadata"
reports = {f"{root_dir}/data/PID001-pass.json",
        f"{root_dir}/data/PID001_DF2-pass.json",
        }

headers = {"Content-Type": "application/json"}

for path in reports: 
    # Submit and upload report to FMR
    payload = open(path, "rb")
    response = requests.post(
        endpoint, 
        data=payload, 
        headers=headers, 
        auth=(user, password),
        verify=False
    )

    # Display response
    if response.status_code in [200, 201]:
        print("Resource successfully created in FMR.")
        print("Response:", response.text)
    else:
        print(f"Failed to create resource. Status code: {response.status_code}")
        print("Response:", response.text)

# NOTE: replace with pysdmx calls once SDMX LAB auth access is ready.
# 
# next: open FMR UI, open dataflow, confirm metadata report is attached to dataflow.