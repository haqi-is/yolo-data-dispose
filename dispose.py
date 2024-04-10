import os
import random
import shutil
score_images_path = r'标注照片的存放文件夹'
score_labels_path = r'标注标签的存放文件夹'
des_path = r'想要构建在哪一个文件夹下,会自动创建目录'


def auto_split_flie():
#     创建文件夹
    for i in ['images','labels']:
        for x in ['train','val','test']:
            os.makedirs(os.path.join(des_path,"score",i,x))
#     按比例随机分割
    images_list = os.listdir(score_images_path)
    num = len(images_list)
    random.shuffle(images_list)
    train_data,test_data,val_data = images_list[0:num//2],images_list[num//2:num*3//4],images_list[num*3//4:num]
    dict_data = {'train':train_data,'test':test_data,'val':val_data}
    for i in dict_data:
        for y in dict_data[i] :
            shutil.copy(os.path.join(score_images_path,y),os.path.join(des_path,'score','images',i,y))
            label_name = y.split('.')[0]+'.txt'
            shutil.copy(os.path.join(score_labels_path,label_name),os.path.join(des_path,'score','labels',i,label_name))
        shutil.copy(os.path.join(score_labels_path,'classes.txt'),os.path.join(des_path,'score','labels',i,'classes.txt'))
auto_split_flie()