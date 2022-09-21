import cv2
# import matplotlib.pyplot as plt
import numpy as np
import os
# TODO: 遍历1级文件
# import os
# for filename in os.listdir(r'D:\PyCharm_project\detect_circle\read_all_file\已完成10-99'):
#     print(filename)

# TODO: 对图进行标框
color_dist = {
    'red': {'Lower1': np.array([0, 43, 46]), 'Lower2': np.array([156, 43, 46]),
            'Upper1': np.array([10, 255, 255]), 'Upper2': np.array([180, 255, 255])},
    'yellow': {'Lower': np.array([15, 160, 50]), 'Upper': np.array([35, 255, 255])},
    'blue': {'Lower': np.array([78, 43, 43]), 'Upper': np.array([130, 255, 255])},
    }
# epsilon是"代表实际轮廓和近似轮廓之间的最大距离并代表近似精度的参数"
epsilon = 0.0005

# 定义一个展示图片的函数
def cv_show(name, img):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 500, 500)
    cv2.imshow(name, img)

def plot_counter(parent, img, name):
    img = cv2.imread(parent + '\\' + img)  # 读入图像（直接读入灰度图）
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv_show('Original_image', img)

    ## Yellow
    # find the yellow contours
    Yellow_mask = cv2.inRange(hsv, color_dist['yellow']['Lower'], color_dist['yellow']['Upper'])
    Yellow_contour = cv2.bitwise_and(hsv, hsv, mask=Yellow_mask)
    # fill the contours
    color = cv2.cvtColor(Yellow_contour, cv2.COLOR_BGR2GRAY)
    Yellow_contour_gray1 = color
    Yellow_contours, Yellow_hierarchy = cv2.findContours(Yellow_contour_gray1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    Yellow_contours_approx = cv2.approxPolyDP(Yellow_contours[0], epsilon, True)  # 轮廓线近似
    Yellow_con_fill = cv2.fillPoly(Yellow_contour_gray1, [Yellow_contours_approx], (255, 0, 0))


    ## Blue
    # find the blue contours
    Blue_mask = cv2.inRange(hsv, color_dist['blue']['Lower'], color_dist['blue']['Upper'])
    Blue_contour = cv2.bitwise_and(hsv, hsv, mask=Blue_mask)
    # 多边形近似
    Blue_contour_gray1 = cv2.cvtColor(Blue_contour, cv2.COLOR_BGR2GRAY)
    Blue_contours, Blue_hierarchy = cv2.findContours(Blue_contour_gray1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if (type(Blue_hierarchy) == type(None)):
        Blue_con_fill = np.zeros(Yellow_con_fill.shape)
    else:
        Blue_contours_approx = cv2.approxPolyDP(Blue_contours[0], epsilon, True)  # 轮廓线近似
        Blue_con_fill = cv2.fillPoly(Blue_contour_gray1, [Blue_contours_approx], (255, 0, 0))



    ## Red
    # find the red contours
    Red_mask1 = cv2.inRange(hsv, color_dist['red']['Lower1'], color_dist['red']['Upper1'])
    Red_mask2 = cv2.inRange(hsv, color_dist['red']['Lower2'], color_dist['red']['Upper2'])
    Red_mask = Red_mask1 + Red_mask2 # 红色有两种色域，需要特殊处理
    Red_contour = cv2.bitwise_and(hsv, hsv, mask=Red_mask)
    # fill the contours
    Red_Blue_Yellow_cont = Blue_contour + Yellow_contour+ Red_contour# 因为红色边框不全，只能用减的方法进行处理
    # cv_show('Blue_Yellow_cont', Red_Blue_Yellow_cont)
    Red_Blue_Yellow_cont_gray = cv2.cvtColor(Red_Blue_Yellow_cont, cv2.COLOR_BGR2GRAY)# 所有的轮廓进一步处理
    Red_Blue_Yellow_contours, hierarchy = cv2.findContours(Red_Blue_Yellow_cont_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)# 再次寻找轮廓，是最外层的轮廓
    Red_Blue_Yellow_cont_approx = cv2.approxPolyDP(Red_Blue_Yellow_contours[0], epsilon, True)  # 轮廓线近似
    contours_all = cv2.fillConvexPoly(Red_Blue_Yellow_cont_gray, Red_Blue_Yellow_cont_approx, (255, 0, 0)) # 填充边界
    Red_contours_fill = contours_all- Yellow_con_fill- Blue_con_fill

    # a = np.load('PA0-ED-2.npz')
    # 全部和在一起，着色
    img_contours = np.zeros(img.shape)
    img_contours[:, :, 0] = Blue_con_fill
    img_contours[:, :, 1] = Red_contours_fill
    img_contours[:, :, 2] = Yellow_con_fill
    ## 保存原图，调色后的图，心肌(myocardium), 左心室(LV), 右心室(RV)
    # np.savez(parent + '\\' +name+'.npz', Image_comtours_Fill=img_contours, Original_image=img, MC=Red_contours_fill, LV=Yellow_con_fill, RV=Blue_con_fill)
    # a = np.load(parent + '\\' + name+'.npz')

    cv2.imwrite(parent + '\\' + name+'_contours.jpg', img_contours)
    cv_show(parent + '\\' + 'Image_contours', img_contours)
    # cv2.waitKey(0)

# TODO: 遍历1级文件下的所有文件
current_address = os.path.dirname(os.path.abspath('D:\\PyCharm_project\\detect_circle\\2_read_all_file\\PA18'))
for parent, dirnames, filenames in os.walk(current_address):
     # Case1: traversal the directories
     for dirname in dirnames:
        print("Parent folder:", parent)
        print("Dirname:", dirname)
     # Case2: traversal the files
     for filename in filenames:
         print("Parent folder:", parent)
         print("Filename:", filename)
         img_name, img_type = os.path.splitext(filename)
         if (img_type == '.png'):
            plot_counter(parent, filename, img_name)
