print("Welcome to the Tip Calculator! 💰")

# Get input from user
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? (10, 12, 15): "))
people = int(input("How many people will split the bill? "))

# Calculate the total bill including tip
tip_amount = bill * (tip / 100)
total_bill = round(bill + tip_amount, 2)
per_person = round(total_bill / people, 2)

# Display results
print(f"\nTotal bill including {tip}% tip: ${total_bill}")
print(f"Each person should pay: ${per_person}")
