def calculate_total(invoice_text):
    invoice_lines = invoice_text.split('\n')
    subtotal = 0
    discount = 0
    for line in invoice_lines:
        if '@' in line and 'x' in line:
            product = line.split('@')
            details = product[1]
            quantity,price = details.split('x')
            floated_quantity = float(quantity.strip())
            floated_price = float(price.replace('$',''))
            subtotal += floated_quantity*floated_price
        elif '%' in line:
            percent = line.split(':')[1].replace('%','')
            tax_rate = float(percent) / 100
        elif '$' in line:
            amount = line.split(':')[1].replace('$','')
            discount = float(amount)
    after_discount = subtotal - discount
    total = after_discount * (1 + tax_rate)
    return "$" + format(total, ".2f")

# Test Case 1: Standard invoice with items, tax, and discount
invoice1 = """Laptop @ 1 x $1250.00
Mouse @ 2 x $25.50
TAX: 8%
DISCOUNT: $50.00"""
print(calculate_total(invoice1))

# Test Case 2: Invoice with no discount
invoice2 = """Book @ 3 x $15.00
Pen @ 10 x $1.50
TAX: 5%"""
print(calculate_total(invoice2))

# Test Case 3: Invoice with zero tax and a discount
invoice3 = """Monitor @ 1 x $300.00
Keyboard @ 1 x $75.00
DISCOUNT: $25.00
TAX: 0%"""
print(calculate_total(invoice3))