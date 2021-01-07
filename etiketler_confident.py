# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:52:49 2020

@author: Ridvan
"""
import os
import pandas as pd
import json
import shutil

# read json file to get label informations
with open('result_mega.json','r') as f:
    data = json.loads(f.read())

# source and target directories 
kaynak = r'D:/ridvan_2020/05_PhD/RAIL/Etiketsiz_Test/'
hedef = r'D:/ridvan_2020/05_PhD/YOLO/tik_2/etiketler/'

i=0
j=0
k=0
conf_tresh=0.40

# to be sure not adding labels under conf_tresh before creating YOLO format labeling text 
# check confidence scores then create text file and write coordinate information for each object     
for i in range(len(data)):
    if (data[i]['objects'] != []):
        conf=0
        for k in range(len(data[i]['objects'])):
            if (data[i]['objects'][k]['confidence']>conf_tresh):
                conf=conf+1
        if (conf>=1):
            kaynak_1=(kaynak+data[i]['filename'][20:-3]+"jpg")
            hedef_1=(hedef+data[i]['filename'][20:-3]+"jpg")
            shutil.copyfile(kaynak_1,hedef_1)
            file_name=(hedef+data[i]['filename'][20:-3]+"txt")
            with open(file_name, "w") as outfile:
                for j in range(len(data[i]['objects'])):
                    if (data[i]['objects'][j]['confidence']>conf_tresh):
                        outfile.write(str(data[i]['objects'][j]['class_id']))
                        outfile.write(" ")
                        outfile.write(str(data[i]['objects'][j]['relative_coordinates']['center_x']))
                        outfile.write(" ")
                        outfile.write(str(data[i]['objects'][j]['relative_coordinates']['center_y']))
                        outfile.write(" ")
                        outfile.write(str(data[i]['objects'][j]['relative_coordinates']['width']))
                        outfile.write(" ")
                        outfile.write(str(data[i]['objects'][j]['relative_coordinates']['height']))
                        outfile.write(" ")
                        outfile.write("\n")
                outfile.close()