# Odd or even


def odd_or_even():
    an_integer = int(input("Please enter a number:\n> "))
    if an_integer % 2 != 0:
        print("You picked an odd number!")
    else:
        print("You picked an even number!")

odd_or_even()
