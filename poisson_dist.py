"""
Poisson Distribution: Discrete Distribution Like Binomial_Dist
 -> Frequency of Event with Time (How many times Occur)/event's occurrence probability
 -> With 2 Parameters:
                    1. lam = no. of occurrences or rate
                    2. size = Returned Array's Size.
"""
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

poiss_dist = random.poisson(lam=3, size=15)  # 3 times occurrences with 1X15 distribution:
print("Poisson_Dist of 3 times occurrences with 1X15 distribution: ", poiss_dist)

""" Visually Poisson Distribution :  """
sns.displot(random.poisson(lam=0, size=10), kde=False)
plt.show()


""" 
        Normal Distribution: Continuous
              VS
        Poisson Distribution: Discrete

###  similar to binomial
 for a large enough poisson distribution it will become similar to normal distribution
  with certain std dev and mean
"""

sns.distplot(random.normal(loc=2, scale=1, size=50), hist=False, label='normal')
sns.distplot(random.poisson(lam=10, size=100), hist=False, label='poisson')
plt.show()

"""
 Binomial: Discrete
            VS (subtle difference)
 Poisson:  Continuous(Here- For large )
  
  ->  For large 'n' and near-zero 'p' binomial distribution:
        is near identical to 'poisson distribution' such that 'n' * 'p' is nearly equal to 'lam'
"""

sns.distplot(random.binomial(n=1000, p=0.1, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=100, size=1000), hist=False, label='poisson')
plt.show()
