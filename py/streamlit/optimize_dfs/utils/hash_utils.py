import hashlib
import importlib
import inspect
import os, sys, time

import pandas as pd
import rich
from rich import print

def get_callables_from_package(package):

    # Get all members (functions, classes, etc.) of the package
    members = dir(package)

    # Filter callable objects (functions and classes) and create a dictionary
    callables_dict = {}
    for member in members:
        obj = getattr(package, member)
        if callable(obj):
            callables_dict[member] = obj

    return callables_dict

def list_hash_types() -> dict[str, str]:

    checksum_dict = get_callables_from_package(hashlib)

    return checksum_dict

def calculate_hash(file_path, hash):
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()

def calculate_md5_for_directory(directory_path: str, hash, sleep_seconds: float = 0.5):
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        return None

    out = []
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            checksum = calculate_hash(file_path, hash())
            print(f"File: {file_name}, checksum: {checksum}")
            time.sleep(sleep_seconds)  # Adjust the sleep duration as needed

            out.append({"file": file_name, "check": checksum})

    return out

if __name__ == "__main__":

    # rich.inspect(list_hash_types())

    gen_sum = list_hash_types()['md5']

    if len(sys.argv) < 2:
        print("Usage: python script_name.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        checksum_data = calculate_md5_for_directory(directory_path, gen_sum)

    if checksum_data is None:
        sys.exit(1)
    
    if len(sys.argv) > 2:
        out_file_name = sys.argv[2]

        df = pd.DataFrame(checksum_data)
        if out_file_name.endswith("csv"):
            df.to_csv(out_file_name)
