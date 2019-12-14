#Odczytuje obrazy z folderu podanego jako pierwszy argument,
#obraca o podany (jako trzeci argument) kąt i zapisuje  
#w folderze podanym jako drugi argument.
#Jako czwarty argument trzeba podać skalę 1 - bez zmian, 0.3 - 30%

import cv2
import sys
import os
import numpy

imagePath = sys.argv[1]
newimagePath = sys.argv[2]
rotation = sys.argv[3]
scale = sys.argv[4]

for file_type in [imagePath]:
    for img in os.listdir(file_type):
        
        line = file_type+'/'+img
        print(line)
        image = cv2.imread(file_type+'/'+img)
        (h, w) = image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, int(rotation), float(scale))
        newimage = cv2.warpAffine(image, M, (int(w), int(h)))
        crop_img = newimage[int((h/2)-(h*float(scale))/2):int((h/2)-(h*float(scale))/2)+int(h*float(scale)), int((w/2)-(w*float(scale))/2):int((w/2)-(w*float(scale))/2)+int(w*float(scale))]
        cv2.imwrite(newimagePath + '/' + img + '_rotate.jpg', crop_img)
