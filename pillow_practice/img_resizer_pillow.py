import os
from PIL import Image
# iterate through images, resize them, put them into another folder
size_1000 = (1000, 1000)  # m*n = 300 * 300

for f in os.listdir('.'):  # check the files in the directory
    if f.endswith('.jpg') or f.endswith('.png'):  # if the file is an image
        img = Image.open(f)  # open it as python object
        # split filename into 'file' and 'extension'
        fn, fext = os.path.splitext(f)
        #img.thumbnail(size_300)  # make it smaller
        # save them into another folder
        #img.save('300/{}_300{}'.format(fn, fext))

        img.thumbnail(size_1000)
        img.save('1000/{}_1000{}'.format(fn, fext))
