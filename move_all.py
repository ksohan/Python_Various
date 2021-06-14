"""
Created on Tue Jun  15 02:51:55 2021

@author: Sohan

@ Move all file from src directory to dest directory
"""

from shutil import move
import os

src_folder = "D:\\RF\\DroneRF-master\\data\\"
dest_folder = "D:\\RF\\DroneRF-master\\data2\\"
files = os.listdir(src_folder)
for file in files:
    move(src_folder + file, dest_folder + file)
