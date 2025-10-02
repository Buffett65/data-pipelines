import jupytext
import nbformat

files = [
    "src/00-setup-environment.py",
    "src/10-sdmx-api/10-sdmx-api.py",
    "src/20-fmr-data-processing/00-fmr-setup-fmr.py",
    "src/20-fmr-data-processing/10-fmr-validate-jupytext.py",
    "src/20-fmr-data-processing/20-fmr-transcode-jupytext.py",
    "src/20-fmr-data-processing/30-fmr-verify-mapping-jupytext.py",
    "src/40-reference-metadata/00-setup.py",
    "src/40-reference-metadata/10-post-metadata-report.py",
    "src/40-reference-metadata/20-get-metadata-report.py",
    "src/50-data-pipeline/00-setup.py",]

merged = nbformat.v4.new_notebook()
merged.cells = []

for f in files:
    if f.endswith(".ipynb"):
        nb = nbformat.read(f, as_version=4)
    else:  # assume .py
        nb = jupytext.read(f)
    merged.cells.extend(nb.cells)

nbformat.write(merged, "merged-all.ipynb")