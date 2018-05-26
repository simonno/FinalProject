import cv2  # OpenCV 2
from random import randint
from os import listdir
from os.path import isfile, join

def to_bit_generator(msg):
    """Converts a message into a generator which returns 1 bit of the message
    each time."""
    for c in (msg):
        o = ord(c)
        for i in range(8):
            yield (o & (1 << i)) >> i


def createBadImage(path_image, path_malware):
    # Create a generator for the hidden message
    hidden_message = to_bit_generator(open(path_image, "rb").read() * 10)

    # Read the original image
    img = cv2.imread(path_image, cv2.IMREAD_GRAYSCALE)
    width, height = img.shape
    for h in range(width):
        for w in range(height):
            # Write the hidden message into the least significant bit
            bit = next(hidden_message)
            img[h][w] = (img[h][w] & ~1) | bit
    # Write out the image with hidden message
    cv2.imwrite(path_image, img)
