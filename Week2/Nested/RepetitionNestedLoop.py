print ("How many rows should i have?")
rows = int (input())

print ("How many columns should I have?")
columns = int(input())

print ("Here I go")


for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(":-)", end="")
    print()

print ("Done")