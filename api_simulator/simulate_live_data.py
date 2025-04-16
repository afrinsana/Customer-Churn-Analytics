
import pandas as pd
import time
import random
import os

# Load the cleaned dataset
df = pd.read_csv('../data/features.csv')

# File to simulate live data stream
live_data_file = '../data/live_data.csv'

# Ensure the live_data.csv exists
if not os.path.exists(live_data_file):
    df.iloc[0:0].to_csv(live_data_file, index=False)  # Create empty file with headers

print("Starting live data simulation...")

# Simulate incoming data every 5 seconds
while True:
    # Pick a random row (simulate a new customer arriving)
    new_row = df.sample(n=1)

    # Append to live_data.csv
    new_row.to_csv(live_data_file, mode='a', header=False, index=False)
    print("New data added to live stream.")

    # Wait before next customer appears
    time.sleep(5)
