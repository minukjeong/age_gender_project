import copy
import os
import re
import time

import cv2
import glob
import torch
import shutil
from config import config
from train import AgePredModel
#from preprocess import clear_dir
from skimage import io
from agegenpredmodel import AgeGenPredModel
from face_detection import RetinaFace
#from retinaface import RetinaFace
from skimage.transform import resize
os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1'
CUDA_AVAILABLE = torch.cuda.is_available()
DEVICE = torch.device("cuda" if CUDA_AVAILABLE else "cpu")

def eval_single(img,
                model = None):
  if type(img) == str:
    img = cv2.imread(img)

  if not model:
    model = AgePredModel(eval_use_only=True)
  int2gender = {0: "Female", 1: 'Male'}

  # input image
  preds, rects, scores = model.getAgeGender(img,
                                            transformed=False,
                                            return_all_faces=True,
                                            return_info=True)


  gen_pred, age_pred = -1, -1
  for pred, (x, y, h, w), score in zip(preds, rects, scores):
    # model predictions
    gen_pred, gen_prob, age_pred, age_var = pred
    age_pred, gen_pred = float(age_pred), int(gen_pred)
    age_var, gen_prob = int(age_var), float(gen_prob)
    # vars

    color = (255, 0, 0) if gen_pred == 1 else (0, 0, 255)
    fontscale = min(1.5, max(0.3, max(w, h) / 500))
    fill_h = int(35 * fontscale)
    font_h = int(6 * fontscale)
    thickness = 1 if fontscale <= 1 else 2

    # draw a rectange to bound the face
    cv2.rectangle(img, (x, y), (x + w, y + h), color, 4)

    # fill an area with color for text show
    cv2.rectangle(img, (x, y + h - fill_h), (x + w, y + h), color, cv2.FILLED)

    # put text
    font = cv2.FONT_HERSHEY_DUPLEX

    cv2.putText(img,
                "{:.0f}% {}, {:.0f} +/- {}".format(100 * gen_prob,
                                                   int2gender[gen_pred],
                                                   age_pred,
                                                   age_var),
                org=(x + 6, y + h - font_h),
                fontFace=font,
                fontScale=fontscale,
                color=(255, 255, 255),
                thickness=thickness)
  return img, gen_pred, age_pred



def eval_batch(path,
               model_name,
               name_contain_label = False,
               result_path = None):
  """
  function used to test a folder of images
  :param path: folder path, e.g. config.val, last char should be '/'
  :param name_contain_label: if set, label is extracted from image name
  :param result_path: path to store the result, default path + "test_results/"
  :return: 
  """
  # check param: path
  if path[-1] != "/":
    print("[WARNING] PARAM: path NOT ENDS WITH '/'!")
    path += '/'

  # check param: result_path
  if result_path is None:
    result_path = path + "all_results/"
  false_results = result_path + "false_results/"
  all_results = result_path + "all_results/"

  # make sure it exists and is empty
  if not os.path.exists(result_path):
    os.mkdir(result_path)
#  clear_dir(result_path)

  if not os.path.exists(all_results):
    os.mkdir(all_results)

  # also the false preds samples if we know the label
  if name_contain_label:
    if not os.path.exists(false_results):
      os.mkdir(false_results)
 #   clear_dir(false_results)


  # start eval
  model = AgePredModel(eval_use_only=True, model_name=model_name)
  gen_sum = 0
  age_sum = 0
  for img_path in glob.glob(path + "*"):
    # only load 'png', 'jpg', 'jpeg' images
    img_name = img_path[len(path):]
    formatt = re.findall("[^.]*.([^.]*)", img_name)[0]
    # formatt = re.findall("[^.]*.([^.]*)", img_name)[0]
    if not formatt: continue
    formatt = formatt.lower()
    if not formatt in ['png', 'jpg', 'jpeg']: continue

    # image qualified for eval
    print("[evaluate] evaluating {}".format(img_name))
    #img = cv2.imread(img_path)
    img = io.imread(img_path)
    img, gen_pred, age_pred = eval_single(img, model)

    age = img_name[0]
    age = int(age)
    gen = img_name[2]
    gen = int(gen)

    age_round = round(age_pred, 0)

    if gen == gen_pred:
      gen_sum += 1

    if age == age_round:
      age_sum += 1
    #else:
      #cv2.imwrite(all_results + img_name, img)


    # write the result
    cv2.imwrite(all_results + img_name, img)

    # if labeled
    if name_contain_label:
      try:
        (age, gender) = re.findall(r'([^_]*)_([^_]*)_*', img_name)[0]
        age, gender = int(age), int(gender)
        if abs(age - age_pred) >= 5:
          cv2.imwrite(false_results + img_name, img)
      except:
        print("Error while extracting labels from {}".format(img_name))
  print("[evaluate] Done!")
  print("gender sum", gen_sum)
  print("age sum", age_sum)
  print("gender_acc {}".format(gen_sum / 700))
  print("age_acc {}".format(age_sum / 700))


def eval_live():
  os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'
  video_file = config.pics + "video7.mp4"
  cap = cv2.VideoCapture(video_file)
  model = AgePredModel(eval_use_only=True) # resnet18 -> classification


#  retinaface = RetinaFace.build_model().cuda()

  while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    t1 = time.time()
    detector = RetinaFace(gpu_id=0)
    faces = detector(frame)
    box, landmarks, score = faces[0]
    #obj = RetinaFace.detect_faces(frame, model=retinalface)
    # filtering
    list = []
    for face in faces:
        if face[2] >= 0.9:
            list.append(face)
        else:
          continue

    for li in list:
      i = li[0]

      crop = frame[int(i[1]):int(i[3]), int(i[0]):int(i[2])]
      _, gender_pred, age_pred = eval_single(crop, model)

    print(f'{time.time() - t1:.3f}s')
    # img = RetinaFace.extract_faces(frame, align = True)
    # for key in faces.keys():
    #   identity = faces[key]
    #   # print(identity)
    #   facial_area = identity['facial_area']
    #   cv2.rectangle(frame, (facial_area[2], facial_area[3]), (facial_area[0], facial_area[1]), (255, 255, 255), 1)
    #   crop = frame[facial_area[1]:facial_area[3], facial_area[0]:facial_area[2]]
    #   _, gender_pred, age_pred = eval_single(crop, model)

    #labeled, _, _ = eval_single(img, model)
    #labeled, _, _ = eval_single(frame, model)
    #labeled = torch.Tensor(labeled).cuda()
    #label = torch.Tensor(copy.deepcopy(labeled)).cuda()
    #modifix

    # Display the resulting frame
    cv2.imshow('frame', frame)
    #cv2.imshow('frame', labeled)

    #cv2.imshow('frame', obj)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # When everything done, release the capture
  cap.release()
  cv2.destroyAllWindows()


if __name__ == "__main__":
  # eval_batch(config.pics + "archive/Validation/aligned",
  #            model_name='res18_cls70',
  #            name_contain_label=False)
  eval_live()
  pass


























