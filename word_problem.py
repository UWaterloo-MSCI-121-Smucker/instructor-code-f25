def main():
    cash_available = 60
    sales_tax_rate = 0.13
    cost_of_lag_bolts = 22 * 0.97
    cost_of_2x4s = 6 * 3.38
    cost_of_hammer = 1 * 9.98
    total_cost = cost_of_lag_bolts + cost_of_2x4s + cost_of_hammer
    total_cost = total_cost + total_cost * sales_tax_rate
    total_cost_in_nickels = total_cost / 0.05
    total_cost_rounded = round(total_cost_in_nickels) / 20
    print("If paying cash, total cost is: $", total_cost_rounded)
    if cash_available < total_cost_rounded:
        cash_needed = total_cost_rounded - cash_available
        print("Not enough cash.  This amount more is needed: $",
               cash_needed)
    else:
        change = cash_available - total_cost_rounded
        print("Change due: $", change)
        

if __name__ == "__main__":
    main()
