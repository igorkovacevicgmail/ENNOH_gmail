
import os
import sys
import pandas as pd
import numpy as np

ROOT_DIR = os.getcwd()
PROJECT_DIR = os.path.join(ROOT_DIR, "drive/MyDrive/Colab_Notebooks/PyPSA/Zonal_model/data/")

from google.colab import drive
drive.mount('/content/drive')

import json

file_path = PROJECT_DIR + 'input_data.json'

try:
    with open(file_path, 'r') as f:
        loaded_data = json.load(f)
    print(f"Successfully loaded data from {file_path}:")
    # print(json.dumps(loaded_data, indent=2)) # Uncomment to see full content
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found. Please ensure it exists and your Google Drive is mounted correctly.")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from {file_path}. The file might be corrupted or not a valid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

optimization_inputs = loaded_data.get('optimization_inputs')
elec_generators = loaded_data.get('elec_generators')
