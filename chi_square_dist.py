"""
 Chi Square Distribution: Basis of Hypothesis verification
 -> with 2 parameters:
                      1. df : degree of freedom
                      2. shape of the returned array
"""
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

# with 3-df & 4X2 chi-square _distribution(sample creation):
chi_sq_dist = random.chisquare(df=2, size=(4, 2))
print("3-df & 4X2 chi-square _distribution(sample created): ", chi_sq_dist)

""" Visually chisquare distribution: """
sns.distplot(random.chisquare(df=3, size=(4, 2)), hist=False)
plt.show()