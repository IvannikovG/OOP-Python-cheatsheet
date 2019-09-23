from PIL import Image
import os

image1 = Image.open('/Users/georgiiivannikov/Desktop/pyth/face1.png')
# Open in python environment

# image1.show()  # Open in preview
# image1.save('face1.png')

# iterate through files in the directory, make png of them
# put them into the new directory
for f in os.listdir('.'):
    if f.endswith('.jpg') or f.endswith('.png'):
        i = Image.open(f)
        filename, fileext = os.path.splitext(f)
        # splits the filename into the name and extension
        i.save('pngs/{}.png'.format(filename))
