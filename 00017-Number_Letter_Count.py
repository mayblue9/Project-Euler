#
# Number Letter Counts
# Problem 17
#
# If the numbers 1 to 5 are written out in words: one,
# two, three, four, five, then there are
# 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive
# were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three
# hundred and forty-two) contains 23 letters and 115 (one hundred
# and fifteen) contains 20 letters. The use of "and" when writing
# out numbers is in compliance with British usage.
#
import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

num_words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
			6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
			11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
			15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
			19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
			50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
			90: 'Ninety', 0: 'Zero'}

def problem00017(n):
	sum = 0
	position, count = 1, 1
	while position <= n:
		thousands = int(count / 1000)
		count %= 1000
		hundreds = int(count / 100)
		count %= 100
		if count < 20:
			tens = 0
		else:
			tens = int(count / 10)
			count %= 10
		if count != 0:
			sum += len(num_words[count])
		if tens != 0:
			sum += len(num_words[tens * 10])
		if hundreds != 0:
			if tens + count != 0:
				sum += (len(num_words[hundreds]) + 10)
			else:
				sum += (len(num_words[hundreds]) + 7)
		if thousands != 0:
			sum += (len(num_words[thousands]) + 8)
		position += 1
		count = position
	return sum

print(time_execution("problem00017(1000)"))
# (21124, 0.001258349990403655)