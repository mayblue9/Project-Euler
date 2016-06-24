#
# Sum Square Difference
# Problem 6
#
# The sum of the squares of the first ten natural numbers is,
#
#  1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
#
#  (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.
#
import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def problem00006(n):
	s1, s2 = 0,0
	for i in range(1, n + 1):
		s1 += i**2
		s2 += i
	return s2**2 - s1

print(time_execution("problem00006(100)"))
