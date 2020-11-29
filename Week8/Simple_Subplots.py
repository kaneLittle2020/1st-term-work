import matplotlib.pyplot as plt 
def read_data (file_path):
  with open (file_path) as file:
    Temperatures = [] 
    for line in file:
      Temperature = float (line.strip())
      Temperatures.append(Temperature)

  return Temperatures  

def run():
  data = read_data('Week8/visual/subplots/temps.txt')
  fig, (ax1, ax2) = plt.subplots(1, 2)

  ax1.plot(range(1, 8), data)
  ax2.bar(range(1, 8), data)
  plt.tight_layout()
  plt.show()

run()

