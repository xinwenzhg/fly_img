#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:46:09 2021

@author: xinwenzhang
"""
from pathlib import Path

dataset_path = Path(r"/ufgi-vulcana/data/xinwen_local/fly_ml_xwz/ml_workspace")
Path.mkdir(dataset_path / "check_points", exist_ok=True)

model.fit(
    train_images =  dataset_path/"train_img",
    train_annotations =  dataset_path/"train_annot",
    checkpoints_path =  dataset_path/"check_points" ,
    epochs=5
)

model.fit(train_gen.generate(),
          validation_data=val_gen.generate(),
          validation_steps=4,
          steps_per_epoch=10,
          epochs=5,
          callbacks=callbacks )