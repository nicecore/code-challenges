import random

a = [random.randint(0, 100) for x in range(1, 15)]

b = [x for x in a if x % 2 == 0]

print(b)
