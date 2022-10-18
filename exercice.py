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
	round(number, num_decimal_digits)
	decimal = number - int(number)
	number = str(abs(int(number)))
	group3 = ''
	result = ''
	for digit in number:
		if len(group3) < 3:
			group3 += digit
		if len(group3) >= 3:
			result += group3
			result += '_'
			group3 = ''
	return result
def get_triangle(num_rows):
	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
