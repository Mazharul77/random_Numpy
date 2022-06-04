"""
Logistic Distribution: To Describe Growth
 -> Uses: In Machine Learning- In Logistic Regression, Neural Network, etc
 -> With 3 Parameters:
                      1. loc(mean) = where the peak exists(ByDefault=0),
                      2. scale(standard deviation) = dist's flatness (by default=1),
                      3. shape = returned array's Shape.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generating & Plotting Logistic_Dist of
# loc(mean)=2, std_dev=3, and 3X2 size:
logist_dist = random.logistic(loc=2, scale=3, size=(3, 2))
print(logist_dist)

""" ....... Logistic Distribution Visualization: ............"""
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()

"""   Logistic
        VS
  Normal Distribution:
  
  -> Both nearly identical
  -> but logistic_dist has more area under the tails;
  -> more possibility of occurrence of an event further away from mean
"""
sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')
plt.show()