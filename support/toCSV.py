from PIL import Image
import numpy as np
import os
import csv

path = r"data_resized"
celebs = os.listdir(path)
# print(celebs)
a = 1
for celeb in celebs:
    images_path =os.path.join(path, celeb)
    images = os.listdir(images_path)
    for image in images:
        img_file = Image.open(os.path.join(images_path, image))
        width, height = img_file.size
        format = img_file.format
        mode = img_file.mode
        img_grey = img_file.convert('L')

        value = np.asarray(img_grey.getdata(), dtype=int).reshape((img_grey.size[1], img_grey.size[0]))
        value = value.flatten()
        value = np.insert(value, 0, a)
        #value = value.reshape(200, 200)
        # img2 = Image.fromarray(value)
        # img2.show()
        with open(r"data.csv", 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(value)
    print('done'+celeb)
    a += 1
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
value = np.insert(value, 0, 1)
#value = value.reshape(200, 200)
# img2 = Image.fromarray(value)
# img2.show()


with open(r"data.csv", 'a') as f:
    writer = csv.writer(f)
    writer.writerow(value)