import img2pdf
import os
import pprint

most_dir = r'f:\Users\25766\Desktop\信院\离散数学\离散数学答案'
imgs = []
imgs_all = []
sec_list = []

for dir in os.listdir(most_dir):
    sec_path = os.path.join(most_dir,dir)
    sec_list.append(sec_path)

thi_list = sec_list[10:]+sec_list[0:10]
#pprint.pprint(thi_list)

for dir3 in thi_list:
    thu_list = os.listdir(dir3)
    thu_list.sort(key=lambda x:int(x.split('.')[0]))
    for f_dir in thu_list:
        fdir = os.path.join(dir3,f_dir)
        imgs.append(fdir)
    with open(f'{dir3}答案.pdf','wb') as f:
        f.write(img2pdf.convert(imgs))
    imgs_all += imgs
    imgs = []

with open(f'{most_dir}/离散数学.pdf','wb') as a:
    a.write(img2pdf.convert(imgs_all))
    