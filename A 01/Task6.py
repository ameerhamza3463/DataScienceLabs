
# Function to calculate BMI
def BMIcalculator(w, h):
    return w/h**2

# Menu
print("==================================================================")
print("\t\t BMI CALCULATOR")
print("==================================================================")

# User Input
weight = float(input("\nEnter weight(kg): "))
height = float(input("Enter height(m): "))

print("\n==================================================================")
bmi = BMIcalculator(weight, height)         # Function call
print("\nBMI: ", bmi)
print("\n==================================================================")