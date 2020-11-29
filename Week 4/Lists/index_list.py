def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path
  
# With loop that amkes it shorter

def run():
  print("Moving...")
  path = movements()
  for index in range(0, len(path), 2):
    print(f"{path[index]} for {path[index+1]} steps")



def run2():
  print("Moving...")
  path = movements()
  print(f"{path[0]} for {path[1]} steps")
  print(f"{path[2]} for {path[3]} steps")
  print(f"{path[4]} for {path[5]} steps")
  print(f"{path[6]} for {path[7]} steps")

run()
