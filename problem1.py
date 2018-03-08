# Find sum of all the multiples of 3 or 5 below 1000
list_of_numbers = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
print "The sum of all natural numbers that are multiple of either 3 or 5 \
below 1000 is: " + str(sum(list_of_numbers))
