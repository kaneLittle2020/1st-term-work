print ("What type of book cover is there (Hard or Soft)")
booktype = input ()
if (booktype == "Soft"):
  print ("Soft cover,is it a thick book?")
  response = input ()
  if (response == "yes"):
    print ("That is a odd choice")
  else:
    print ("That's a good choice")
else:
  print ("Hard cover, is it a thick book?")
  response = input ()
  if (response == "yes"):
    print ("this is a good choice")
  else:
    print ("Not nescerary but still good to have")