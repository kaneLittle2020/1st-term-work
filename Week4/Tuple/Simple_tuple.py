temperatures = (19, 20, 21, 22)

# Concatenate tuples (this creates a new tuple)
all_temperatures = temperatures + (23, 24)
print(all_temperatures)

# Repeat a tuple
print(temperatures * 2)

# Check membership of a tuple
print(20 in temperatures)

#Tuples also support some useful functions such as min which gets the smallest value in a tuple and max which gets the largest value in a tuple

print("The lowest temperature is: {}".format(min(temperatures)))
print("The highest temperature is: {}".format(max(temperatures)))