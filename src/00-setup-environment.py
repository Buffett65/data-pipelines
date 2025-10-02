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
# ## Setup SDMX Lab Jupyter Notebook environment
#

# %%  # code cell
# Clone the repo
#PROD
# #!git clone https://github.com/HMS-Analytical-Software/hms-sdmx-lab-notebooks.git
# #%cd hms-sdmx-lab-notebooks/notebooks/data-pipelines
#DEV
!git clone https://github.com/Buffett65/data-pipelines.git
%cd data-pipelines
root_dir="/content/data-pipelines"

# Install dependencies
!pip install -r requirements.txt

# %%
from pathlib import Path
import os
import json
import requests
import certifi
from lxml import etree
from getpass import getpass
from requests.auth import HTTPBasicAuth
from dataclasses import dataclass

@dataclass
class MyConfig:
    # Load config variables
    with open(f"{root_dir}/config.json") as f:
        config = json.load(f)
    _test = config["TEST"]
    agency = config["AGENCY"]
    flowid = config["FLOWID"]
    endpoint = config["ENDPOINT"]
    #
    out_dir = f"{root_dir}/data"

    headers = {"Accept": "application/xml"}  # we'll ask for SDMX-ML data via ?format=sdmx-3.0

cfg = MyConfig()

# %% [markdown]
# Set up your credentials for basic authorization. These will be used to authenticate REST API calls to the Lab instance.

# %%
# Obtain Lab instance endpoint
sdmx_lab=True # if True, need to use 'auth' on *ALL* api calls, not just on POST calls.

lab_url = os.environ.get("USER_LAB") or input("Enter URL of your Lab space: ")
fmr_url = f"{lab_url}/fmr"

# Obtain authentication credentials
user = os.environ.get("USER_ID") or input("Username: ")
password = os.environ.get("PASS") or input("Password: ")
auth = HTTPBasicAuth(username=user, password=password)

print(f"User: {user}")
print(f"password: {password}")
print(f"Lab URL: {lab_url}")
print(f"FMR URL: {fmr_url}")
