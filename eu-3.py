# Largest prime factor
   
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

x = 600851475143
r = 2
primes = []
while r <= x:
	if x % r != 0:
		r = r + 1
	else:
		x = x / r
		primes.append(r)  

print(max(primes))
