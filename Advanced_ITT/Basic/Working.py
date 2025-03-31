# Investment Options Based on User Input with Retry Option

while True:
    # Get investment amount from user and convert to integer
    investment_amount = int(input("Enter the amount you want to invest: "))

    # Get risk tolerance from user (expecting 'High' or 'Low')
    risk_tolerance = input("Enter your risk tolerance (High/Low): ")

    # Evaluate investment options based on user input
    if investment_amount >= 50000:
        if risk_tolerance == "High":
            print("> Invest in Stocks")
        else:
            print("> Invest in Bonds")
    else:
        print("> Consider a Fixed Deposit")

    # Ask if the user wants to try again
    retry = input("Do you want to try again? (y/n750): ").strip().lower()
    if retry != "y":
        print("Thank you! Goodbye")
        break
