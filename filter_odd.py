#filter odd number in the list
def is_odd(n):
	return n % 2 == 1

print filter(is_odd , [1 , 2 , 3 , 4 , 5 , 6 , 9 , 10 , 16])