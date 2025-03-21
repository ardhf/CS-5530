import pandas as pd

# This file will take in the raw_data.csv and clean it to ensure all rows are complete.
# Read the file from csv
df = pd.read_csv('Assignment1/Q2/data_raw/raw_students_performance.csv')

# Verify the data was imported correctly
print(f'\nOriginal Data\n{df.head()}')

# This will show how many NaN values are in each column
print(f'\nNa Counts\n{df.isna().sum()}')

# Dropping any rows with missing data
df = df.dropna()

# Verifying the dataframe is clean
print(f'\nClean Data\n{df.head()}')

# Exporting the cleaned data to the clean data folder without the row index
df.to_csv('Assignment1/Q2/data_clean/clean_students_performance.csv', index=False)