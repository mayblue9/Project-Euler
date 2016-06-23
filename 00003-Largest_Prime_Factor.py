#
# Largest Prime Factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

# Pseudocode for the following algorithm can be found at:
# https://en.wikipedia.org/wiki/Primality_test
def isPrime(n):
	if n <= 1:
		return False
	elif n <= 3:
		return True
	elif n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True

def problem00003(n):
	for x in range(1, n):
		if n % x == 0:
			t = n / x
			if isPrime(t):
				return t


print(time_execution('problem00003(600851475143)'))
# (6857.0, 13.509592983197322)