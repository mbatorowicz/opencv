#Odczytuje obrazy z folderu podanego jako pierwszy argument i wyszukuje twarz.
#Znalezione twarze zapisuje w odrębnych plikach w folderze podanym jako drugi argument.

import cv2
import sys
import os

imagePath = sys.argv[1]
newimagePath = sys.argv[2]
new_dimensionX = 36
new_dimensionY = 36

for file_type in [imagePath]:
    for img in os.listdir(file_type):
        line = file_type+'/'+img
        print(line)
        image = cv2.imread(file_type+'/'+img)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(36, 36))

        print("[INFO] Found {0} Faces!".format(len(faces)))

        for (x, y, w, h) in faces:
            #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_gray = gray[y:y + h, x:x + w] 
            print("[INFO] Object found. Saving locally.")
            newimage = cv2.resize(roi_gray,(int(new_dimensionX), int(new_dimensionY)))
            cv2.imwrite(newimagePath + '/'+ str(x) + str(y) + str(w) + str(h) + '.jpg', newimage)
