import pandas as pd
from datasets import *
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(OWID['covid'])

germany = data[data["location"] == "Germany"]
germany = germany[["date", "new_cases", "weekly_hosp_admissions", "icu_patients", "new_deaths", "people_fully_vaccinated", "people_vaccinated"]]
germany['date'] = pd.to_datetime(germany['date'])
germany = germany.set_index('date')
germany['cases_7dayaverage'] = germany["new_cases"].rolling(7).mean()
germany['weekly_deaths'] = germany['new_deaths'].resample('w', origin='2020-03-22').sum()


print(germany)
germany.to_clipboard()

# sns.lineplot(data=germany, x='date', y='cases')
# plt.show()