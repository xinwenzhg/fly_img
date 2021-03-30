#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 12:23:41 2021

@author: xinwenzhang
"""

im_test = Image.open("/ufgi-vulcana/data/xinwen_local/keras_example_divam/test/example_dataset/annotations_prepped_test/0016E5_07959.png")

ary_test = np.asarray(im_test)


im_folder_path = Path("/nfshome/xinwenzhang/mnt/exasmb.rc.ufl.edu-blue/mcintyre-cid/share/fly_image_analysis/human_labeled/fly_seg_4objects")
im_name = "18_1-1"

a = Image.open(im_folder_path / im_name /"class_masks"/ "a_abd.png").load()
a[825,218]

b = Image.open(im_folder_path / im_name /"class_masks"/ "a_thorax.png").load()
b[825,218]

c = Image.open(im_folder_path / im_name /"class_masks"/ "a_head.png").load()
c[825,218]

d = Image.open(im_folder_path / im_name /"class_masks"/ "a_thorax_shed.png").load()
d[825,218]

ary_test = np.array([[0,1,2,3],[4,5,0,1]],dtype="uint8") # only uin8 works!!
ary_test
ary_test.shape

img_test = Image.fromarray(ary_test, mode="L")
img_test.size
np.asarray(img_test)

h = tint_annot_image(img_test,tint_color)
