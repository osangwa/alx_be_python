# User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings with 5% interest
annual_savings_before_interest = monthly_savings * 12
interest_earned = annual_savings_before_interest * 0.05
projected_annual_savings = annual_savings_before_interest + interest_earned

# Output Results
print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.0f}.")