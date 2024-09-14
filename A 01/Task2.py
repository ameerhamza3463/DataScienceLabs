import math as m

# Taking Input
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

# Function to calculate Determinant
def calculateDeterminant():
    return b**2 - 4*a*c

D = calculateDeterminant()      # Function Call
print("\nDeterminant is: ", D)

# Conditions based on D
if (D > 0):
  x1 = (-b + m.sqrt(D))/(2*a)
  x2 = (-b - m.sqrt(D))/(2*a)
  print("\nTwo real roots are")
  print("\tX1: ", round(x1, 3))
  print("\tX2: ", round(x2, 3))
elif (D == 0):
  x = -b/2*a
  print("\nReal root (x) : ", x)
else:
   print("\nOnly Complex Roots")
