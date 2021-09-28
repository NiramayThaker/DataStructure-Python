list_1 = []
list_2 = []

size = int(input("Enter maximum size: "))

print("\n")
for _ in range(0, size):
    temp = int(input(f"Enter value {_+1}: "))
    list_1.append(temp)

print("\n")

for i in list_1:
    if i not in list_2:
        list_2.append(i)
    else:
        print("Duplicate: ", i)
