# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 08:24:21 2021

@author: xinwe
"""

from pathlib import Path
import random
import shutil


val_num = 4

#p = Path(r"E:\xinwe\proj_mng\fly_im_xwz")
p = Path(r"/ufgi-vulcana/data/xinwen_local/fly_ml_xwz")

pwks = p / "ml_workspace"

Path.mkdir(pwks / "train_img", exist_ok=True) # just no error, won't rewrite the folder
Path.mkdir(pwks / "train_annot", exist_ok=True)
Path.mkdir(pwks / "val_img", exist_ok=True)
Path.mkdir(pwks / "val_annot", exist_ok=True)

imgs = (pwks/"check_annot"). iterdir()
num_imgs = len(list(imgs)) # imgs is a generator, once count, need to init again
chosed_imgs = [random.randrange(0, num_imgs, 1) for i in range(val_num)]  # random choose val_num of images from pool


imgs = (pwks/"check_annot"). iterdir()
k = 0
for i in imgs:
    print(k)
    print(i.name)
    if k in chosed_imgs: # to val folder
        from_rgb_img = pwks / "rgb_img" / i.name
        to_rgb_img = pwks / "val_img" / i.name

        from_annot_img = pwks / "annot_img" / i.name
        to_annot_img = pwks / "val_annot" / i.name

    else:
        from_rgb_img = pwks / "rgb_img" / i.name
        to_rgb_img = pwks / "train_img" / i.name

        from_annot_img = pwks / "annot_img" / i.name
        to_annot_img = pwks / "train_annot" / i.name

    shutil.copy(str(from_rgb_img), str(to_rgb_img))  # For older Python.
    shutil.copy(str(from_annot_img), str(to_annot_img))  # For newer Python.
    k += 1
