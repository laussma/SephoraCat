import pandas as pd
from ColumnNames import column_names

unhealthyIngredients = "Parabens, Sodium Laureth Sulfate, SLES, Sodium Lauryl Sulfate, SLS, Diethanolamine, DEA, Triethanolamine, TEA, Triclosan, Octinoxate, Oxybenzone, Formaldehyde, PEG-10 Laurate, Butylated hydroxyanisole, BHA, Butylated Hydroxytoluene, BHT, Benzalkonium Chloride, Hydroquinone, Methylisothiazolinone, Methylchloroisothiazolinone, Toluene, Triclocarban, 1,4-DIOXANE, ACRYLATES, BENZOPHENONE, CARCINOGENS, CARBON BLACK, COAL TAR, MEA, DEA, TEA, FRAGRANCE, HYDROQUINONE, MICA, NITROSAMINES, OCTINOXATE, PABA, MORE, PETROLATUM, PETROLEUM JELLY, P-PHENYLENEDIAMINE, PRESERVATIVES, PHTHALATES, QUATERNIUM-15, RESORCINOL, RED LIST, STYRENE ACRYLATES COPOLYMER, RETINOL AND RETINOL COMPOUNDS, SYNTHETIC MUSKS, TALC, TITANIUM DIOXIDE, TOLUENE, TRICLOSAN"

unhealthyIngredientsList = unhealthyIngredients.split(",")

for i in range(len(unhealthyIngredientsList)):
    unhealthyIngredientsList[i] = unhealthyIngredientsList[i].strip().lower()

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