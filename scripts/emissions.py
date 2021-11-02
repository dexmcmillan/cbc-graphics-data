import pandas as pd
from datawrapper import new_chart
from datasets import *

COUNTRIES = [
    'South America',
    'Oceania',
    'Africa',
    'Europe',
    'Asia (excl. China & India)',
    'North America (excl. USA)',
]

df = pd.read_csv(OWID['emissions'])

all_emissions = df[['iso_code', 'country', 'year', 'cumulative_co2']]
all_emissions['year'] = all_emissions['year'].astype(int)
all_emissions = all_emissions[all_emissions['year'] == 2019]

all_emissions = all_emissions[~all_emissions['country'].isin(COUNTRIES)]

pivot = pd.pivot_table(all_emissions,columns=['iso_code', "country"]).transpose()
pivot = pivot.sort_values('cumulative_co2', ascending=False).head(25)
print(pivot)
pivot.to_clipboard()

# chart = new_chart(chart_data, pivot)