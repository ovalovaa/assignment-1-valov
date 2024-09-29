salary_per_month = int(input("Enter your monthly payment"))
yearly_percent_bank = int(input("enter percent for year from bank"))

months =12
monthly_percent_bank = yearly_percent_bank/months
cont = "y"
deposit = 0
while cont == "y":
    for month in range(months):
        percent_for_deposit = int(input("enter percent of salary you want to use"))
        deposit_for_month = salary_per_month / 100 * percent_for_deposit
        monthly_revenue = deposit/100 * monthly_percent_bank
        deposit=deposit+deposit_for_month+monthly_revenue
        print(f"{month+1} month Total = {deposit}")
    cont = input("do you want to continue using your deposit? y/n?")
print(f"your total is {deposit}")

