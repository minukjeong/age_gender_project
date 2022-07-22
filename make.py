import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import shutil
import glob
os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1'

# fold0 = pd.read_csv("./utkface/Adience/fold_0_data.txt",sep = "\t" )
# fold1 = pd.read_csv("./utkface/Adience/fold_1_data.txt",sep = "\t")
# fold2 = pd.read_csv("./utkface/Adience/fold_2_data.txt",sep = "\t")
# fold3 = pd.read_csv("./utkface/Adience/fold_3_data.txt",sep = "\t")
# fold4 = pd.read_csv("./utkface/Adience/fold_4_data.txt",sep = "\t")
#
# total_data = pd.concat([fold0, fold1, fold2, fold3, fold4], ignore_index=True)
# print(total_data.shape)
#
# imp_data = total_data[['age', 'gender']].copy()
# img_path = []
# for row in total_data.iterrows():
#     path = "./utkface/Adience/faces/"+row[1].user_id+"/coarse_tilt_aligned_face."+str(row[1].face_id)+"."+row[1].original_image
#     img_path.append(path)
# imp_data['img_path'] = img_path
# imp_data.head()
#
# age_mapping = [('(0, 2)', '0-2'), ('2', '0-2'), ('3', '0-2'), ('(4, 6)', '4-6'), ('(8, 12)', '8-13'), ('13', '8-13'), ('22', '15-20'), ('(8, 23)','15-20'), ('23', '25-32'), ('(15, 20)', '15-20'), ('(25, 32)', '25-32'), ('(27, 32)', '25-32'), ('32', '25-32'), ('34', '25-32'), ('29', '25-32'), ('(38, 42)', '38-43'), ('35', '38-43'), ('36', '38-43'), ('42', '48-53'), ('45', '38-43'), ('(38, 43)', '38-43'), ('(38, 42)', '38-43'), ('(38, 48)', '48-53'), ('46', '48-53'), ('(48, 53)', '48-53'), ('55', '48-53'), ('56', '48-53'), ('(60, 100)', '60+'), ('57', '60+'), ('58', '60+')]
# age_mapping_dict = {each[0]: each[1] for each in age_mapping}
# drop_labels = []
# for idx, each in enumerate(imp_data.age):
#     if each == 'None':
#         drop_labels.append(idx)
#     else:
#         imp_data.age.loc[idx] = age_mapping_dict[each]
# imp_data = imp_data.drop(labels=drop_labels, axis=0) #droped None values
# imp_data.age.value_counts(dropna=False)
#
# imp_data = imp_data.dropna()
# clean_data = imp_data[imp_data.gender != 'u'].copy()
#
# gender_to_label_map = {
#     'f' : 0,
#     'm' : 1
# }
# clean_data['gender'] = clean_data['gender'].apply(lambda g: gender_to_label_map[g])
#
# clean_data.to_csv("adience_age_gender", index=False)

# adience_age_gender = pd.read_csv("./utkface/adience_age_gender")
# #
# age = adience_age_gender["age"]
# gender = adience_age_gender["gender"]
# img_path = adience_age_gender["img_path"]
# img_pather = img_path
# #img_path = img_path.values.tolist()
# #img_path_1 = os.path.basename(img_path)
#
# # #img_path = img_path[0].split(sep = "/")
# list = []
# list_1 = []
# for i in img_path:
#     img_path = i.split(sep = "/")
#     img_path_1 = img_path[5]
#     list.append(img_path_1)
# img_path_1 = pd.Series(list)
# img_path_1 = pd.DataFrame(list)
#
# for i in img_pather:
#     img_path = i.split(sep = "/")
#     img_path_2 = img_path[-2] + "/" + img_path[-1]
#     list_1.append(img_path_2)
# img_path_2 = pd.Series(list_1)
# img_path_2 = pd.DataFrame(list_1)
#
# #adience_age_gender = pd.concat([age, gender, img_path], axis = 1)
# #adience_age_gender.to_csv("clean_adience_age_gender", index=False)
#
# #adience_age_gender = pd.read_csv("./utkface/Adience/clean_adience_age_gender")
#
# original_img = "/home/mujung/PycharmProjects/Age-Gender-Pred-master/utkface/Adience/faces/"
# #original_img = glob.glob(original_img + '**/*.jpg' ,recursive=True)
# newName = pd.concat([age, gender, img_path_1], axis=1)
# newName = newName.values.tolist()
# list_3 = []
# for value in newName:
#     convert_name = str(value[0]) + '_' + str(value[1]) + '_' + str(value[2])
#     list_3.append(convert_name)
# newName = pd.DataFrame(list_3)
#
# df = pd.DataFrame()
#
# for a in range(len(img_path_2)):
#     print(a)
#     print("-------")
#     img_name = newName
#     img_path_3 = original_img + img_path_2[a]
#     img_path_3 = img_path_3.values.tolist()
#
#
#     # for i in range(len(img_path_3)):
#     #     dirs = img_path_3[i].split("/")[1:]
#     #     for j in range(len(dirs)):
#     #         df.iloc[i][j] = dirs[j]
#     #
#     #
#     #
#     #
#     # #img_path_3 = [img_path_3[0], img_path_3[1], img_path_3[2], img_path_3[3], img_path_3[4], img_path_3[5], img_path_3[6], img_path_3[7], img_path_3[8], img_path_3[9]]
#     # #img_path_3 = "/".join(img_path_3)
#     # #img_path_3 = pd.Series(img_path_3)
#     # shutil.copy(img_path_3, f'/home/mujung/PycharmProjects/Age-Gender-Pred-master/utkface/new_image/{img_name}')
link = "/home/mujung/PycharmProjects/Age-Gender-Pred-master/utkface/new_image"
dataset = glob.glob(link + "/*.jpg",recursive=True)


print(len(dataset))
for i in dataset:
    org_file = i.split(sep = "/")[-1]
    age = org_file.split(sep= "_")[0]
    gender = org_file.split(sep= "_")[1]
    img_path = org_file.split(sep="_")[2]
    if '-' in age:
        new_file = org_file
    else:
        if "60+" in age:
            new_file = org_file
        else:
            age = int(age)
            if (age >= 0 and age <= 3):
                age = '0-2'
            elif (age >= 4 and age <= 7):
                age = '4-6'
            elif (age >= 8 and age <= 14):
                age = '8-13'
            elif (age >= 15 and age <= 24):
                age = '15-20'
            elif (age >= 25 and age <= 37):
                age = '25-32'
            elif (age >= 38 and age <= 47):
                age = '38-43'
            elif (age >= 48 and age <= 59):
                age = '48-53'
            else:
                age = '60+'

            new_file = age + "_" + gender + "_" + img_path
    load_img = cv2.imread(i)
    cv2.imwrite(f"/home/mujung/PycharmProjects/Age-Gender-Pred-master/utkface/new_image2/{new_file}", load_img)



