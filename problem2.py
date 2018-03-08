# The fibonacci sequence whose values do not exceed four million,
# find the sum of the even valued terms.

def fibonacci_iter(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print sum(a for a in fibonacci_iter(4000000))
