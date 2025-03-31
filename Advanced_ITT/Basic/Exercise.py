'''
write a python program to calculate simple interest if:
principal = 20,00,000.00
int rate = 8.75%
tenure = 18 Months
'''

principal = 2500000.00
int_rate = 8.75 / 100
tenure = 18 / 12  # converting months to years

interest = principal*int_rate*tenure

print("Simple Interest for above is:", interest)
