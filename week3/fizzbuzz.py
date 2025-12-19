number = int(input("Enter number from 1 to 100: "))
print("--- FizzBuzz Challenge (1-100) ---")
for number in range(1,number + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)