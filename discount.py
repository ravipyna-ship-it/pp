
purchase_amount = float(input("Enter purchase amount: "))
is_premium = input("Is the customer a premium member? (yes/no): ").strip().lower()
discount = 0
if purchase_amount > 10000:
    discount = 15
if is_premium == "yes":
        discount+=5 
discounted=purchase_amount-(purchase_amount*discount/100)         
final_price = discounted+(discounted*18/100)
print("final_price after discount and gst",final_price)