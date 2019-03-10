import pandas as pd

df = pd.read_csv("dataset.csv")
df1 = df["country_long"].value_counts()
print(df1)