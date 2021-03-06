import os
a = open("classes.txt", "w")
num = 1
for path, subdirs, files in os.walk(r'D:\btwin\data_resized'):
   for subdir in subdirs:
      a.write(str(num)+". "+subdir+"<br>"+"\n") 
      num += 1
      