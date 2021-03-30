#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:34:23 2021

This script
@author: xinwenzhang
"""

from PIL import Image
import numpy as np
from pathlib import Path


def find_object_center(im_mask):# input a mask, output a tuple, the row and col of center point
    ary = np.asarray(im_mask.convert("L")) # make it grey scale, reduce from 3 to 2 dimention array
    mrow, mcol = np.where(ary == 255)
    center_row = round(np.median(mrow))  # not use mean() ,since some out of box labeling points may confuse the center,  eg. 18_1-3 head mask has several wrong points.
    center_col = round(np.median(mcol))
    return(center_row, center_col)

def crop_side_img(img, obj_center,goal_width):
    """
    Crop two sides of an img
    Parameters
    ----------
    img : An image in any mode
    obj_center : tuple, row and col, eg.(620,830)
        object center, need to provide an object center, since fly are not always in the center.
    goal_width : Int
        the goal witdth of an image

    Returns
    -------
    An croped image

    """

    im_rowC, im_colC = obj_center # get head mask center
    left = im_colC - goal_width/2
    right = im_colC + goal_width/2

    im_res = img.crop((left, 0 , right, img.size[1] ))

    return(im_res)


 # converts mask images into a multichannel array representing the different
  # classes within the image. If there are n classes, the image has n channels

def create_annot_img(img_folder, annot_dict):
     # img_folder is a Path object  #

    class_masks_path = img_folder / "class_masks"

    im_mask_abd = Image.open(class_masks_path / "a_abd.png") # take this mask to get image size
    width = im_mask_abd.size[0]
    height = im_mask_abd.size[1]

    # init the annot channel, and loop through all masks
    annot_channel = np.zeros((height, width),dtype="int8")
    for key in annot_dict.keys():
        #print(key)
        mask_filename =  key + ".png"
        im_mask_one = Image.open(class_masks_path / mask_filename )
        print(im_mask_one.mode)
        ary_mask_one = np.asarray(im_mask_one.convert("1",dither=None))   # 0/1 image.

        print(np.amax(ary_mask_one))
        print(np.amin(ary_mask_one))
        print(annot_dict[key])
        annot_channel +=  annot_dict[key] * ary_mask_one

    return(annot_channel)
    #return Image.fromarray(annot_channel, mode="L")

def tint_annot_image(annot_img, tint_color): # annot should be in "L" mode
    width, height = annot_img.size
    ary_annot = np.asarray(annot_img)

    print(np.amax(ary_annot))
    print(np.amin(ary_annot))

    ary_tinted = np.zeros((height, width, 3), dtype=int)
    for key in tint_color.keys():  # change color to RGB
        print(key)
        print(tint_color[key])
        ary_tinted[ary_annot == key] = tint_color[key]
        print(ary_tinted)

    #return(Image.fromarray(ary_tinted, mode="RGB"))
    return(ary_tinted)





tint_color={0:[255,255,255], # white , it the background
            1:[255,0,0], # red
            2:[0,0,255], # blue
            3:[255,255,0], # yellow
            4:[0,255,255]} # cyan

tint_color={0:[255,255,255], # white , it the background
            1:[0,0,0], # red
            2:[0,0,0], # blue
            3:[0,0,0], # yellow
            4:[0,0,0]} # cyan

h = tint_annot_image(d,tint_color)


d = create_annot_img(test_folder, annot_dict)

im_folder_path = "/nfshome/xinwenzhang/mnt/exasmb.rc.ufl.edu-blue/mcintyre-cid/share/fly_image_analysis/human_labeled/fly_seg_4objects"
im_name = "18_1-1"
part = "thorax"

im_org = Image.open(im_folder_path + "/" + im_name + "/" + im_name + '.png')
im_mask = Image.open(im_folder_path + "/" + im_name + "/" + "class_masks/" + "a_"+ part +".png") # get mask

# find center from thorax mask
fly_center = find_object_center(im_mask)
crop_side_img(im_org, fly_center, goal_width=500)

annot_dict = {"a_abd":1, "a_head":2,"a_thorax":3, "a_thorax_shed":4}