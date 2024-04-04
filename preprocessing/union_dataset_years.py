# ~~~~~~~~~~~~~~~~~~~~~~~~
# DEPRECATED as of 2024-04-04 -Mac
print(
    "DEPRECATED as of 2024-04-04 -Mac\nUse updated function from preprocessing_funcs.py"
)
exit()
# ~~~~~~~~~~~~~~~~~~~~~~~


import pandas as pd

# Load the datasets
file_paths = [
    "/mnt/data/PROCESSED_Wells_Fargo_Mortgage_2018.csv",
    "/mnt/data/PROCESSED_Wells_Fargo_Mortgage_2019.csv",
    "/mnt/data/PROCESSED_Wells_Fargo_Mortgage_2020.csv",
    "/mnt/data/PROCESSED_Wells_Fargo_Mortgage_2021.csv",
    "/mnt/data/PROCESSED_Wells_Fargo_Mortgage_2022.csv",
]

# Read and concatenate the datasets
dfs = [pd.read_csv(file) for file in file_paths]
union_df = pd.concat(dfs, ignore_index=True)

# Save the unioned dataset to a new file
output_file_path = "/mnt/data/Unioned_Wells_Fargo_Mortgage_2018_2022.csv"
union_df.to_csv(output_file_path, index=False)

output_file_path
