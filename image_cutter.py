from PIL import Image
import numpy as np


def cut_image(img, fpt = (320,110), spt=[1542,750]):
    '''
    :param img: изображение np.array
    :param fpt: координаты левой верхней точки
    :param spt: координаты правой нижней точки
    :return: обрезанное изображение
    '''
    arr = np.array(img)

    res_img = arr[fpt[0] : spt[0], fpt[1] : spt[1]]
    res = Image.fromarray(res_img)
    return res

