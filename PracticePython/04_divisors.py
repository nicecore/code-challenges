# Divisors

an_integer = int(input("Please enter a number:\n> "))

listRange = list(range(1, an_integer+1))

divisorList = []

for number in listRange:
    if an_integer % number == 0:
        divisorList.append(number)

print(divisorList)
