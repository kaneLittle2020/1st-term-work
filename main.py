print ("where should i look?") 
place = input () 

if (place == 'bedroom'):
  print ("you are now in the bedroom, where in the bedroom do you want to look?")
  input ()
  if (input == 'under the bed') :
    print ("Nothing seems to be here")
  else: 
    print ("Found some mess but, no batteries")

elif  (place == 'bathroom'):
  print("Where in the bathroom should I look?")
  input ()
  if (input == 'bathtub'):
    print ("Found a rubber duck but no battery")
  else:
    print("Found a wet surface but no battery.")













