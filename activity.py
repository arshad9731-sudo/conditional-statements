actual_cost = float(input("please enter  the actual cost of the item:"))
selling_price = float(input("please enter the selling price of the item: "))

if selling_price > actual_cost:
    amount = selling_price - actual_cost
    print("total profit = {0:.2f}".format(amount))
else:
    print("no profit")