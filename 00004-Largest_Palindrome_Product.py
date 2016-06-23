#
# Largest Palindrome Product
# Problem 4
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def is_palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

def problem00004():
	a, b = 999, 999
	num = 0
	while a > 100:
		while b > 100:
			if is_palindrome(str(a * b)):
				if (a * b) >= num:
					num = a * b
				else:
					break
			b -= 1
		a -= 1
		b = 999
	return num

print(time_execution("problem00004()"))
# (906609, 0.22996623431414054)