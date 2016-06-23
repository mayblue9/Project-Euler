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

def problem00003(n):
	a = 0
	x = 1
	while x <= n:
		if n % x == 0:
			a = x
			n /= x
		x += 1
	return a

print(time_execution('problem00003(600851475143)'))
# (6857, 0.0015863230979117119)