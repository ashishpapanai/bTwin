from PIL import Image
import numpy as np
import os
import csv

path = r"data_resized"
celebs = os.listdir(path)
# print(celebs)
a = 0
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
