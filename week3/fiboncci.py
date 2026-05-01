print("--- Fibonacci Sequence Generator ---")
num = int(input("How many Fibonacci numbers would you like to generate? "))
a = 0
b = 1
for i in range(num):
    print( a, end=', ' if i< num -1 else " ")
    a, b = b,a+b