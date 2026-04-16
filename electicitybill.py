# Electricity Bill Calculation

units = int(input("Enter number of units consumed: "))

# Step 1: Calculate base bill
bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 8
else:
    bill = (100 * 5) + (100 * 8) + (units - 200) * 10

# Step 2: Apply surcharge if bill > 5000
if bill > 5000:
    bill += bill * 0.10  # 10% surcharge

# Step 3: Minimum bill condition
if bill < 500:
    bill = 500

# Output
print(f"Total Bill: ₹{bill:.2f}")