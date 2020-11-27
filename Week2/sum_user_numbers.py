print ("How many numbers should I sum up?")
Amount = int (input())

summed = 0 
print ()
total = 0 


while (summed < Amount):
    print("Please enter number", summed, "of", Amount, ":")
    number = int(input())
    total = total + number
    summed = summed + 1

# Display result
print("The answer is", total)