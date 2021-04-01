#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:46:09 2021

@author: xinwenzhang
"""
from pathlib import Path

dataset_path = Path(r"/ufgi-vulcana/data/xinwen_local/fly_ml_xwz/ml_workspace")
Path.mkdir(dataset_path / "check_points", exist_ok=True)

ti = dataset_path/"train_img"
ta = dataset_path/"train_annot"
cp = dataset_path/"check_points"

vi = dataset_path/"val_img" / "18_1-5.png"

model.train(
    train_images =  str(ti),
    train_annotations =  str(ta),
    checkpoints_path =  str(cp) ,
    epochs=1
)


out = model.predict_segmentation(
    inp=str(vi),
    out_fname="output.png"
)
o = Image.open("output.png")
o
model.predict()
