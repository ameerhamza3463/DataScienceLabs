
# Function to calculate weight in stones
def calculate_weightInStones(w):
    return (w * 2.2)/14


print("\n==================================================================")
print("\t\t WEIGHT in STONES CALCULATOR")
print("==================================================================")

# User Input
weight = float(input("\nEnter Weight(kg): "))

print("\n==================================================================")

Ws = calculate_weightInStones(weight)       # Function Call
print(f"\n\tWeight in Stones: {round(Ws, 2)} stones")       # round() rounds up the value to given decimal places

print("\n==================================================================")
