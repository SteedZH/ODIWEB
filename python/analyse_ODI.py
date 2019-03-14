import pandas as pd

df = pd.read_csv("../dataset.csv")  # raw data

df1 = df["country_long"].value_counts()  # number of plants in countries
fuel = df["fuel1"].value_counts()
df2 = df[["country_long", "capacity_mw", "latitude", "longitude", "fuel1"]]  # choosing rows
# df3 = df.loc[df["capacity_mw"].isnull(), :]
df3 = df2.dropna()  # get rid of row contained null
# df4 = df[df["country"] == "North Vietnam"]
# print(len(df), len(df1), len(df2), len(df3))

# df3.to_csv("refine.csv", index=False)

country = pd.read_json("countries.json")
country = country.loc[["name", "continent"]]

country.replace({
    "AF": "Africa",
    "AN": "Antarctica",
    "AS": "Asia",
    "EU": "Europe",
    "NA": "North America",
    "OC": "Oceania",
    "SA": "South America"
}, inplace=True)

# country_name = df1.index.values
df1 = df1.reset_index()
df1 = df1.rename(columns={"index": "country", "country_long": "plant_number"})

country = country.stack()
# country.to_csv("test.csv", index=True)
country = pd.read_csv("country_continent.csv")

result = pd.merge(df1, country, how='left', on="country")

# df_test = result[result["continent"].isnull()]
# result.loc["Myanmar", "continent"] = "Asia"
# result.loc["syrian arab republic", "continent"] = "Asia"
# result.loc["brunei Darussalam", "continent"] = "Asia"
# result.loc["Rhodesia", "continent"] = "Africa"

# result.to_csv("join.csv")
result = pd.read_csv("join.csv")
test = result["continent"].value_counts()

pd.concat([result, pd.DataFrame(columns=["Hydro",
                                         "Gas",
                                         "Solar",
                                         "Wind",
                                         "Oil",
                                         "Coal",
                                         "Biomass",
                                         "Waste",
                                         "Geothermal",
                                         "Nuclear",
                                         "Other",
                                         "Cogeneration",
                                         "Wave and Tidal"])], sort=False)

result = pd.concat(
    [
        result,
        pd.DataFrame(
            0,
            index=result.index,
            columns=["Hydro",
                     "Gas",
                     "Solar",
                     "Wind",
                     "Oil",
                     "Coal",
                     "Biomass",
                     "Waste",
                     "Geothermal",
                     "Nuclear",
                     "Other",
                     "Cogeneration",
                     "Wave and Tidal"]
        )
    ], axis=1
)

for index, row in df3.iterrows():
    # print(result[row.fuel1])
    #
    # if string == row.country_long:

    print(row.fuel1)
    result.loc[result["country"] == row.country_long, row.fuel1] += 1
    #
    # else:
    #
    #     string = row.country_long
    #     result.loc[result[row.country_long] == row.country_long, row.fuel1] = result[row.fuel1] + 1

print("hello")
