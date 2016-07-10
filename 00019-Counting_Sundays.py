#
# Counting Sundays
# Problem 19
#
# You are given the following information, but you may prefer
# to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4,
# but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the
# twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
import time
import calendar
import datetime

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def problem00019():
	start_date = datetime.date(1901,1,1)
	end_date = datetime.date(2000,12,31)
	num_sundays = 0
	
	while start_date <= end_date:
		if start_date.day == 1 and calendar.weekday(start_date.year, start_date.month, start_date.day) == 6:
			num_sundays += 1
		start_date += datetime.timedelta(1)
	return num_sundays

print(time_execution("problem00019()"))
# (171, 0.02407249689654698)