def search(file_name):
  print("Searching...")
  data = {}

  with open(file_name) as file:
    section_name = ""
    for line in file:
      if (line.startswith("Section")):
        parts = line.split(":")
        section_name = parts[1].strip()
      elif (section_name in data):
        data[section_name].append(line.strip())
      else:
        data[section_name] = [line.strip()]
    
   print("Done!")
   return data

def run():
  data = search("data/files/txt/books.txt")

  with open("data/files/txt/generated.csv", "w") as file:
    for section, books in data.items():
      for book in books:
        file.write(f"{section},{book}\n")

run()