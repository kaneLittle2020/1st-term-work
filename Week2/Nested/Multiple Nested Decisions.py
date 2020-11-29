print ("where should i look, Bathroom, Bedroom, Lab?") 
place = input () 

if (place == 'bedroom'):
  print ("you are now in the bedroom, where in the bedroom do you want to look?")
  bedroomloc = input ()
  if (bedroomloc == 'under the bed') :
    print ("Nothing seems to be here")
  else: 
    print ("Found some mess but, no batteries")

elif  (place == 'bathroom'):
  print("Where in the bathroom should I look?")
  bathloc = input ()
  if (bathloc == 'bathtub'):
    print ("Found a rubber duck but no battery")
  else:
    print("Found a wet surface but no battery.")

elif (place == "lab"):
    print("Where in the lab should I look?")
    labplace = input()

    if (labplace == "on the table"):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")

# Handle unknown place
else:
    print("I am not sure where that place is located.")