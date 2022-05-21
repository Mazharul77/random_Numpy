"""
random.normal()
--> Normal Gaussian(German Mathmatician CArl Friedrich Gauss) Distribution:
--> Heartbeat, IQ Scores, and so on probability distributions
    are fitted by 'Normal Gaussian Distribution'
"""
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# .................. random.normal():....................
# 1. return normal distribution.........
# with 3 parameters:
#                   -> loc (mean): where the peak-bell value exists
#                   -> scale (standard deviation) : how flat the graph distribution should be
#                   -> shape (size/no. elems): Returned Array's shape

norm_rd = random.normal(size=(3, 4))
print("Generated 3X4 Normal Dist. Array:\n", norm_rd)

# Normal Distribution along with 'mean' & 'standard deviation' :
norm_dist_gen_ = random.normal(loc=2, scale=3, size=(3, 4))
print("\n\tNorm_Dist with loc(mean)-2, scale(std_dev)-3 & 3X4(shape):\n", norm_dist_gen_)

# ......... Visualize Normal Distribution: (without histogram) ................
sns.distplot(random.normal(size=1000), hist=False)
plt.show()

"""
 Curve of A Normal Distribution: Is also called as 'Bell Curve'(Because of Bell-Shaped Curve).....
 """