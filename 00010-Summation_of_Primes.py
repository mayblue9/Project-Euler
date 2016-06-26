#
# Summation of Primes
# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
import time
import math

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

# Using the Sieve of Erotaosthenes algorithm found at:
#  https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def problem00010(n):
	A = {}
	for i in range(2, n + 1):
		A[i] = True
	
	for i in range(2, 1 + int(math.sqrt(n))):
		if A[i]:
			for j in range(i**2, n+1, i):
				A[j] = False
	sum = 0
	for i in range(2, n + 1):
		if A[i]:
			sum += i
	return sum

print(time_execution("problem00010(2000000)"))
# (142913828922, 0.6681524400573088)