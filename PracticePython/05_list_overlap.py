import random

# Two lists, each 14 elements long, from random integers between 0 and 10
a = [random.randint(0,10) for x in range(1, 15)]
b = [random.randint(0,10) for x in range(1, 15)]

# Convert the two lists into sets
a = set(a)
b = set(b)

# Listify the intersection of set a with set b
intersect = list(a.intersection(b))

print(intersect)
