#
# 10001st Prime
# Problem 7
#
# By listing the first six prime numbers:
#
#  2, 3, 5, 7, 11, and 13,
#
# we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?
#
import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def largestPrime(n):
	a = 0
	x = 1
	while x <= n:
		if n % x == 0:
			a = x
			n /= x
		x += 1
	return a

def problem00007(n):
	x = 1
	i = 0
	while n >= 0:
		if x == largestPrime(x):
			n -= 1
			i += 1
		x += 1
	return x - 1

print(time_execution("problem00007(10001)"))
# (104743, 199.28019872631887)