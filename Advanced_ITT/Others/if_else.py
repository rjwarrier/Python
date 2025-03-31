# -------------------------------
# Demonstration of If-Else Statements in Python
# -------------------------------

# Basic if statement - Checking if income is taxable
income = 500000  # Annual income
if income > 250000:
    # This block executes if income is greater than 250,000
    print("Your income is taxable.")  # Output: Your income is taxable

# Indentation in if (code to explain error)
# Python requires indentation after control statements like if
# Uncommenting below lines will cause an IndentationError
# if income > 250000:
# print("Your income is taxable.")  # ❌ Incorrect: No indentation

# -------------------------------
# Elif - Income Tax Slab Calculation
# -------------------------------

income = 750000  # Reassigning income to check multiple conditions

if income > 1000000:
    print("Tax Rate: 30%")  # Executes if income is above 10L
elif income > 750000:
    print("Tax Rate: 20%")  # Executes if income is > 750000 but ≤ 10L
elif income > 500000:
    print("Tax Rate: 10%")  # Executes if income is > 5L but ≤ 7.5L
else:
    print("No tax applicable")  # Executes if income ≤ 5L

# -------------------------------
# Else - Checking Account Balance
# -------------------------------

balance = 5000  # Available balance in the account
withdrawal_amount = 7000  # Requested withdrawal

if withdrawal_amount <= balance:
    print("Transaction Successful")  # Condition is True if balance is enough
else:
    print("Insufficient Balance")  # Runs when withdrawal is more than balance

# -------------------------------
# IF And - Loan Eligibility
# -------------------------------

credit_score = 750  # Applicant's credit score
monthly_income = 40000  # Applicant's monthly income

# Both conditions must be True for loan approval
if credit_score >= 700 and monthly_income >= 30000:
    print("Loan Approved")
else:
    print("Loan Denied")

# -------------------------------
# IF Or - Credit Card Application
# -------------------------------

existing_loan = False  # No ongoing loan
high_salary = True  # Applicant earns a high salary

# Eligible if either no existing loan OR high salary
if not existing_loan or high_salary:
    print("Eligible for Credit Card")

# -------------------------------
# IF Not - Checking Loan Default Status
# -------------------------------

loan_default = False  # Customer has no loan defaults

# not False → True, so block runs
if not loan_default:
    print("Eligible for new loan")

# -------------------------------
# Nested IF - Checking Investment Options
# -------------------------------

# Get investment amount from user and convert to integer
investment_amount = int(input("Enter the amount you want to invest: "))

# Get risk tolerance from user (expecting 'High' or 'Low')
risk_tolerance = input("Enter your risk tolerance (High/Low): ")

if investment_amount >= 50000:
    # Inside outer if block — check risk tolerance
    if risk_tolerance == "High":
        print("Invest in Stocks")  # High investment + high risk = stocks
    else:
        print("Invest in Bonds")  # High investment + low risk = bonds
else:
    # Investment amount too low for market options
    print("Consider a Fixed Deposit")
