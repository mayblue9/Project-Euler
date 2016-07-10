#
# Factorial Digit Sum
# Problem 20
#
# n! means n x (n-1) x ... x 3 x 2 x 1
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is
# 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
#
# Find the sum of the digits in the number 100!
#
import time
import math

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def problem00020(n):
	return sum(int(i) for i in str(math.factorial(n)))

print(time_execution("problem00020(100)"))
# (648, 0.00013984921445994066)