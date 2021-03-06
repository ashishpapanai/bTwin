import os
a = open("classes.txt", "w")
for path, subdirs, files in os.walk(r'D:\btwin\data_resized'):
   for subdir in subdirs:
      a.write(subdir+"\n") 
      