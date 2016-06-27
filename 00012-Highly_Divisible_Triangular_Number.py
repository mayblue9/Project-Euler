#
# Highly Divisible Triangular Number
# Problem 12
#
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
#
#  1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#   1: 1
#   3: 1,3
#   6: 1,2,3,6
#  10: 1,2,5,10
#  15: 1,3,5,15
#  21: 1,3,7,21
#  28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?
#
import time
import math

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def number_of_factors(n):
	num_factors = 0
	i = 1
	while i <= math.sqrt(n):
		if n % i == 0:
			num_factors += 1
			if i != n / i:
				num_factors += 1
		i += 1
	return num_factors

def problem00012(n):
	num, i = 1, 1
	while number_of_factors(num) < n:
		i += 1
		num += i
	return num

print(time_execution("problem00012(500)"))