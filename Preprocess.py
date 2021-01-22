import cv2
import numpy as np 
import glob
import os

for fileImg in glob.glob("/home/nguyetgt/Projects/ChuyenDe1/Data_face_base/*.jpg"):
    img = cv2.imread(fileImg)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgName = os.path.splitext(os.path.basename(fileImg))[0]
    height = img.shape[1]
    width = img.shape[0]
    w= width-200
    h = height-100
    start_row,start_col=100,100
    end_row,end_col=w,h
    # crop Image
    cropped=img[start_row:end_row,start_col:end_col]
    resize = cv2.resize(cropped,(256,256), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("/home/nguyetgt/Projects/ChuyenDe1/DataFace_created/GroundTruth/{}.jpg".format(imgName),resize)
    #  convert Skecth
    grayImg = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
    invert_gray_imd= 255-grayImg
    blurred_img= cv2.GaussianBlur(invert_gray_imd, (21,21),0)
    inverted_blurr_img = 255-blurred_img
    skecthImg = cv2.divide(grayImg, inverted_blurr_img,scale= 256)
    cv2.imwrite("/home/nguyetgt/Projects/ChuyenDe1/DataFace_created/Skecth/{}.jpg".format(imgName),skecthImg)
    # combine two image
# combine = []
# Gtruth = []
# skecth= []
# base_root = '/home/nguyetgt/Projects/ChuyenDe1/DataFace_created'
# i = 0
# for fileName in glob.glob("/home/nguyetgt/Projects/ChuyenDe1/DataFace_created/GroundTruth/*.jpg"):
#     name = os.path.splitext(os.path.basename(fileName ))[0]
#     G = Gtruth.append(base_root+"/GroundTruth/"+name+".jpg")
#     S =skecth.append(base_root+"/Skecth/"+name+".jpg")
#     #  print(imgName1 , imgName2)
#             # img1 = cv2.imread(fileName)
#             # img2 = cv2.imread(fileName2)
#             # img2 = np.fliplr(img2)
#             # out = np.concatenate((img1, img2),axis=1)
#     cv2.imwrite("/home/nguyetgt/Projects/ChuyenDe1/DataFace_created/combine/{}.jpg".format(name),out)
   