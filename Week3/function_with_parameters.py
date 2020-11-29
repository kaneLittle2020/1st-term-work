def climb_ladder (StepsRemaining, Crossed):
  if (StepsRemaining < Crossed):
    print ("There is still more to go")
  elif (StepsRemaining > Crossed):
    print ("We are almost there")
  else:
    print ("i dont know")



climb_ladder(5, 2)
climb_ladder(2, 5)