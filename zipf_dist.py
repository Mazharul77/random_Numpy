"""
zipf distribution : to sampling data based on zipf's law

    -> zipf's law : within a collection the nth common term is:
        1/n times of the most common term.
    -> Example: 3rd common word in english occurs nearly 1/3 times as of the most used word.

    ==>> 2 parameters :
            1. a-distribution parameter,
            2. size-shape of the returned array
"""
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

# distribution parameter-2 & size 2X3:
zipf_dist = random.zipf(a=2, size=(2, 3))
print("The zipf_dist with parameter-2 & size 2X3: \n", zipf_dist)


""" ............. Visualization zipf distribution:........... """
# sampling 100 points but plotting only ones:
#  with values <20 for more understanding/meaningful chart

zf_d = random.zipf(a=2, size=100)
sns.distplot(zf_d[zf_d < 20], hist=True)
plt.show()