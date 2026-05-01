print("=== Book Rental System ===")
print("Enter membership type: student, regular, or premium")
print("Type 'done' when finished selecting books")
subtotal = 0
while True:
    i = input("\nEnter membership type: ")
    if i == "done":
        break
    elif i == "regular":
        price = 4
        print(f"Price: ${price: 2f}")
        subtotal = subtotal + price
        print(f"Current total: ${subtotal: 2f}")
    elif i == "premium":
        price = 6
        print(f"Price: ${price: 2f}")
        subtotal = subtotal + price
        print(f"Current total: ${subtotal: 2f}")
    elif i == "student":
        price = 2
        print(f"Price: ${price: 2f}")
        subtotal = subtotal + price
        print(f"Current total: ${subtotal: 2f}")
if subtotal >= 15:
    bulk = 2.50
    total = subtotal - bulk
else:
    bulk = 0
    total = subtotal
print("\n=== Rental Summary ===")
print(f"Subtotal: ${subtotal}")
print(f"Bulk Rental Discount: -${bulk}")
print(f"Final Total: ${total}")
print("Thank you for your rental!")