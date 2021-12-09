import pandas as pd
from ColumnNames import column_names

prohibitedIngredients = "Bithionol, Chlorofluorocarbon propellants, Chloroform, Halogenated salicylanilides, Hexachlorophene, Mercury, Methylene chloride, BSE, Vinyl chloride, Zirconium, Bithionol, Chlorofluorocarbon propellants, Chloroform, Halogenated salicylanilides, Hexachlorophene, Mercury, Methylene chloride, Potassium bromate, Carrageenan, Yellow No, rBGH, rBST"

prohibitedIngredientsList = prohibitedIngredients.split(",")

for i in range(len(prohibitedIngredientsList)):
    prohibitedIngredientsList[i] = prohibitedIngredientsList[i].strip().lower()

def filterProhibitedIngredients(df: pd.DataFrame):
    ingredients = df["raw_ingrediat_desc"]
    isProhibited = []
    prohibitedFound = False
    for i in range(len(ingredients)):
        for j in range(len(prohibitedIngredientsList)):
            if type(ingredients[i]) is float:
                break
            if ingredients[i].lower().find(prohibitedIngredientsList[j]) != -1:
                prohibitedFound = True
                break
        isProhibited.append(prohibitedFound)
        prohibitedFound = False
    df.insert(len(column_names), "isProhibited", isProhibited, True)
    return df