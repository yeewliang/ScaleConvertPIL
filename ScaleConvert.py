#!/usr/bin/env python3

#Automating Real-World Tasks with Python Week 1 Assignment

from PIL import Image
import os
#from pathlib import Path

curDir = "/images"
newDir = "/opt/icons/"

# go through each file
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for file in files:
  if not file.endswith(".py"):
    print(file)
    im = Image.open(file)
    new_im = im.rotate(-90).resize((128,128)).convert("RGB")
    new_im.save(newDir + file + ".jpeg")

