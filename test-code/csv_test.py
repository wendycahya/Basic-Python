import pandas as pd

# read CSV file
data = pd.read_csv("data.csv")

# calculate mean of column "x"
a = data["x"].iloc[3]
b = data["y"].iloc[3]

print(len(data.columns))