from PIL import Image
import os, sys

path = r"D:\btwin\data"
celebs = os.listdir( path )
#print(celebs)

def resize():
    for celeb in celebs:
            a = 1
            path_celeb = os.path.join(path, celeb)
            dirs = os.listdir( path_celeb )
            for item in dirs:
                if os.path.isfile(os.path.join(path_celeb,item)):
                    im = Image.open(os.path.join(path_celeb,item))
                    f, e = os.path.splitext(os.path.join(path_celeb,item))
                    
                    f = os.path.join(path, 'resized\\')
                    print(f)
                    imResize = im.resize((200,200), Image.ANTIALIAS)
                    if imResize.mode != "RGB":
                        imResize = imResize.convert("RGB")
                    imResize.save(f+ str(a) +'.jpg', 'JPEG', quality=90)
                    a += 1

resize()