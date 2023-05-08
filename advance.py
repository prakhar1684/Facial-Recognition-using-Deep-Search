nameOfFiles = ["photo compare.py", "Live image.py", "abc.py", "Dialogue for selecting.py"]
with open("advanced_file.py", "w") as new_created_file:
   for name in nameOfFiles:
      with open(name) as file:
         for line in file:
            new_created_file.write(line)
            
         new_created_file.write("\n")