print("--- Running Total Calculator ---")
print("Enter numbers to add them up. Type 'done' to see the total.")
total =0
while True:
    i = input("Enter a number or 'done': ")
    if i == "done":
        break
    number = float(i)
    total += number
    print(f"Current total: {total} ")
print("--- Final Calculation ---")
print(f"The final sum of all numbers is: {total}")