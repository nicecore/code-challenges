import random

a = random.sample(range(1, 10), 7)

def less_than_five(sequence):
  lessThanFive = []
  for i in sequence:
    if i < 5:
      lessThanFive.append(i)
  print(lessThanFive)

less_than_five(a)
