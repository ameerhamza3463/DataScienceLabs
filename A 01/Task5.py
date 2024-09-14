
# List Initialization
list1 = [1,3,6,78,35,55]
list2 = [12,24,35,24,88,120,155]

# Converting lists to sets
set1 = set(list1)
set2 = set(list2)

set1 &= set2        # Intersection update method on sets

intersectedlist = list(set1)    # Converting intersected set back to list

print("\nList1: ", list1)
print("List2: ", list2)
print("\nIntersected List: ", intersectedlist, end="\n\n")