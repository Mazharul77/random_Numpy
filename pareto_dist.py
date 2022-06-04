"""
Pareto Distribution: 40-10 distribution [10% factors cause 40% outcome]
 (following Pareto's law)
 ==> uses 2 parameters:
                        1. a - shape parameters
                        2. size - shape of the returned array

 """
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Pareto Distribution with shape 2 along with size 2X3:
pareto_dist = random.pareto(a=2, size=(2, 3))
print("Pareto Distribution with shape 2 along with size 2X3: ", pareto_dist)

# Pareto Distribution Visualization :
sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()
