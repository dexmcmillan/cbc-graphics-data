import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datasets import *

birds = pd.read_csv('./data/birds.csv')

included_birds = [
443,
446,
449,
451,
459,
460,
462,
468,
470,
473,
479,
480,
481,
482,
484,
485,
489,
495,
496,
497,
498,
499,
501,
502,
504,
505,
506,
507,
508,
511,
515,
518,
520,
522,
523,
524,
527,
531
]

filter = birds[["Sort Order_Ordre de tri", "English Name_Nom anglais", "Year_Année", "Annual Index_Indice annuel"]]
filter.columns = ["sort_order", "name", "year", "value"]

filter["value"] = filter["value"].astype('int')
filter["sort_order"] = filter["sort_order"].astype('int')

filter = filter[filter["sort_order"].isin(included_birds)]


print(filter)

# grid = sns.FacetGrid(data=latest, col="prname", col_wrap=3)
# grid.map(sns.lineplot, "date", "rateactive", color="#C42127").set_titles(col_template="{col_name}", row_template="{row_name}")
# grid.set_axis_labels("Date", "Rate")
# # grid.set(xticks=["2021-10-13", "2021-10-16", "2021-10-19"])
# # grid.set_xticklabels(["Oct. 13/21", "Oct. 16/21", "Oct. 19/21"])

# for axis in grid.axes.flat:
#     axis.tick_params(labelbottom=True)
#     axis.tick_params(labelleft=True)



# plt.savefig("./charts/covid_cases_by_province_facet.svg", format="svg")
# plt.show()
