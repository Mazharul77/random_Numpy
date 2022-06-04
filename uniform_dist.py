"""
 Uniform Distribution: Equal Chances-Probability Distribution
 -> For Example: Generation Of Random Numbers;
 -> With 3 Parameters:
                    1. a = upper bound,
                    2. b = lower bound,
                    3. shape = Returned Array's Shape
 """

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generation Of 3X4 random distribution:
unif_dist = random.uniform(size=(3, 4))
print("Generated 3X4 random distribution: ")
print(unif_dist)

""" ........... Visually Distributing Unoform Distribution:........... """
sns.distplot(random.uniform(size=(3, 4)))
plt.show()

# Without Histogram Plotting The Uniform Distribution

sns.distplot(random.uniform(size=(3, 4)), hist=False)
plt.show()