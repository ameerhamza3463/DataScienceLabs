
# Function to remove duplicates from the list
def removedupliates(numbers):
    temp = set()
    finallist = []
    for i in numbers:
        if i not in temp:
            temp.add(i)
            finallist.append(i)
    return finallist


numbers = [12,24,35,24,88,120,155,88,120,155]       # Original list
finalnumbers = removedupliates(numbers)               # Function Call

# Output Statements
print("\nOriginal List: ", numbers)
print("\nFinal List: ", finalnumbers, end = "\n\n")