print("This is a rightangled triangle")
print("A rightangled triangle always has one angle 90 degrees.")

n = int(input("Enter how many rows you would like: "))

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()