import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import shutil
import glob
from pathlib import Path
os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1'
load = pd.read_csv("./utkface/Adience/clean_adience_age_gender")
load = load.values.tolist()
file_path = "/home/mujung/PycharmProjects/Age-Gender-Pred-master/utkface/Adience/crop/"
imgs = glob.glob(file_path + '*.jpg' ,recursive=True)


for img in imgs:
    img_name = img.split(sep="/")[-1]

    for i in range(len(load)):
        age = load[i][0]
        gender = load[i][1]
        gt_img_name = load[i][2]
        if img_name == gt_img_name:
            # np_imgs = np.array(imgs)
            load_img = cv2.imread(img)
            image_name = str(age) + "_" + str(gender) + "_" + str(gt_img_name)
            cv2.imwrite(f"/home/mujung/PycharmProjects/Age-Gender-Pred-master/utkface/new_image/{image_name}", load_img)
        else:
            continue
    "25-32_0_filename"

