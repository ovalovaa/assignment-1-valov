amount_dishes = int(input("enter amount of dishes"))
total_cost = 0
tips = 0
for x in range(amount_dishes):
    dish_price = int(input("enter cost of your dishes"))
    total_cost = total_cost + dish_price
print("Total before discount:", str(total_cost))
if total_cost > 2000:
    total_cost = total_cost * 0.9
    print("total after discount:", str(total_cost))
tips = int(input("enter tips"))
tips_total = total_cost/100*tips
total_cost_after = total_cost + tips_total
print("cost after tips", str(total_cost_after))
print("Tips amount", str(tips_total))


