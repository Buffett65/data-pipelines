# %% [markdown]
# ## SDMX API
#
# %% [markdown]
# ### Setup Environment for SDMX API examples and exercises.
#
# %%  # code cell

import requests, urllib.parse as up
import xml.etree.ElementTree as ET
from typing import Dict, Any, List, Tuple, Optional
import json
import io
import os
import pandas as pd



def get_csv(url, headers=None, params=None):
    r = requests.get(url, params=params, headers=headers, timeout=60)
    r.raise_for_status()
    # (optional but safe) ensure correct decoding before you touch .text
    # SDMX-CSV is UTF-8, so force UTF-8 to avoid stray characters
    r.encoding = "utf-8"
    return r

# %% [markdown]
# ### EXAMPLE: SDMX REST API - get structure
# ###          Scenario: get all dataflows, return JSON
#
# %% [markdown]
# ### Version A: bespoke code
#
# %%  # code cell
# Retrieve all dataflows, based on config parameters.
# Example --- sdmx-json structure call

# Make an API structure call requesting all dataflows     
r = requests.get(f"{cfg.endpoint}/structure/dataflow/*/*/*", 
                 params={"format":"sdmx-json"}, 
                 headers=None, 
                 timeout=60)
r.raise_for_status()

flows=r.json()

# Create List of all dataflows (catalog)
dfs = []
for flow in (flows.get("data", {}).get("dataflows",{})):
    name = flow.get("name")
    agency = flow.get('agencyID')
    id = flow.get("id")
    version = flow.get('version')
    description = flow.get("description")
    dfs.append({"agency": agency, "id": id, "version": version, "name": name, "description": description})

dfs[:10]  # peek

# %% [markdown]
# ### Version B: using pysdmx
#
# %%  # code cell

from pysdmx.api.fmr import RegistryClient
fmr_client=RegistryClient(f"{cfg.endpoint}")
dfs=fmr_client.get_dataflows("*","*","*")

dfs[:10]  # peek


# %% [markdown]
# ### EXAMPLE: SDMX REST API - get structure
# ###          Scenario: get all dataflows, return SDMX-ML
# 
# %% [markdown]
# ### Version A: bespoke code
#
# %%  # code cell

# 1) Make an API structure call, retrieve all dataflows (catalog)

# Call an SMDX API endpoint requesting an SMDX-ML response.
flows = requests.get(f"{cfg.endpoint}/structure/dataflow/{cfg.agency}/*/*", 
                     params={"format":"sdmx-3.0", "prettyPrint":True}, 
                     headers={"Accept": "application/xml"}, 
                     timeout=60)
r.raise_for_status()

# Parse the XML and return its ElementTree and namespaces.
root = ET.fromstring(r.content) 

# Extract all namespaces declared in the document
namespaces = dict([
    node for _, node in ET.iterparse(
            # We need a bytes stream for iterparse
            io.BytesIO(r.content),
            events=['start-ns']
    )
])

# Create List of all dataflows (catalog)
dfs = []
for flow in flows.findall(".//str:Dataflow", namespaces):
    agency = flow.attrib.get('agencyID')
    id = flow.attrib.get('id')
    version = flow.attrib.get('version')
    name_elem = flow.find("com:Name", namespaces)
    name = name_elem.text if name_elem is not None else None
    description_elem = flow.find("com:Description", namespaces)
    description = description_elem.text if description_elem is not None else None
    dfs.append({"agency": agency, "id": id, "version": version, "name": name, "description": description})

dfs[:10]  # peek
# %% [markdown]
# ### Version B: using pysdmx
#
# %%  # code cell

from pysdmx.api.fmr import RegistryClient
fmr_client=RegistryClient(f"{cfg.endpoint}")
dfs=fmr_client.get_dataflows("*","*","*")

dfs[:10]  # peek

# %% [markdown]
# ### EXAMPLE: SDMX REST API - get data
# ###          Scenario: get dataset, return CSV, save to file.
#
# %%  # code cell
# Ensure output directory exists
os.makedirs(cfg.out_dir, exist_ok=True)

# Build filename from flowid
filename = f"{flowid}.csv"
out_path = os.path.join(cfg.out_dir, filename)

# Make an API data call, retrieve the latest 1 observation, in csv format, for the provided agency/dataflow/version
resp = requests.get(cfg.endpoint}/data/dataflow/{agency}/{flowid}/*",
                    params={"format":"sdmx-csv", "lastNobservations":"1"}, 
                    headers={"Accept": "application/text"},
                    timeout=60)

resp.raise_for_status()

# (optional but safe) ensure correct decoding before you touch .text
# SDMX-CSV is UTF-8, so force UTF-8 to avoid stray characters
resp.encoding = "utf-8"

# Get csv into a pandas dataframe
dataset = pd.read_csv(
    io.StringIO(resp.text),
    dtype=str,              # start as strings; we’ll coerce precisely below
    keep_default_na=True,   # empty fields -> NaN
)

# 1st 10 lines of the Pandas Dataframe 
dataset.head(10)    

# %% [markdown]
# ### Drop the first column of a pandas DataFrame and save to CSV.
#
# %% (code cell)

# Drop the first column
dataset_out = dataset.drop(dataset.columns[0], axis=1)

# Save to CSV
dataset_out.to_csv(out_path, index=False)

print(f"Saved {dataset.shape[0]} rows x {dataset_out.shape[1]} cols to {out_path}")
