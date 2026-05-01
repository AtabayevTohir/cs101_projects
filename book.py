print("*" * 40)
print("The list of books:")
print("1. English - 30000 sum")
print("2. Math - 40000 sum")
print("3. Coding - 35000 sum")
print("*" * 40)

name = input("Enter your name: ")
staff = input("Are you faculty staff (yes/no): ")
textbook = input("Is this a textbook order (yes/no): ")

book1 = float(input("How many English books are you gonna buy: "))
book2 = float(input("How many Math books are you gonna buy: "))
book3 = float(input("How many Coding books are you gonna buy: "))

books_number = book1 + book2 + book3
price_before = book1 * 30000 + book2 * 40000 + book3 * 35000
faculty_discount = 0
textbook_discount = 0

if staff == "yes":
    faculty_discount = 0.20 * price_before
if textbook == "yes":
    textbook_discount = 0.25 * price_before

if textbook_discount >= faculty_discount:
    main_discount = textbook_discount
    applied_discount = "Textbook discount"
else:
    main_discount = faculty_discount
    applied_discount = "Faculty discount"

bulk_discount = 0
if books_number >= 10:
    bulk_discount = 0.08 * price_before

total_discount = main_discount + bulk_discount

small_order_fee = 0
if books_number < 3:
    small_order_fee = 10000

tax = 0
if textbook == "no":
    tax = 0.05 * (price_before - total_discount + small_order_fee)

shipping = 20000
if (price_before - total_discount) >= 200000:
    shipping = 0

total_price = price_before - total_discount + small_order_fee + tax + shipping

print("\n" + "*" * 40)
print("Customer name:", name)
print("Faculty staff:", staff)
print("Textbook order:", textbook)
print("Books bought:", books_number)
print("*" * 40)
print("Price before discounts:", price_before, "sum")
print("Applied discount:", applied_discount)
print("Main discount amount:", main_discount, "sum")
print("Bulk discount:", bulk_discount, "sum")
print("Total discount:", total_discount, "sum")
print("Small order fee:", small_order_fee, "sum")
print("Tax:", tax, "sum")
print("Shipping:", shipping, "sum")
print("*" * 40)
print("Final total:", total_price, "sum")
print("*" * 40)
