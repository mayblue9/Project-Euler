#
# Longest Collatz Sequence
# Problem 14
#
# The following iterative sequence is defined for the set of positive integers:
#
#   n -> n/2 (n is even)
#   n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
#   13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
# that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def get_collatz_count(n):
	i = 1
	while n != 1:
		if n % 2 == 0:
			n /= 2
			i += 1
		else:
			n = 3 * n + 1
			i += 1	
	return i

def problem00014(n):
	largest, lcn = 0, 1
	count = 1
	while count < n:
		cn = get_collatz_count(count)
		if cn > largest:
			largest, lcn = cn, count
		count += 1
	return lcn

print(time_execution("problem00014(999999)"))
# (837799, 12.439175485757017)