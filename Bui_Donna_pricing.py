# Functions Part 2: Software Sales - Donna Bui - 2/14/2023 - Professor Henry Estrada's COMSC 078

discount = 0
price = float(input("What is the price of each item? "))
count = float(input("How many are you ordering? "))


if count < 10: # Less than 10 items will not receive a discount
    discount = 0
elif count >= 10 and count <= 19: # 10-19 items = 10% discount
    discount = 0.1
elif count >= 20 and count <= 49 :# 20-49 items = 20% discount
    discount = 0.2    
elif count >= 50 and count <= 99: # 50-99 items = 25% discount
    discount = 0.25
elif count >= 100: # 100 or more = 30% discount
    discount = 0.30
    
subtotal = price*count
discountamt = subtotal*discount
total = subtotal-discountamt

print("Subtotal: $", "%.2f" % subtotal)
print("Discount: $", "%.2f" % discountamt)
print("Total: $", "%.2f" % total)
    
    