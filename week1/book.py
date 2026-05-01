print(f"{'-' * 40}")
print(f"            The lists of books")
print(f"1.English - 30000 sum")
print(f"2.Math - 40000 sum")
print(f"3.Coding - 35000 sum")
print(f"{'-' * 40}")
name =  input("Enter your name: ")
staff = input("Are you faculty staff (yes/no): ")
textbook = input("IS this text book order (yes/no): ")
book1 = float(input("How many of 'English' book are you gonna buy: "))
book2 = float(input("How many of 'Math' book are you gonna buy: "))
book3 = float(input("How many of 'Coding' book are you gonna buy: "))
books_number = book1 + book2 + book3
prize_before = book1 * 30000 + book2 * 40000 + book3 * 35000
faculty_discount = 0.20 * prize_before if staff else 0
textbook_discount = 0.25 * prize_before if textbook else 0
main_discount = faculty_discount * (faculty_discount >= textbook_discount) + textbook_discount * (textbook_discount > faculty_discount)
bulk_discount = 0.08 * main_discount if books_number >= 10 else 0
small_order_fee = (books_number < 3) * 10000
totalprize = prize_before - faculty_discount - textbook_discount - bulk_discount + small_order_fee
print(f"\nYour total cost is {totalprize}")