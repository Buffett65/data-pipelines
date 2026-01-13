from pysdmx.api.fmr import RegistryClient 

# Establish connection to API fmr_api = "http://localhost:8080/"
fmr_api="http://localhost:8080/sdmx/v2"
fmr_client = RegistryClient(fmr_api)

# Retrieve metadata details for dataflow.
report = fmr_client.get_report("BIS.SDMXIO", "DF_ID2401_SRC", "*")

# Iterate through all items and print them (for illustration, not of much practical use).
for attribute in report:
    print(attribute)
