
rooms = []          # Declared empty list
# User's input
n = int(input("\nHow many rooms you want to add? "))

# Loop to take input from user and insert each new entry into the list
for i in range(0, n):
    print("\n---------------------------------------------------")
    name = input(f"\nEnter room {i+1} name: ")
    area = input(f"Enter room {i+1} area (square-meter): ")
    rooms.append(name +' '+ area)

# Output
print("\n==================================================================")
print("\nFinal rooms list: ", rooms, end="\n")
print("\n==================================================================")