import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import shutil
import glob
from retinaface import RetinaFace
os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1'

link = "/home/mujung/PycharmProjects/Age-Gender-Pred-master/utkface/new_image2"
dataset = glob.glob(link + "/*.jpg",recursive=True)
for data in dataset:
    s = ''
    org_file = data.split(sep = "/")[-1]
    file_split = org_file.split('_')
    age = file_split[0]
    gender = file_split[1]
    img_path = file_split[2:]
    img_path = "".join(img_path)

    if "0-2" in age:
        age = "0"
    elif "4-6" in age:
        age = "1"
    elif "8-13" in age:
        age = "2"
    elif "15-20" in age:
        age = "3"
    elif "25-32" in age:
        age = "4"
    elif "38-43" in age:
        age = "5"
    elif "48-53" in age:
        age = "6"
    else:
        age = "7"
    new_file = age + "_" + gender + "_" + img_path
    load_img = cv2.imread(data)
    cv2.imwrite(f"/home/mujung/PycharmProjects/Age-Gender-Pred-master/utkface/new_image/{new_file}", load_img)
