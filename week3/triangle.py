height = int(input("Enter the height of triangle: "))
print("--- Triangle Pattern Printer ---")
print(f"Enter the desired height of the triangle: {height}")
for row_num in range (height +1):
    for col_num in range (row_num):
        print("* ", end="")
    print()