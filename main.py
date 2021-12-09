from Filter import Filter
from Pipeline import Pipeline
from read_data import read_data
from ProhibitedIngredients import filterProhibitedIngredients
from UnhealthyIngredients import filterUnhealthyIngredients

df = read_data("data/sephora.csv")

pipeline = Pipeline()

filterUnhealthy = Filter("Unhealthy Ingredients Filter", filterUnhealthyIngredients)
filterProhibited = Filter("Prohibited Ingredients Filter", filterProhibitedIngredients)

pipeline.add(filterUnhealthy)
pipeline.add(filterProhibited)

pipeline.execute(df)

df.to_csv("data/sephora_filtered.csv")
print(df)
