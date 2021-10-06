#! python3
# ascii_pic_gen.py - generate txt file with ascii-art picture based on standard image

import sys
import os.path

from PIL import Image


# returns appropriate ascii character depending on the pixel darkness
def rgb_to_ascii(pixel):
    # ascii pixels (10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%)
    ascii_pixels = (" ", ".", ",", "*", "/", "(", "#", "%", "&", "@")[::-1]
    # sum up RGB values to measure darkness
    pixel_value = sum(pixel)
    step = 255 * 3 / len(ascii_pixels)
    index = int(pixel_value / step)
    if index == len(ascii_pixels):
        index = index - 1
    return ascii_pixels[index]


# generates txt file with image
def generate_ascii_art(image_path, scale=1):
    image = Image.open(image_path)
    width, height = image.size

    image_name = os.path.basename(image_path).split(".")[0]
    ascii_art_name = "ascii_" + image_name + ".txt"
    ascii_art_path = "\\".join([os.path.dirname(image_path), ascii_art_name])

    with open(ascii_art_path, 'w') as ascii_art_file:
        for y in range(0, height, 3 * scale):
            for x in range(0, width, scale):
                ascii_pixel = rgb_to_ascii(image.getpixel((x, y)))
                ascii_art_file.write(ascii_pixel)
            ascii_art_file.write('\n')

    if os.path.exists(ascii_art_path) and os.path.getsize(ascii_art_path) > 0:
        return ascii_art_path
    else:
        return False


def main():
    image_path = sys.argv[1]
    if not os.path.exists(image_path):
        print("Wrong path!")
        sys.exit(0)
    elif len(sys.argv) > 2 and sys.argv[2].isdigit() and sys.argv[2] > "0":
        scale = int(sys.argv[2])
        print(f"Generating ascii art from {os.path.basename(image_path)}, scale = 1/{scale}.")
    else:
        scale = 1
        print(f"Generating ascii art from {os.path.basename(image_path)}")

    ascii_art_path = generate_ascii_art(image_path, scale)

    if ascii_art_path:
        print(f"{ascii_art_path} - ascii art generated!")
        os.startfile(ascii_art_path)
    else:
        print("Some problem occurred!")
        sys.exit(0)


if __name__ == "__main__":
    main()
