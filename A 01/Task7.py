
# Variable Initialization
growth_multiplier = 1.3
sales = 140000

print(f"\nSales in 1st year: {sales} PKR")

#Loop to iterate for 7 years
for i in range(0, 7):
    sales *= growth_multiplier

print(f"\nSales after 7 years: {sales} PKR", end = "\n\n")