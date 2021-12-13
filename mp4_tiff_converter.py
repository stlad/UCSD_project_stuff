import cv2
import os
from PIL import Image

import image_cutter

path = os.getcwd() + '/video' # папка с видео
os.chdir(path)            # папка с видео - активная
print(os.listdir())       # получаем список файлов

for video in [file for file in os.listdir(path) if file.__contains__('.mp4')]:  # бежим по всем файлам с .mp4
  os.chdir(path)          # папка с видео - активная
  vidcap = cv2.VideoCapture(video)  # открываем видео файл
  success, image = vidcap.read()    # читаем первый кадр
  count = 0
  os.makedirs(video[:-4])           # создаем новую папку для кадров
  os.chdir(path+'/'+video[:-4])     # переходим в папку


  while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 100)) # раз в сколько мс берем кадр.
                                                     # 20 сек видео. 200 кадров, тогда кадр берется раз в 100 мс

    cv2.imwrite("%d.tif" % count, image) #оставить, если кадр не обрезается

    success,image = vidcap.read()
    count += 1


