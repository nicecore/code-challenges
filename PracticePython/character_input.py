

def year_100(age):
    return (100-32) + 2018

name = input("What's your name, pardner? ")
age = int(input("And how many candles were on your last birthday cake? "))

message = "Well I'll be, %s! You'll turn 100 in "
      "the year %s! How's that feel?" % (name, year_100(age)))

