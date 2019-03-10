import pandas as pd

df = pd.read_csv("../dataset.csv")  # raw data

df1 = df["country_long"].value_counts()  # number of plants in countries

df2 = df[["country_long", "capacity_mw", "latitude", "longitude", "fuel1"]]  # choosing rows
# df3 = df.loc[df["capacity_mw"].isnull(), :]
df3 = df2.dropna()  # get rid of row contained null
# df4 = df[df["country"] == "North Vietnam"]
# print(len(df), len(df1), len(df2), len(df3))

df3.to_csv("refine.csv", index=False)

