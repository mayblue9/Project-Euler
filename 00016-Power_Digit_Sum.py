#
# Power Digit Sum
# Problem 16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
#
import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def problem00016(n):
	num = 2**n
	number = str(num)
	sum = 0
	while number:
		sum += int(number[0])
		number = number[1:]
	return sum

print(time_execution("problem00016(1000)"))
# (1366, 0.0001454080319066767)