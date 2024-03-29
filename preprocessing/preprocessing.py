import pandas as pd
from glob import glob
from mapping import MAPPER

for f in glob("preprocessing/data/input/*.csv"):
    df = pd.read_csv(f, dtype="string")

    for col in MAPPER.keys():
        df[col] = df[col].map(MAPPER.get(col), na_action="ignore")
    df.to_csv("preprocessing/data/output/PROCESSED_" + f[25:-4] + ".csv")
