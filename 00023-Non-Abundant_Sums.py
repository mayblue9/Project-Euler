#
# Non-Abundant Sums
# Problem 23
#
# A perfect number is a number for which the sum of its proper divisors
# is exactly equal to the number. For example, the sum of the proper
# divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
# is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is
# less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
# smallest number that can be written as the sum of two abundant numbers
# is 24. By mathematical analysis, it can be shown that all integers
# greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be
# expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.
#
import time
import functools

LARGEST = 28123

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def factors(n):
	f = list(set(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
	f.remove(n)
	return f

def problem00023():
	list_of_nums = []
	for i in range(12,LARGEST):
		if sum(factors(i)) > i:
			list_of_nums.append(i)

	temp_list = set()

	for i in list_of_nums:
		for j in list_of_nums:
			if i + j < LARGEST:
				temp_list.add(i + j)

	n = 1
	total = 0
	while n < LARGEST:
		if n not in temp_list:
			total += n
		n += 1
	return total

print(time_execution("problem00023()"))
# (4179871, 5.810848837175282)
