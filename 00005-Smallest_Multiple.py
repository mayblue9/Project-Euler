#
# Smallest Multiple
# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?
#
# Where "evenly divisible" means no remainder.
#
import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

# Code from user "lassevk" on Project Euler forums
# I originally computed the answer by hand first
def problem00005(n):
	i = 1
	for k in (range(1, n+1)):
		if i % k > 0:
			for j in range(1, n+1):
				if (i*j) % k == 0:
					i *= j
					break
	return i

print(time_execution("problem00005(20)"))
# (232792560, 4.183773570663496e-05)