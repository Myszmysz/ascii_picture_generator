#! python3
# ascii_pic_gen.py - generate txt file with ascii-art picture based on standard image

from PIL import Image


def rgb_to_ascii(pixel_value):
    # ascii_pixels = (" ", "░", "▒", "▓", "█")
    ascii_pixels = (" ", ".", ",", "*", "/", "(", "#", "%", "&", "@")
    ascii_pixels = ascii_pixels[::-1]
    step = 255 * 3 / 10
    index = int(pixel_value / step)
    return ascii_pixels[index]

def image_in_terminal():
    

imageName = "3.jpg"
asciiArtName = "ascii_" + imageName + ".txt"
scale = 4

pigImage = Image.open(imageName)
pigWidth, pigHeigh = pigImage.size

with open(asciiArtName, 'w') as asciiArtFile:
    for y in range(0, pigHeigh, 2*scale):
        for x in range(0, pigWidth, scale):
            ascii_pixel = rgb_to_ascii(sum(pigImage.getpixel((x, y))))
            asciiArtFile.write(ascii_pixel)
        asciiArtFile.write('\n')
