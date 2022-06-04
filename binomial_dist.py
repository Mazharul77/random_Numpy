"""
Binomial Distribution: Discrete Distribution
 -> as outcome of Binary Scenario : result of coin's toss
 -> with 3 parameters (n, p, size) : n(no. of trials), p(occurrence probability), size(returned array's shape)

"""
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

# let's find binomial distribution:
# for n = 5 trials(tossing a coin), p =.5 (with probability) & generating 5 data points:
bin_dist = random.binomial(n=5, p=.5, size=5)
print("The Binomial Distribution(5-trials for 5-data & p=.5): ", bin_dist)

"""
 ############# Visualization of Binomial Distribution: #############
"""
sns.distplot(random.binomial(n=5, p=.5, size=5), hist=True, kde=False)  # without density curve, with histogram
plt.show()

sns.distplot(random.binomial(n=5, p=.5, size=5), hist=False, kde=True)  # with density curve but without histogram
plt.show()

sns.distplot(random.binomial(n=5, p=.5, size=1000), hist=False, kde=True)  # with data-size=1000 & density-curve but without hist
plt.show()


""" ............ Normal Dist_ VS Binomial Dist_: """

sns.distplot(random.normal(loc=11, scale=3, size=20), hist=False, label='normal')
sns.distplot(random.binomial(n=7, p=.5, size=10), hist=False, label='binomial')
plt.show()