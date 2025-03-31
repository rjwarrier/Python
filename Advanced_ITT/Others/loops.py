# While Loop - Compound Interest Calculation
# A while loop is used when we do not know in advance how many times we need to iterate.
# In this case, we are calculating compound interest for a given number of years.
deposit = 10000  # Initial deposit
interest_rate = 0.05  # 5% annual interest
years = 5
current_year = 1
while current_year <= years:
    deposit += deposit * interest_rate  # Adds interest to deposit
    print(f"Year {current_year}: Balance = {deposit:.2f}")  # Displays balance
    current_year += 1  # Increments year

# For Loop - Summing up monthly expenses
# A for loop is used when we know in advance the number of iterations required.
# Here, we iterate over a list of monthly expenses to calculate the total.
monthly_expenses = [1500, 2000, 1800, 2200, 1700]  # List of monthly expenses
total_expense = 0
for expense in monthly_expenses:
    total_expense += expense  # Adds each month's expense to total
print(f"Total Expense over {len(monthly_expenses)} months: {total_expense}")
