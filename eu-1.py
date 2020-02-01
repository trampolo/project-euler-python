# Multiples of 3 and 5

# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

multiples_3 = [x for x in range(3, 1000, 3)]
multiples_5 = [x for x in range(5, 1000, 5)]
multiples_3_5 = set(multiples_3) | set(multiples_5)
sum_of_multiples_3_5 = 0
for n in multiples_3_5:
	sum_of_multiples_3_5 = sum_of_multiples_3_5 + n

print(sum_of_multiples_3_5)