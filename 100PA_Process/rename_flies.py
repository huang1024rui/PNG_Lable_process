import os

# 图片所在路径
counter_path = "D:\\PyCharm_project\\detect_circle\\1_rename_png\\"
orignal_path = "D:\\PyCharm_project\\detect_circle\\10-99\\orignal\\"
t = 'PA26\\'
# root_path = "G:\\cardiac 数据\\处理后的文件\\counter\\PA27\\"
def rename_png(root_path, ED_or_ES):
    filename_list = os.listdir(root_path)
    no = 0
    for filename in filename_list:
        if filename.endswith('.png'):
            src_img_path = os.path.join(os.path.abspath(root_path), filename)
            # new_img_code = filename.split('_')[1].split('.')[0].zfill(5)
            if ED_or_ES == 0:
                # dst_img_path = os.path.join(os.path.abspath(root_path), 'ED_' + str(no) + '_counter.jpg')
                dst_img_path = os.path.join(os.path.abspath(root_path), 'ED_' + str(no) + '.png')
            if ED_or_ES == 1:
                # dst_img_path = os.path.join(os.path.abspath(root_path), 'ES_' + str(no) + '_counter.jpg')
                dst_img_path = os.path.join(os.path.abspath(root_path), 'ES_' + str(no) + '.png')

            no += 1
            try:
                os.rename(src_img_path, dst_img_path)
                print('converting %s to %s ...' % (src_img_path, dst_img_path))
            except:
                continue

if __name__=='__main__':
    # for i in range(28, 99):
    #     root_path = "D:\\PyCharm_project\\detect_circle\\1_rename_png\\pic\\PA" + str(i) + '\\'
    rename_png(counter_path + t + 'ED', ED_or_ES=0)
    rename_png(counter_path + t + 'ES', ED_or_ES=1)
    rename_png(orignal_path + t + 'ED', ED_or_ES=0)
    rename_png(orignal_path + t + 'ES', ED_or_ES=1)
