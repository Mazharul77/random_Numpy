"""
 Rayleigh Distribution : In Signal Processing
==> with 2 parameters:
                    1. scale (std dev) : how flatness the distribution is;
                    2. size : The Shape of the Returned Array
"""
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#  Rayleigh Distribution - sample drawing with sacle(std_dev)=2 & size-(3x2):
rayl_dist = random.rayleigh(scale=2, size=(3, 2))
print("The Rayleigh Distribution: ", rayl_dist)


""" ............Visual Rayleigh Dist:.............."""
sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()

""" ###### Similarity : chisquare & rayleigh dist: ########## """
# At unit std_dev-2df rayleigh and chi square demonstrate are the same dist..

