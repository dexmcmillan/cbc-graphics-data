import pandas as pd
from datasets import *

cases = pd.read_csv(OWID['covid'])

COUNTRIES = [
    'Singapore',
    'Malaysia',
    'Thailand',
    'Vietnam',
    'Philippines',
    'South Korea',
    'Korea, South'
]

print(cases.columns)

included_countries = cases[cases["location"].isin(COUNTRIES)]
included_countries = included_countries.sort_values('date', ascending=False).drop_duplicates(['location'])

export = included_countries[['location', 'total_cases_per_million']]

print(export)
export.to_clipboard()

# print(export)
# export.to_clipboard()