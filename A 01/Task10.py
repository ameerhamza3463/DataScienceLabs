
# Variables Initialization
n = 3
sem = 6

# Lists Declaration
Score = []
Names = []
Students = []

# Loop to take input for each student name and his/her semester wise GPA and add into a single list students
for i in range(0, n):
    print("\n---------------------------------------------------")
    name = input(f"\nEnter Student {i+1} name: ")
    print("")
    s = []
    for j in range(0, sem):
        gpa = float(input(f"Enter Student {i+1} Semester {j+1} GPA: "))
        s.append(gpa)
    Score.append(s)
    Names.append(name)
    Students.append(list((Names[i], Score[i])))

print("\n==================================================================")
print("\nFinal Students List: ", Students, end="\n\n")
print("\n==================================================================")

