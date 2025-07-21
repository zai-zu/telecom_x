
import os
import pandas as pd

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the processed data folder
processed_data_path = os.path.join(current_dir, '..', 'data', 'processed', 'custumers_norm_processed.csv')

# Read the CSV file
df_custumers = pd.read_csv(processed_data_path)
