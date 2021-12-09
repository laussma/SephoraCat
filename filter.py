import pandas as pd
from UnhealthyIngredients import unhealthyIngredientsList
from ColumnNames import column_names

def filterUnhealthyIngredients(df: pd.DataFrame):
    ingredients = df["raw_ingrediat_desc"]
    isUnhealthy = []
    unhealthyFound = False
    for i in range(len(ingredients)):
        for j in range(len(unhealthyIngredientsList)):
            if type(ingredients[i]) is float:
                break
            if ingredients[i].lower().find(unhealthyIngredientsList[j]) != -1:
                unhealthyFound = True
                break
        isUnhealthy.append(unhealthyFound)
        unhealthyFound = False
    df.insert(len(column_names), "isUnhealthy", isUnhealthy, True)
    return df