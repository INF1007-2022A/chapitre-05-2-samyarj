#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name: str, data: list[tuple]):
	INDEX_NAME = 0  # useless
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	price = 0
	for entry in data:
		price += (entry[INDEX_QUANTITY] * entry[INDEX_PRICE])
	taxe = price * 0.15
	total = price + taxe
	return f"{name}\nSOUS TOTAL{format(price, '.2f'):>12} $\nTAXES{format(taxe, '.2f'):>17} $\nTOTAL{format(total, '.2f'):>17} $"


def format_number(number, num_decimal_digits):
	neg = False
	if number < 0:
		neg = True
	number = abs(round(number, num_decimal_digits))
	decimal = number - int(number)
	number = str(int(number))
	number = number[::-1]  # reverse the number
	group = ''

	result = ''

	for digit in number:
		if len(group) < 3:
			group += digit
		else:
			result += group
			result += ' '
			group = ''
			group += digit
	result += group

	result = result[::-1]
	result += str(decimal)[1:num_decimal_digits+2]  # add decimal
	if neg == True:  # if number is -ve
		result = '-' + result
	return result

def get_triangle(num_rows):
	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
