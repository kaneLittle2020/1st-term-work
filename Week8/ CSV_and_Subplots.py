import csv
import matplotlib.pyplot as plt

first_key = None
second_key = None

def read_data():
  global first_key, second_key

  with open ('Week8/visual/subplots/temps.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)

    first_key = header[0].strip()
    second_key = header[1].strip()

    data = {
    first_key:[],
    second_key:[]
    }

    for row in csv_reader:
      data[first_key].append (row [0].strip())
      data[second_key].append (row [1].strip ())
    
    return data
def run():
  data = read_data()

  fig, (ax1, ax2) = plt.subplots (2, 1, sharex = 'all')
  ax1.plot(data[first_key])
  ax2.plot(data[second_key])

  plt.tight_layout()
  plt.show()

run()

