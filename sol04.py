#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3 digit numbers

palindrome = []
temp = []
product = 1

for i in range (100,1000):
	for num in range (100,1000):
		product = num * i
		productStr = str(product)
		revProduStr = productStr[::-1]
		# appends palindrome numbers to array as ints		
		if productStr == revProduStr and productStr not in palindrome:
			palindrome.append(int(productStr))

print max(palindrome)