
# Function to calculate smaller numbers
def smaller(x, s, n):
    count = 0
    for i in range(0, s):
        if x[i] < n:
          count += 1
    return count 

# User's Input
print("==================================================================")
print("\t\t SMALL NUMBERS COUNTER")
print("==================================================================")

x = []
s = int(input("\nHow many elements are there in the array? "))
print("Add the elements of the array sequentially (Only add numbers)\n")
# Loop to add elemnts in the array
for i in range(0, s):
   temp = int(input("Enter the next element: "))
   x.append(temp)

n = int(input("\nEnter the comparison number: "))

smallCount = smaller(x, s, n)           #Function Call

print("\n\n\tOutput:")
print(f"There are {smallCount} small elements than {n} in the given array.\n")  