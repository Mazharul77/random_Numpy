# Random Data Distribution:
"""
Data distribution: Certain probability density function
 (continuous probability)
1. In Data Science & Statistics
2. How often each value occurs (list of possible values)
3. random - Randomly generated data distributions

"""
from numpy import random

# choice()-probability : probability between 0 and 1:
# 0-means no probability to occur & 1 means - always occurs
prob_ = random.choice([11, 44, 17, 8, 90], p=[.3, .2, .4, 0.0, .1], size=20)
# p : refers probability of each values in the array respectively; where the sum of probs should be : 1
# size - here total 20 values are randomly picked except 8 since it's probability is :0.0
print("Each values random occurrence according to probability: ", prob_)

# Probable values-2D array probability in 3 rows along with 5 elements in each rows
prob_2d = random.choice([11, 44, 17, 8, 90], p=[.3, .2, .4, 0.0, .1], size=(3, 5))
print("2d Array : Each values random occurrence according to probability: ", prob_2d)
