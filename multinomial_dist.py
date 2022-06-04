"""
 Multinomial Distribution: generalization of Binomial Distribution
 -> outcomes scenarios must be only one of two
 -> Blood type of a population, dice roll outcome, etc.
 -> with 3 parameters:
                        1. n = no. of possible outcomes (ex: 6 for dice roll),
                        2. pvals = list of probabilities of outcomes ([1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll),
                        3. size = Returned Array's Shape.
"""
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Dice Rolling to return sample Output:

multinom_dist = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print("Drawing out a sample for dice rol: ", multinom_dist)
# Output(Random Sample): Drawing out a sample for dice rol:  [0 0 2 2 2 0]

# ---->>> Doesn't produce single value ; produce one value for each "pval" <<<--------
# ---->>> Both visualization & similarity of normal distribution:same as multiple binomial distributions
