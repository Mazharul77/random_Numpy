"""
Permutation in numpy :
 arrangement of array elements in-place or by shuffling.
 shuffle() and permutation() methods are used for this purposes.
"""

import numpy as np
from numpy import random
# shuffle() : in-place changing elements(modify original array) in the array itself
# Let's shuffling array randomly:
unshuffled_ = np.array([11, 22, 1, 0, 8, 6])
print("The Original Un_shuffled Array: ", unshuffled_)
random.shuffle(unshuffled_)
print("Now Shuffling modified original array is: ", unshuffled_)

# ................ Permutation generations of array: Without changing original one...........................
array_unperm = np.array(['B', 'h', 'u', 'i', 'y', 'a', 'n', 'M', 'a', 'z', 'h', 'a', 'r', 'u', 'l'])
print("Un-Permuted Original Array: ", array_unperm)
print("Permutation Generation Randomly from  array_unperm: ", random.permutation(array_unperm))
print("Checking: Unchanged original Array after permutation: ", array_unperm)
