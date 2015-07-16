# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

n = 2000000
primes = []

while i  < n:
	if n < 0:
		pass
	for i in range(2, int(n**0.5)):
		if n % i == 0:
			primes.append(i)
	print primes