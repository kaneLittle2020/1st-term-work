print ("please enter three whole number")
print ("First whole number")
Numberinput1 = int (input())
print ("Second whole number")
Numberinput2 = int (input())
print ("third whole number")
Numberinput3 = int (input())

evennumbers = 0
oddnumbers = 0

if (Numberinput1 % 2 == 0):
  evennumbers = evennumbers + 1
else:
  oddnumbers = oddnumbers + 1

if (Numberinput2 % 2 == 0):
  evennumbers = evennumbers + 1
else:
  oddnumbers = oddnumbers + 1

if (Numberinput3 % 2 == 0):
  evennumbers = evennumbers + 1
else:
  oddnumbers = oddnumbers + 1

print("There were {} even and {} odd numbers.".format(evennumbers, oddnumbers))
