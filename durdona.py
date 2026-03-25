def calculate_quote(quote_text):
    quote_lines = quote_text.split('\n')
    subtotal = 0
    credit = 0
    for quote_line in quote_lines:
        if ':' in quote_line and 'x' in quote_line:
            splitted_quote_line = quote_line.split(':')
            details = splitted_quote_line[1]
            hours , rates = details.split('x')
            cleaned_hours = float(hours.replace('hrs', ''))
            cleaned_rates = float(rates.replace('$','').replace('/hr',''))
            subtotal += cleaned_hours * cleaned_rates
        elif '$' in quote_line:
            first_action = quote_line.split(':')
            amount = first_action[1]
            credit = float(amount.replace('$',''))
        elif '%' in quote_line:
            second_line = quote_line.split(':')
            amount1 = second_line[1] 
            surcharge = float(amount1.replace('%',''))
    credit_deduction = subtotal - credit
    surcharge_application = credit_deduction * (1+surcharge/100)
    return f'${surcharge_application}'
        
# Test Case 1: Standard quote
quote1 = """Design : 10 hrs x $50.00/hr
Coding : 20 hrs x $60.00/hr
SURCHARGE: 20%
CREDIT: $100.00"""
print(calculate_quote(quote1))

# Test Case 2: No credit
quote2 = """Consulting : 5 hrs x $100.00/hr
Reporting : 2 hrs x $50.00/hr
SURCHARGE: 5%"""
print(calculate_quote(quote2))

# Test Case 3: Credit, no surcharge
quote3 = """Testing : 10 hrs x $30.00/hr
Docs : 5 hrs x $20.00/hr
CREDIT: $50.00
SURCHARGE: 0%"""
print(calculate_quote(quote3))