#empty list Fruits = []
Fruits = ["Bannana", "Orange", "Pear"] 
#to add items 
Fruits.append ("dragon fruit")
Fruits.append ("Apple")
Fruits.remove ("Bannana")

# Displays fruits
for fruit in Fruits:
  print(fruit)
  
# also display the index position of the fruit
for index in range(len(Fruits)):
  print("{} is at index {}.".format(fruit, index))

print (Fruits)


#Indexing
print (Fruits[0])
del (Fruits[1])
print (Fruits)

