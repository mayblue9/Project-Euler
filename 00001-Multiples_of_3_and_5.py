#
# Multiples of 3 and 5
# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def problem00001(n):
	sum = 0
	for i in range(1,1000):
		if i % 3 == 0 or i % 5 == 0:
			sum += i
	return sum

print(time_execution("problem00001(1000)"))
