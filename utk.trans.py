import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import shutil
import glob
from pathlib import Path

path = "./utkface/crop_part1"
file = glob.glob(path + "/*.jpg")

for i in file:
    information = i.split(sep="/")[-1]
    new_file = information.split("_")
    if len(new_file) == 4:
        new_file = new_file[0] + '_' + new_file[1] + "_" + new_file[3]
        load_img = cv2.imread(i)
        cv2.imwrite(f"/home/mujung/PycharmProjects/Age-Gender-Pred-master/utkface/new_image/{new_file}", load_img)
    else:
        print(i, new_file)
