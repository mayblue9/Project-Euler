#
# Amicable Numbers
# Problem 21
#
# Let d(n) be defined as the sum of proper divisors of
# n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a =/= b, then a and b
# are an amicable pair and each of a and b are called
# amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4,
# 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220)
# = 284. The proper divisors of 284 are 1, 2, 4, 71 and
# 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
#
import time
import numpy as np

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def amicable_pair(n):
	factors = set()
	i = 1
	while i < n:
		if n % i == 0:
			factors.add(i)
		i += 1
	x = np.array(list(factors)).sum()
	factors = set()
	i = 1
	while i < x:
		if x % i == 0:
			factors.add(i)
		i += 1
	y = np.array(list(factors)).sum()
	if y == n and x != n:
		return int(y), int(x)
	else:
		return None, None

def problem00021(n):
	ami_nums = set()
	
	for i in range(n):
		x,y = amicable_pair(i)
		if x and y:
			ami_nums.add(x)
			ami_nums.add(y)
	return np.array(list(ami_nums)).sum()

print(time_execution("problem00021(10000)"))
# (31626, 14.887486267413506)