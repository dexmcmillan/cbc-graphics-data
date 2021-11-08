import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datasets import *

vaccines = pd.read_csv(OWID['global_vaccines'])

exclusions = [
    "World",
    "High income",
    "Upper middle income",
    "Lower middle income",
    "Oceania",
    "Asia",
    "Europe",
    "North America",
    "European Union",
    "South America"
    ]

boosters = (vaccines[['location','date','total_boosters']]
                .sort_values('date', ascending=False)
                .drop_duplicates(['location'])
                .dropna()
                .sort_values('total_boosters', ascending=False)
                
                )

boosters = boosters[~boosters['location'].isin(exclusions)]

print(boosters)
boosters.to_clipboard()