from Filter import Filter
from Pipeline import Pipeline
from read_data import read_data
from ProhibitedIngredients import filterProhibitedIngredients
from UnhealthyIngredients import filterUnhealthyIngredients

# --------- PIPES AND FILTER -----------

df = read_data("data/sephora.csv")

pipeline = Pipeline()

# could be executed in parallel
filterUnhealthy = Filter("Unhealthy Ingredients Filter", filterUnhealthyIngredients)
filterProhibited = Filter("Prohibited Ingredients Filter", filterProhibitedIngredients)

pipeline.add(filterUnhealthy)
pipeline.add(filterProhibited)

pipeline.execute(df)

df.to_csv("data/sephora_filtered.csv")

print("\n----------------")
print("-----RESULTS----")
print("----------------\n")

print(df[["isUnhealthy", "isProhibited"]])
