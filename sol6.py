#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

tempSquares = []
tempSum = []

n = 100
for i in range(1,n+1):
	tempSum.append(i)
	i = i ** 2
	tempSquares.append(i)
squareOfSums = sum(tempSum) ** 2
sumOfSquares = sum(tempSquares)

print ("Sum of squares: " + str(sumOfSquares))
print ("Square of sums: " + str(squareOfSums))

print (str(squareOfSums) + " - " + str(sumOfSquares) + " = " + str(squareOfSums - sumOfSquares))