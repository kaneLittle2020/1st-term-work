print ("How Far are we from the cave")
steps = int (input ())

# Display count down
print ()

for count in range(steps, 0, -1):
  print(count, "steps remaining")

print("We have reached the cave!")
