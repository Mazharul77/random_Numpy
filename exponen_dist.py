"""
Exponential Distribution: Describing 'time' till next event e.g. failure/success etc
-> with 2 parameters:
                    1. scale = inverse of Rate(lam-in poisson distribution): defaults=1.0
                    2. size= shape of returned array
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Drawing exponential_dist with scale=3.0 with 3X3 size:
expon_dist = random.exponential(scale=3, size=(3, 3))
print("The exponential_dist with scale=3.0 with 3X3 size: ", expon_dist)

""" .............. Visualizing Exponential Distribution:............ """
sns.distplot(random.exponential(size=1000), hist=False)
plt.show()

""" ...................Relation Between:..............
     Poisson:  Deals with "No. of Occurrences" of an event in a time period
     Exponential Distribution: Deals with the "Time" between these events
"""

#
