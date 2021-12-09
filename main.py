from read_data import read_data
from filter import filterUnhealthyIngredients

df = read_data("data/sephora.csv")
df = filterUnhealthyIngredients(df)
df.to_csv("data/sephora_filtered.csv")
print(df)