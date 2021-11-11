import glob
import os

from PIL import Image
from PIL import ImageColor


def img_file():
    """
    search files with suffix
    :return: all images from directory in "path" variable
    """
    img_container = []
    path = './thermo image'
    for filename in glob.glob(os.path.join(path, '*.jpg')):
        img_container.append(filename)
    for filename in glob.glob(os.path.join(path, '*.png')):
        img_container.append(filename)
    for filename in glob.glob(os.path.join(path, '*.jpeg')):
        img_container.append(filename)
    return img_container
# print(img.size)
# print(img.format)
# print(img.getpixel((0, 0)))


def get_all_colors(img):
    """

    :param img: open image from image container
    :return: changed all blue colors in to darkgray
    """
    # imgFile = open('imgRGB.txt', 'w')
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            # pix = []
            # pixLst = img.getpixel((x, y))
            # for v in pixLst:
            #     pix.append(str(v))
            # imgFile.write(f'''(({x}, {y}):[{", ".join(pix)}])'''+"\n")
            if img.getpixel((x, y))[0] < 190 and img.getpixel((x, y))[1] < 190:
                img.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
    # imgFile.close()
    return print("Image convert")


def get_grey_background():
    """
    :return: change background colors and open changed Image
    """
    for imageName in img_file():
        img = Image.open(imageName)
        get_all_colors(img)
        print(img.show())
    return print("changes complete")


get_grey_background()
# imgFile = open('bacon.txt', 'a')
# imgFile.write('Bacon is not a vegetable.')
# imgFile.close()
# imgFile = open('imgRGB.txt')
# content = imgFile.read()
