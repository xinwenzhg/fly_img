#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:34:23 2021

This script
@author: xinwenzhang
"""

from pathlib import Path
from custom_module import *

#hpc_folder = Path(r"T:\share\fly_image_analysis\human_labeled\fly_seg_4objects")
hpc_folder = Path(r"/nfshome/xinwenzhang/mnt/exasmb.rc.ufl.edu-blue/mcintyre-cid/share/fly_image_analysis/human_labeled/fly_seg_4objects")

# this script is to make two folders, one is for original image, one is for annot_images,and one for check annot.
# first generate , the annot image, and a check folder
# then crop the images and save
# the core is to loop through all images under fly_seg_4objects.


# define the color
annot_dict = {"a_abd":1, "a_head":2,"a_thorax":3, "a_thorax_shed":4}
tint_color={0:[255,255,255], # white , the background
            1:[255,0,0], # red
            2:[0,0,255], # blue
            3:[255,255,0], # yellow
            4:[0,255,255]} # cyan


# create a folder to put
#p = Path(r"E:\xinwe\proj_mng\fly_im_xwz")
p = Path(r"/ufgi-vulcana/data/xinwen_local/fly_ml_xwz")
Path.mkdir(p / "ml_workspace", exist_ok=True)
Path.mkdir(p / "ml_workspace" / "rgb_img", exist_ok=True)
Path.mkdir(p / "ml_workspace" / "annot_img", exist_ok=True)
Path.mkdir(p / "ml_workspace" / "check_annot", exist_ok=True)

pwks = Path(p / "ml_workspace")



for i in hpc_folder.iterdir():
     if str(i.name).startswith(("1","2")): # make sure to get the correct folder
         print(i.name)

         im_org = Image.open(i / (str(i.name) + ".png"))
         im_annot = create_annot_img(i , annot_dict)
         im_tint =  tint_annot_image(im_annot,tint_color)


         abd_mask = Image.open(i / "class_masks" / "a_abd.png")
         fly_center = find_object_center(abd_mask)

         # crop org and annot image and tinted annot
         im_org_crop = crop_side_img(im_org, fly_center, goal_width=500)
         im_annot_crop = crop_side_img(im_annot, fly_center, goal_width=500)
         im_tint_crop = crop_side_img(im_tint, fly_center, goal_width=500)

         im_org_crop.save(pwks / "rgb_img" / (str(i.name) + ".png"))
         im_annot_crop.save(pwks / "annot_img" /(str(i.name) + ".png"))
         im_tint_crop.save(pwks / "check_annot" /(str(i.name) + ".png") )












