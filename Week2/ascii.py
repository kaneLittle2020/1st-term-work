print ("How many bars should be charged")
chargebars = int(input())

charged = 0

print()

while (charged < chargebars ):
  charged = charged + 1
  print ("Charging", "█" * charged)

print ("done charging")
