#Homework - create a FIZZBUZZ game:
#take a number as input, then pass the number to a loop. 
#Check each number up to the passed one. If the number is divisble by 3 - print FIZZ, if it is divisible by 5 - print BUZZ, if it's divisible by both - FIZZBUZZ.


UserInput = int(input("Enter Any Number :"))


for number in range(UserInput + 1):

  if (number % 5 == 0 and number % 3 == 0):
    print( number, " : ", "FIZZBUZZ")
  else:
    if (number % 3 == 0):
      print(number, " : ", "FUZZ")
    elif (number % 5 == 0):
      print(number, " : ", "BUZZ")
    else:
      print(number, " : ", "The Number is Indivisible")