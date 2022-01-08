# 批处理含有LV，RV和MC的图片
import os
import numpy as np
import cv2
from Single_Image_detect_all_Circle import Single_Image_Detect_ThreeCicle,Single_Image_Detect_TwoCicle

target_color = ['ED', 'ES']

num=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def cv_show(name, img):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 500, 500)
    cv2.imshow(name, img)

# 批处理含有LV，RV和MC的图片
# for t in target_color:
#     for i  in num:
#         for filename in os.listdir(r'E:/png_lable_process(22.1.8)/PA'+str(i) +'/'+ t):
#             if filename.endswith('png') :
#                 img = cv2.imread('E:/png_lable_process(22.1.8)/PA'+str(i) +'/'+ t +'/'+filename)
#                 img_contours, Red_contours_fill, Yellow_con_fill, Blue_con_fill = Single_Image_Detect_ThreeCicle(img)
#                 # 保存处理后的图片
#                 suffix = filename.split(".")[0]
#                 # np.savez(suffix+'.npz', Image_comtours_Fill=img_contours, Original_image=img, MC=Red_contours_fill,
#                 #          LV=Yellow_con_fill, RV=Blue_con_fill)
#                 cv2.imwrite('E:/png_lable_process(22.1.8)/PA'+str(i) +'/'+ t +'/'+suffix+'-contours.jpg', img_contours)
#                 # cv_show('img', img)
#                 # cv_show('img_contours', img_contours)
#                 # cv2.waitKey(0)


## 批处理含有LV和MC的图片
for filename in os.listdir(r'E:\png_lable_process(22.1.8)\deal_with_separate'):
    if filename.endswith('png') :
        img = cv2.imread('E:\png_lable_process(22.1.8)\deal_with_separate' +'/'+filename)
        img_contours, Red_contours_fill, Yellow_con_fill, Blue_con_fill = Single_Image_Detect_TwoCicle(img)
        # 保存处理后的图片
        suffix = filename.split(".")[0]
        # np.savez(suffix+'.npz', Image_comtours_Fill=img_contours, Original_image=img, MC=Red_contours_fill,
        #          LV=Yellow_con_fill, RV=Blue_con_fill)
        cv2.imwrite('E:\png_lable_process(22.1.8)\deal_with_separate' +'/'+suffix+'-contours.jpg', img_contours)
