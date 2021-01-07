# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 22:49:57 2020

@author: -
"""
import os
import glob

#path = 'D:/ridvan_2020/01_gelisim/python_ornekleri/furkan'
path = 'D:/ridvan_2020/05_PhD/YOLO/tik_2/yedekler/R_F_D_Mega_09'
#D:\ridvan_2020\05_PhD\YOLO\tik_2\yedekler\R_F_D_Bigger_v2_09
#D:\ridvan_2020\05_PhD\YOLO\tik_2\yedekler\First_Plus_07

# set all object number's value to zero 
sleeper = 0
foreign_object= 0
bolt= 0
head_check= 0
fastening= 0
sleeper_crack= 0
rail_crack= 0
fastening_rotated_deformed= 0
corrugation= 0
squat= 0
surface_defect= 0
i=0    

# read all YOLOv4 format labeling text files in the dataset folder and count object's number    
for filename in glob.glob(os.path.join(path, '*.txt')):
   with open(filename, 'r') as f: # open in readonly mode
       for satır in f:
           sinif = satır.split(' ')[0]
           print(sinif)
           i+=1
           if (sinif == "0"):
               sleeper+=1
           elif (sinif == "1"):
               foreign_object+=1
           elif (sinif == "2"):
               bolt+=1
           elif (sinif == "3"):
               head_check+=1
           elif (sinif == "4"):
               fastening+=1
           elif (sinif == "5"):
               sleeper_crack+=1
           elif (sinif == "6"):
               rail_crack+=1
           elif (sinif == "7"):
               fastening_rotated_deformed+=1
           elif (sinif == "8"):
               corrugation+=1
           elif (sinif == "9"):
               squat+=1
           elif (sinif == "10"):
               surface_defect+=1       
    
print(i, "number of total object")