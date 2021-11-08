import pandas as pd
from datasets import *
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('./data/globalcarbonatlas.csv')
data.index = data['year'].astype('str')
data = data.transpose()
data = data.drop('year')


print(data)
data.to_clipboard()

# sns.lineplot(data=germany, x='date', y='cases')
# plt.show()