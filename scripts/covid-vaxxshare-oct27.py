import pandas as pd
from datawrapper import new_chart
import seaborn as sns
import matplotlib.pyplot as plt
from datasets import *

vaccines = pd.read_csv(OWID['global_vaccines'])
population = pd.read_csv(OWID['population'])

dates = vaccines.columns[4:]

# pivot = vaccines.melt(id_vars=["location", ""], value_vars=dates)

continents = ["Africa", "Asia", "Europe", "North America", "Oceania", "South America"]

included_countries = vaccines[vaccines["location"].isin(continents)]
included_countries = included_countries.sort_values('date', ascending=False).drop_duplicates(['location'])

population_continents = population[population["entity"].isin(continents)]

included_countries["total"] = included_countries["total_vaccinations"]
included_countries["total_vaccinations"] = included_countries["total_vaccinations"].astype('int')
export = included_countries[["location", "date", "total_vaccinations"]]

export["vaccination_share"] = export["total_vaccinations"] / export["total_vaccinations"].sum()

merged = export.merge(population_continents, left_on="location", right_on="entity")

print(merged)
merged.to_clipboard()