#
# Name Scores
# Problem 22
#
# Using p022_names.txt (right click and 'Save Link/Target As...'),
# a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working
# out the alphabetical value for each name, multiply this
# value by its alphabetical position in the list to obtain a
# name score
# 
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
# 938th name in the list. So, COLIN would obtain a score of
# 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?
#
import time
import csv

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def alpha_value(name):
	sum = 0
	for c in name:
		sum += (ord(c) - 64)
	return sum

def problem00022(n):
	list_names = []
	with open(n) as csvfile:
		names = csv.reader(csvfile, delimiter=',')
		for name in names:
			list_names = name
	list_names.sort()
	i, total = 0, 0
	test = []
	for name in list_names:
		i += 1
		total += alpha_value(name) * i
	return total

print(time_execution("problem00022('p022_names.txt')"))
# 