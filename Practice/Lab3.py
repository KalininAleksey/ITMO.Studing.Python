import math
import random
import statistics
from random import randint

help(math)
help(statistics)
intList = [22, 32, 45, 12, 43, 45, 11, 49, 52, 90]
print("Sum of list elements", intList, " is ", sum(intList, 0))
print("Average of list elements", intList, " is ", statistics.mean(intList))
print("Median of list elements", intList, " is ", statistics.median(intList))
print("Standard deviation of list elements", intList, " is ", statistics.median(intList))
help(random.randint)
print(randint(1, 100))
