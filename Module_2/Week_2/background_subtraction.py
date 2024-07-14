import numpy as np
import cv2
from icecream import ic


ORIGIN_BG_IMAGE_PATH = "D:\\QuocAnh\\AIO\\AIO2024\\AIO2024\\Module_2\\Week_2\\Image data\\OriginalBackground.png"
OBJECT_IMAGE_PATH = "D:\\QuocAnh\\AIO\\AIO2024\\AIO2024\\Module_2\\Week_2\\Image data\\Object.png"
NEW_BG_IMAGE_PATH = "D:\\QuocAnh\\AIO\\AIO2024\\AIO2024\\Module_2\\Week_2\\Image data\\NewBackground.jpg"


def compute_difference(bg_image, obj_image):
    """
    Lấy obj_image - bg_image, những pixel != 0 là foreground, 
    và ngược lại là background

    Phép trừ thực hiện được vì đã resize về chung 1 kích thước

    Args:
        bg_image (ndarray): Original background
        obj_image (ndarray): Object image
    """
    obj_image = cv2.cvtColor(obj_image, cv2.COLOR_BGR2GRAY)
    bg_image = cv2.cvtColor(bg_image, cv2.COLOR_BGR2GRAY)

    # Ensure no negative values
    diff_single_channel = cv2.absdiff(obj_image, bg_image)

    return diff_single_channel


def compute_binary_mask(diff_image):
    """ Compute binary mask with 0 and 255

    Args:
        diff_image (ndarray): Difference in grayscale image

    Returns:
        _type_: ndarray
    """
    binary_mask = np.where(diff_image > 0, 255, 0).astype(np.uint8)

    # Ensure same shape with new_bg_image
    binary_mask = cv2.cvtColor(binary_mask, cv2.COLOR_GRAY2BGR)

    return binary_mask


def replace_backround(obj_image, origin_bg_image, new_bg_image):
    diff_image = compute_difference(origin_bg_image, obj_image)

    binary_mask = compute_binary_mask(diff_image)

    output = np.where(binary_mask == 255, obj_image, new_bg_image)

    return output


def read_and_resize_images():
    origin_bg_image = cv2.imread(ORIGIN_BG_IMAGE_PATH, 1)
    origin_bg_image = cv2.resize(origin_bg_image, dsize=(678, 381))

    obj_image = cv2.imread(OBJECT_IMAGE_PATH, 1)
    # dsize takes (width, height)
    obj_image = cv2.resize(obj_image, dsize=(678, 381))

    new_bg_image = cv2.imread(NEW_BG_IMAGE_PATH, 1)
    new_bg_image = cv2.resize(new_bg_image, dsize=(678, 381))

    return obj_image, origin_bg_image, new_bg_image


if __name__ == '__main__':
    obj_image, origin_bg_image, new_bg_image = read_and_resize_images()

    ic(obj_image.shape)  # (height, width, channels)

    diff_image = compute_difference(origin_bg_image, obj_image)
    binary_mask = compute_binary_mask(diff_image)
    output = replace_backround(obj_image, origin_bg_image, new_bg_image)

    cv2.imshow("Segmented object", diff_image)
    cv2.imshow("Foreground mask", binary_mask)
    cv2.imshow("Final output", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
