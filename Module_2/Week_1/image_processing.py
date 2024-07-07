import matplotlib.image as mpimg
from icecream import ic
import numpy as np


def extract_rgb_channel(img):
    # Extract the RGB channels
    r_channel = img[:, :, 0]
    g_channel = img[:, :, 1]
    b_channel = img[:, :, 2]

    return r_channel, g_channel, b_channel


def lightness_convert(img):
    r_channel, g_channel, b_channel = extract_rgb_channel(img)

    max_channel = np.maximum.reduce([r_channel, g_channel, b_channel])
    min_channel = np.minimum.reduce([r_channel, g_channel, b_channel])

    gray_img = (max_channel + min_channel) / 2

    return gray_img


def average_convert(img):
    gray_img = np.mean(img, axis=2)

    return gray_img


def luminosity_convert(img):
    r_channel, g_channel, b_channel = extract_rgb_channel(img)

    gray_img = 0.21 * r_channel + 0.72 * g_channel + 0.07 * b_channel

    return gray_img


if __name__ == '__main__':
    img = mpimg.imread("Module_2\\Week_1\\dog.jpg")  # (534, 800, 3)

    # Cau 12 -> A
    print("------------------- Cau 12 ---------------------")
    gray_img_1 = lightness_convert(img)
    ic(gray_img_1[0, 0])  # A

    # Cau 13 -> A
    print("------------------- Cau 13 ---------------------")
    gray_img_2 = average_convert(img)
    ic(gray_img_2[0, 0])

    # Cau 14 -> C
    print("------------------- Cau 14 ---------------------")
    gray_img_3 = luminosity_convert(img)
    ic(gray_img_3[0, 0])
