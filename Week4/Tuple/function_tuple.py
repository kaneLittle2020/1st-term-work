def Likelihood ():
 Likelihood =  (50, 38, 27, 99, 4) #Tuple function
#print ("The min likelihood of falling is : {}".format(min(Likelihood)))
 return min (Likelihood), max (Likelihood)

def run():
  probabilities = Likelihood()
  print(f"Minimum likelihood of falling: {probabilities[0]}%")
  print(f"Maximum likelihood of falling: {probabilities[1]}%")

run()

#def run ():
  #print(f"Minimum likelihood of falling: {Likelihood[0]}%")
