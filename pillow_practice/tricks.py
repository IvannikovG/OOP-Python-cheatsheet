import os
from PIL import Image, ImageFilter

image1 = Image.open('me.png')
image1.rotate(90)  # rotate(degrees)
image1.convert(mode='L')  # black and white

image1.filter(ImageFilter.GaussianBlur(45)).save('blurred_me.png')
