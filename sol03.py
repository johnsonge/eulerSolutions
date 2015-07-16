# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

n = 600851475143
prime = []

#Finding Primes
#Stop searching for primes after sqrt(n) is reached (only odd)
i = 2
for i in range(2, int(n**0.5)):
	if n % i == 0:
		n = n / i
		prime.append(i)
		print prime