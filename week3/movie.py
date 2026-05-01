age = int(input('Enter your age: '))
if age <= 12:
    print("Cost of your ticket is 8$")
elif 13 <= age <= 64:
    print("Cost of your ticket is 15$")
else:
    print("Cost of your ticket is 10$")