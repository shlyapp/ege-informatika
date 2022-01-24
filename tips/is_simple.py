def is_simple(num):
	return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))