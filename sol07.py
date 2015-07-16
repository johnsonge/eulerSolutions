#What is the 10001st prime number?

primes = []

def is_prime(n):
    if n < 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

j = 1
while len(primes) < 10001:
    j += 1
    if is_prime(j):
        primes.append(j)

print j