# Self-Assessment Question 1:

# The first bug I noticed was that total = sale replaced the total instead of adding to it. I found it by reading through the loop.

# Self-Assessment Question 2:
# apply_discount(price, tier) takes a price and tier and applies the correct discount then returns the discounted price.

# AI Disclosure:
# I used AI to help explain errors, review my code and clarify how the functions and loops worked. It helped me understand the code better than just getting the answers.

# --- Exercise 1 ---

def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")

# --- Exercise 3 ---

discounted_price = apply_discount(200, "gold")
print(f"After gold discount: ${discounted_price:.2f}")

tax = calculate_tax(discounted_price, 0.07)
after_tax = discounted_price + tax
print(f"After tax: ${after_tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# --- Exercise 4 ---

orders = [
    (200, "gold"),
    (150, "silver"),
    (80, "bronze"),
    (500, "none")
]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")
# --- Exercise 5 ---

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1
# --- Exercise 6 ---

x = 100   # global variable

def double_it():
    x = 999   # local variable
    return x * 2

print(x)
print(double_it())
print(x)

# Scope explanation:
# The x inside double_it() is a local variable and it only exists inside the function, doesnt change the global x outside the function.