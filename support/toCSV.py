from PIL import Image
import numpy as np
import os
import csv

# load the original image
path = r"data_resized\Aamir_Khan"
myFileList = os.listdir(path)
img_file = Image.open(os.path.join(path, '1.jpg'))
# img_file.show()

# get original image parameters...
width, height = img_file.size
format = img_file.format
mode = img_file.mode

# Make image Greyscale
img_grey = img_file.convert('L')
#img_grey.save('result.png')
#img_grey.show()

# Save Greyscale values
value = np.asarray(img_grey.getdata(), dtype=int).reshape((img_grey.size[1], img_grey.size[0]))
value = value.flatten()
print(value.shape)
value = value.reshape(200, 200)
img2 = Image.fromarray(value)
img2.show()
"""with open(r"data_resized\Aamir_Khan.csv", 'a') as f:
    writer = csv.writer(f)
    writer.writerow(value)"""