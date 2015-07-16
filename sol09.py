#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

for a in range(1, 201):
     for b in range(a, 401):
         c = 1000 - (a + b)
         if c*c == a*a + b*b:
             # print a, b, c
             print a*b*c
             break