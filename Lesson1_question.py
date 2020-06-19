# Prints the numbers 1..100
# For multiples of 3, prints "Fizz" instead of the number
# For multiples of 5, prints "Buzz" instead of the number
# For multiples of 3 and 5, prints "FizzBuzz" instead of the number
# Coding style should be PEP8 (4 spaces for indentation)

def FizzBuzz():
    for element in range(1, 101):
        if element % 3 == 0 and element % 5 != 0:
            print("Fizz")
        elif element % 5 == 0 and element % 3 != 0:
            print("Buzz")
        elif element % 5 == 0 and element % 3 == 0:
            print("FizzBuzz")
        else:
            print(element)

# Where I got with 5 minutes
print(FizzBuzz())
