"""
1. Pseudo Random: For computer program generated random numbers(not the true random number).
But randomly generated number is not predicted logically also.

2. True Random:
 Random data from outside source/networks, our keystroke, mouse movements, etc.
    use: Security purposes like encryption/decryption keys. Digital roulette Wheels
    is one the example of it.
"""
from numpy import random
# ........ random: this module in numpy is used to generate random numbers ..........
# random.randint(): random integers each time with different numbers within specified range
num_rd = random.randint(20)
print("Random Integers Numbers: ", num_rd)

# ......... random.rand(): random n-float numbers each time with different numbers ......
num_rd_flt = random.rand(10)
print("Random 10 Float Numbers: ", num_rd_flt)

# .......... random 1D Array with size specification as parameter: ...........
# Array of Integers :
print("Random Integers of 20 elements within 0 to 500: ")
ran_arr_int = random.randint(500, size=20)
print(ran_arr_int)

# ........... 2d Integer Array generation: creating 4 rows each containing 3 elements: ...........
# ranadom.randint(50, size=(4, 3))
rd_2d = random.randint(50, size=(4, 3))
print("Generated Random 2d Array 4 rows with 3 elements each:\n", rd_2d)

# .......... 1d Float Array generation:
# creating 3 rows each containing 4 elements: .................
# ranadom.rand(7)
rdf_1d = random.rand(7)
print("Generated Random 1d Float-Array with 7 elements :\n", rdf_1d)

# ........ 2d Float Array generation: creating 3 rows each containing 4 elements: ........
# ranadom.rand(4, 3)
rdf_2d = random.rand(4, 3)
print("Generated Random 2d Float-Array 3 rows with 4 elements each:\n", rdf_2d)


# ..................... Generate Random Number from Array: ................
# choice() :
#   1. generate random value from array values:
#   2. takes array as a parameter & return one of the value
# my_random_array = random.randint(100, size=5) # or(below declared array manual)
# 2.
choose_ = random.choice([0, 22, 70, 5, 100])
print("Returned one of Value From Array: ", choose_)

# 1. ............ Generate 2D new array from existed array: ..........
# Random array generation : let's create 2D array:
print("Random Array with 4 rows along with 5 elements (using above 5 values): ")
choice_2d = random.choice([0, 22, 70, 5, 100], size=(4, 5))
print(choice_2d)
