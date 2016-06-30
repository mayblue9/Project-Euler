#
# Lattice Paths
# Problem 15
#
# Starting in the top left corner of a 2x2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20x20 grid?
#
import time
import math

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def problem00015(n):
	return int(math.factorial(2*n) / (math.factorial(n) * math.factorial(n)))

print(time_execution("problem00015(20)"))
# (137846528820, 3.072003370426555e-05)