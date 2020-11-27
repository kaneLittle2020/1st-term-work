#Ask user for number of mountains
print("How many mountains should I display?")
mountains = int(input())

# Display mountains
print("\nDisplaying...")

for mountain in range(mountains):
  print (""""
  __
  /  \\_  
  /^    \\
  /  ^    \\_
  / ^ ^     ^\\
  /  ^     ^    \\""")