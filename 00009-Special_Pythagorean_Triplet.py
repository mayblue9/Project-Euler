#
# Special Pythagorean Triplet
# Problem 9
#
# A Pythagorean triplet is a set of three natural numbers,
#  a < b < c, for which,
#
#  a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
import time
import math

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def problem00009(n):
	square_list = {}
	for i in range(1, n + 1):
		square_list[i] = i**2
	for a in range(n, 0, -1):
		b = 1
		while b <= 1000:
			c_int = int(math.sqrt(square_list[a] + square_list[b]))
			c_float = math.sqrt(square_list[a] + square_list[b])
			if c_int != c_float:
				b += 1
			elif a + b + c_int == 1000:
				print(a, b, c_int)
				return a*b*c_int
			else:
				b += 1

print(time_execution("problem00009(1000)"))
# (31875000, 0.4891118215386722)