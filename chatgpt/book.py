# ===== Bookstore Billing Program =====

# --- Market book list (fixed) ---
books = [
    {"title": "English", "price": 30000},
    {"title": "Math", "price": 40000},
    {"title": "Coding", "price": 35000}
]

# --- Display book catalog ---
print("*" * 40)
print("The list of books available:")
for i, book in enumerate(books, start=1):
    print(f"{i}. {book['title']} - {book['price']} sum")
print("*" * 40)

# --- Customer input ---
print("\nEnter customer details:")
customer_name = input("Name: ")
is_faculty_staff = input("Is faculty/staff? (yes/no): ").lower() == "yes"
is_textbook_order = input("Is textbook order? (yes/no): ").lower() == "yes"

# --- Customer chooses quantities ---
print("\nEnter quantity for each book:")
for book in books:
    book["quantity"] = int(input(f"How many '{book['title']}' books? "))

# --- Calculations ---
number_of_books = sum(book["quantity"] for book in books)
subtotal = sum(book["price"] * book["quantity"] for book in books)

# --- Discounts ---
faculty_discount_eligible = is_faculty_staff
textbook_discount_eligible = is_textbook_order
bulk_discount_eligible = number_of_books >= 10

faculty_discount = 0.20 * subtotal if faculty_discount_eligible else 0
textbook_discount = 0.25 * subtotal if textbook_discount_eligible else 0
bulk_discount = 0.08 * subtotal if bulk_discount_eligible else 0

# Faculty & textbook discount do not stack — apply the larger
if faculty_discount >= textbook_discount:
    main_discount = faculty_discount
    applied_discount_type = "Faculty/Staff Discount"
else:
    main_discount = textbook_discount
    applied_discount_type = "Textbook Discount"

# Bulk discount stacks with main discount
total_discounts = main_discount + bulk_discount

# --- Small order fee ---
small_order_fee_applied = number_of_books < 3
small_order_fee = 10000 if small_order_fee_applied else 0

# --- Subtotal after discounts and fees ---
subtotal_after_discounts = subtotal - total_discounts + small_order_fee

# --- Tax ---
tax_exempt = is_textbook_order
tax = 0 if tax_exempt else 0.05 * subtotal_after_discounts

# --- Shipping ---
free_shipping = subtotal_after_discounts >= 200000
shipping = 0 if free_shipping else 20000

# --- Final total ---
final_total = subtotal_after_discounts + tax + shipping
net_savings = total_discounts - (small_order_fee + shipping + tax)

# --- Output ---
print("\n" + "*" * 40)
print("RECEIPT SUMMARY")
print("*" * 40)
print(f"Customer Name: {customer_name}")
print(f"Faculty/Staff: {is_faculty_staff}")
print(f"Textbook Order: {is_textbook_order}")
print(f"Total Number of Books: {number_of_books}")

print("\n" + "*" * 40)
print("Itemized List of Purchased Books:")
for i, book in enumerate(books, start=1):
    total_price = book["price"] * book["quantity"]
    print(f"{i}. {book['title']} - {book['quantity']} x {book['price']} sum = {total_price} sum")
print("*" * 40)

print(f"Subtotal before discounts: {subtotal:.2f} sum")
print("\n--- Discounts ---")
print(f"Faculty discount eligible: {faculty_discount_eligible}, amount: {faculty_discount:.2f}")
print(f"Textbook discount eligible: {textbook_discount_eligible}, amount: {textbook_discount:.2f}")
print(f"Applied main discount: {applied_discount_type} ({main_discount:.2f} sum)")
print(f"Bulk discount eligible: {bulk_discount_eligible}, amount: {bulk_discount:.2f}")
print(f"Total discounts applied: {total_discounts:.2f} sum")

print("\n--- Fees, Tax, and Shipping ---")
print(f"Small order fee applied: {small_order_fee_applied}, amount: {small_order_fee:.2f}")
print(f"Subtotal after discounts/fees: {subtotal_after_discounts:.2f} sum")
print(f"Tax exempt (textbook order): {tax_exempt}, amount: {tax:.2f}")
print(f"Free shipping: {free_shipping}, amount: {shipping:.2f}")

print("\n" + "*" * 40)
print(f"FINAL TOTAL: {final_total:.2f} sum")
print(f"Net Savings (or extra cost if negative): {net_savings:.2f} sum")
print("*" * 40)
