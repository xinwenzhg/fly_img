# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 05:58:26 2021

@author: xinwe
"""

from PIL import Image
import numpy as np
from pathlib import Path


def find_object_center(im_mask):# input a mask, output a tuple, the row and col of center point
    ary = np.asarray(im_mask.convert("L", dither=None)) # make it grey scale, reduce from 3 to 2 dimention array
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


def create_annot_img(img_folder, annot_dict):
     # img_folder is a Path object  #

    class_masks_path = img_folder / "class_masks"

    im_mask_abd = Image.open(class_masks_path / "a_abd.png") # take this mask to get image size
    width = im_mask_abd.size[0]
    height = im_mask_abd.size[1]

    # init the annot channel, and loop through all masks
    annot_channel = np.zeros((height, width),dtype="uint8")
    for key in annot_dict.keys():
        #print(key)
        mask_filename =  key + ".png"
        
        try:
            im_mask_one = Image.open(class_masks_path / mask_filename )
        except FileNotFoundError:
            print(key, 'not found')
            continue
        ary_mask_one = np.asarray(im_mask_one.convert("1",dither=None), dtype="uint8")   # 0/1 image.

        #print(np.amax(ary_mask_one))
        #print(np.amin(ary_mask_one))
        #print(annot_dict[key])
        annot_channel +=  annot_dict[key] * ary_mask_one
        #print(annot_channel)
    #return(annot_channel)
    return Image.fromarray(annot_channel, mode="L")  # annot_channel must be in "uint8" format.

def tint_annot_image(annot_img, tint_color): # annot should be in "L" mode
    width, height = annot_img.size
    ary_annot = np.asarray(annot_img, dtype="uint8")

    #print(np.amax(ary_annot))
    #print(np.amin(ary_annot))

    ary_tinted = np.zeros((height, width, 3), dtype="uint8")
    for key in tint_color.keys():  # change color to RGB
        #print(key)
        #print(tint_color[key])
        ary_tinted[ary_annot == key] = tint_color[key]
        #print(ary_tinted)

    return(Image.fromarray(ary_tinted, mode="RGB"))
    #return(ary_tinted)
