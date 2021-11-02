import pandas as pd
from datawrapper import new_chart
import seaborn as sns
import matplotlib.pyplot as plt
from datasets import *

vaccines = pd.read_csv(VACCINES['global'])

dates = vaccines.columns[4:]

# pivot = vaccines.melt(id_vars=["location", ""], value_vars=dates)

countries = ["Chile", "Argentina", "Mexico", "Costa Rica", "Argentina", "Brazil", "Ecuador", "Panama", "Bolivia", "Peru", "Colombia", "El Salvador", "Venezuela", "Paraguay", "Guatemala", "Honduras", "Uruguay", "Nicaragua", "Cuba"]

included_countries = vaccines[vaccines["location"].isin(countries)]
included_countries = included_countries.sort_values('date', ascending=False).drop_duplicates(['location'])

included_countries["one_dose"] = included_countries["people_vaccinated_per_hundred"] - included_countries["people_fully_vaccinated_per_hundred"]
included_countries["two_doses"] = included_countries["people_fully_vaccinated_per_hundred"]
export = included_countries[["location", "date", "one_dose", "two_doses"]]
print(export)
export.to_clipboard()