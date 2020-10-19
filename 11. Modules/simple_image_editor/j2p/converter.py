from PIL import Image
import os

def image_converter(input_path, output_path):
    for filename in os.listdir(input_path):
        img = Image.open(input_path +"/"+ filename)
        img.save(output_path +'/' +filename.split('.')[0] + '.png')
        del img
