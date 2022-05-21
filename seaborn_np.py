"""
Seaborn-Module :
1. Seaborn library using Matplot for plotting graph,
2. Visualizing the random-distribution.
"""
"""
Importing Matplotlib.pyplot Library 
"""

import seaborn as sns
import matplotlib.pyplot as plt

# after installing seaborn by-- pip install seaborn
# Distplot:
""" [We can also use 'displot' or 'kdeplot' in future code instead of 'distplot'] """
sns.distplot([5, 5, 10, 5, -10, 5, 20, 100])
plt.show()
# Distribution of plot which takes an array as input
# to plot it's value into a curve according to the points in the array:

# ............. Distploting Without Histogram: .................
sns.distplot([2, 4, 7, 8, 11, 8, 30], hist=False)
plt.show()

