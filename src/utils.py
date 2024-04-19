import sys
import os
import json
def load_config(name ,verbose=True):
    try:
        with open(name,"r") as f:
            config = json.load(f)
        del(f)
        if verbose:
            print(f"File '{name}' loaded successfully.")
    except Exception as e:
        print({"Exception":e})
        print(f"Try to correct ROOT and if config/{name} file is correctly configured.")
        sys.exit()
    return config